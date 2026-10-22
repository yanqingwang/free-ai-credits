"""free-ai-credits scanner orchestrator.

用法：
    python -m src.main                # 探活 + 折算 + 重建 README 表格 + reports 周报
    python -m src.main --skip-links   # 跳过探活（离线快速排版）
    python -m src.main --no-stale     # 不标 stale
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import yaml                                  # noqa: E402
from src import changelog, links             # noqa: E402
from src.valuecalc import valuations, staleness  # noqa: E402
from src.render import table, inject_readme, report as render_report  # noqa: E402


def load_offers() -> list:
    with open(REPO_ROOT / "data" / "offers.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("offers") or []


def load_sources() -> dict:
    """id → {"official": [...], "third": [...]}"""
    p = REPO_ROOT / "data" / "sources.yml"
    if not p.exists():
        return {}
    with open(p, encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}
    return {k: {"official": (v or {}).get("official") or [],
                "third": (v or {}).get("third_party") or []} for k, v in raw.items()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-links", action="store_true")
    ap.add_argument("--mail", action="store_true", help="发送邮件日报（需 SMTP secrets）")
    args = ap.parse_args()

    src_index = load_sources()
    state_path = REPO_ROOT / "data" / "scan-state.json"
    previous = changelog.load_previous(state_path)   # 昨天提交的基线，用于「较昨日」列

    entries = load_offers()
    for e in entries:
        vals = valuations(e)
        e["_vals"] = vals
        e["_recur"] = vals["recurring"][0]
        e["_once"] = vals["once"][0]
        e["_sources"] = src_index.get(e["id"], {})
        n_off = len(e["_sources"]["official"])
        n_third = len(e["_sources"]["third"])
        e["_conf_rank"] = 0 if (n_off and n_third) else (1 if (n_off or n_third) else 2)

        stale_days = staleness(e)
        e["_stale"] = bool(stale_days and stale_days > 45)

        bad_links = []
        locked = []
        if args.skip_links:                       # 离线排版：沿用昨日探活结果，避免误报「死链修复」
            prev_offer = (previous.get("offers") or {}).get(e["id"]) or {}
            bad_links = list(prev_offer.get("bad_links") or [])
            locked = list(prev_offer.get("locked") or [])
        else:
            for key in ("website", "docs"):
                u = e.get(key)
                if u and u.startswith("http"):
                    code = links.check(u)
                    if code == 403:
                        locked.append(f"{key}:{u}")
                    elif code is None or code >= 400:
                        bad_links.append(f"{key}:{u} (HTTP {code or 'NO'})")
        e["_bad_links"] = bad_links
        e["_locked"] = locked
        e["_link_bad"] = bool(bad_links)

    # 排序：持续价值优先，其次一次性，无估值限速型随后；信源贫乏条目最后
    removed = changelog.annotate(entries, previous)
    entries.sort(key=lambda e: (
        0 if e["_recur"] or e["_once"] else 1,
        -(e["_recur"] or 0),
        -(e["_once"] or 0),
        e["_conf_rank"],
    ))

    today = dt.date.today().isoformat()
    inject_readme(str(REPO_ROOT / "README.md"), table(entries, "zh", removed), today, "zh")
    inject_readme(str(REPO_ROOT / "README_EN.md"), table(entries, "en", removed), today, "en")

    rep_dir = REPO_ROOT / "reports"
    rep_dir.mkdir(exist_ok=True)
    y, w, _ = dt.date.today().isocalendar()
    render_report(entries, str(rep_dir / f"{y}-W{w:02d}.md"), removed)
    render_report(entries, str(rep_dir / "weekly.md"), removed)

    # 邮件日报（secrets 缺失时静默跳过，不影响报告产出）
    if args.mail:
        from src import mailer
        if mailer.enabled():
            body = (rep_dir / "weekly.md").read_text(encoding="utf-8")
            attach = str(rep_dir / "weekly.md")
            mailer.send(f"Free AI Credits Daily · 免费额度日报 {today}（valuation + link health）", body, attach)
            print("邮件已发送（库主）", file=sys.stderr)
            # 订阅者：daily 每天发，weekly 仅周一（UTC）发；逐个失败隔离
            try:
                from src import subscribers
                subs = subscribers.sendable(dt.date.today())
            except SystemExit:
                subs = []
            for email, freq in subs:
                subject = (
                    f"Free AI Weekly Digest {today} · 周报（ valuation + link health）"
                    if freq == "weekly"
                    else f"Free AI Credits Daily {today} · 日报（valuation + link health）"
                )
                try:
                    mailer.send(subject, body, attach, to=email)
                    print(f"邮件已发送（订阅者 {email}）", file=sys.stderr)
                except Exception as exc:                 # 单个失败的订阅者不影响其余
                    print(f"订阅者 {email} 发送失败: {exc}", file=sys.stderr)
        else:
            print("SMTP secrets 缺失，跳过邮件", file=sys.stderr)

    # state 记录（审计用，供未来 diff）
    state = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "offers": {e["id"]: {
            "provider": e["provider"],
            "recurring_usd": e["_recur"], "once_usd": e["_once"],
            "official_sources": len(e["_sources"]["official"]), "third_sources": len(e["_sources"]["third"]),
            "stale": e["_stale"], "bad_links": e["_bad_links"], "locked": e["_locked"],
            "snapshot": changelog.snapshot(e),
        } for e in entries},
    }
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    for e in entries:
        flag = "🚫" if e["_link_bad"] else ("⚠️stale" if e["_stale"] else "✅")
        print(f"[{e['id']}] {flag} recur={e['_recur']} once={e['_once']} bad={len(e['_bad_links'])}/locked={len(e.get('_locked', []))}", file=sys.stderr)


if __name__ == "__main__":
    main()
