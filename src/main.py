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
from src import links                        # noqa: E402
from src.valuecalc import valuations, staleness  # noqa: E402
from src.render import table, inject_readme, report as render_report  # noqa: E402


def load_offers() -> list:
    with open(REPO_ROOT / "data" / "offers.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("offers") or []


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-links", action="store_true")
    ap.add_argument("--mail", action="store_true", help="发送邮件日报（需 SMTP secrets）")
    args = ap.parse_args()

    entries = load_offers()
    for e in entries:
        vals = valuations(e)
        e["_vals"] = vals
        e["_recur"] = vals["recurring"][0]
        e["_once"] = vals["once"][0]

        stale_days = staleness(e)
        e["_stale"] = bool(stale_days and stale_days > 45)

        bad_links = []
        locked = []
        if not args.skip_links:
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

    # 排序：持续价值优先，其次一次性，无估值限速型随后，待核最后
    conf_rank = {"high": 0, "medium": 1, "low": 2}
    entries.sort(key=lambda e: (
        0 if e["_recur"] or e["_once"] else 1,
        -(e["_recur"] or 0),
        -(e["_once"] or 0),
        conf_rank.get(e.get("confidence"), 3),
    ))

    today = dt.date.today().isoformat()
    inject_readme(str(REPO_ROOT / "README.md"), table(entries, "zh"), today, "zh")
    inject_readme(str(REPO_ROOT / "README_EN.md"), table(entries, "en"), today, "en")

    rep_dir = REPO_ROOT / "reports"
    rep_dir.mkdir(exist_ok=True)
    y, w, _ = dt.date.today().isocalendar()
    render_report(entries, str(rep_dir / f"{y}-W{w:02d}.md"))
    render_report(entries, str(rep_dir / "weekly.md"))

    # 邮件日报（secrets 缺失时静默跳过，不影响报告产出）
    if args.mail:
        from src import mailer
        if mailer.enabled():
            mailer.send(f"免费额度日报 {today}（valuation + 链接体检）",
                        (rep_dir / "weekly.md").read_text(encoding="utf-8"))
            print("邮件已发送", file=sys.stderr)
        else:
            print("SMTP secrets 缺失，跳过邮件", file=sys.stderr)

    # state 记录（审计用，供未来 diff）
    state = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "offers": {e["id"]: {
            "recurring_usd": e["_recur"], "once_usd": e["_once"],
            "stale": e["_stale"], "bad_links": e["_bad_links"],
        } for e in entries},
    }
    sp = REPO_ROOT / "data" / "scan-state.json"
    sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    for e in entries:
        flag = "🚫" if e["_link_bad"] else ("⚠️stale" if e["_stale"] else "✅")
        print(f"[{e['id']}] {flag} recur={e['_recur']} once={e['_once']} bad={len(e['_bad_links'])}/locked={len(e.get('_locked', []))}", file=sys.stderr)


if __name__ == "__main__":
    main()
