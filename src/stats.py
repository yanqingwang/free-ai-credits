"""对 data/offers.yml 首批全量数据做静态统计分析，输出 Markdown 报告。

用法：
    python src/stats.py            # 打印统计摘要
    python src/stats.py --write    # 同时写入 reports/stats-<date>.md
"""
import argparse
import datetime as dt
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import yaml                                        # noqa: E402
from src.valuecalc import valuations, staleness    # noqa: E402


def load():
    with open(REPO_ROOT / "data" / "offers.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    offers = data.get("offers") or []
    with open(REPO_ROOT / "data" / "sources.yml", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}
    srcs = {k: {"official": (v or {}).get("official") or [],
                "third": (v or {}).get("third_party") or []} for k, v in raw.items()}
    return offers, srcs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    today = dt.date.today()
    offers, srcs = load()
    n = len(offers)

    countries = Counter((o.get("country") or "未标注") for o in offers)
    oss = Counter((o.get("open_source") or "未标注") for o in offers)
    types = Counter(((o.get("offer") or {}).get("type") or "未标注") for o in offers)
    conf = Counter((o.get("confidence") or "未标注") for o in offers)

    vals = {o["id"]: valuations(o) for o in offers}
    stales = {o["id"]: staleness(o) for o in offers}
    verified_days = [(o["id"], o.get("verified")) for o in offers]

    bench = [(o["provider"], o["bench_model"], o["bench_score"]) for o in offers
             if o.get("bench_model") and o.get("bench_score") is not None]

    recurring = [(o["provider"], vals[o["id"]]["recurring"][0]) for o in offers
                 if vals[o["id"]]["recurring"][0]]
    once = [(o["provider"], vals[o["id"]]["once"][0]) for o in offers
            if vals[o["id"]]["once"][0]]
    recurring.sort(key=lambda x: -x[1])
    once.sort(key=lambda x: -x[1])
    no_val = [o["provider"] for o in offers
              if not vals[o["id"]]["recurring"][0] and not vals[o["id"]]["once"][0]]

    sig = {"high": 0, "other": 0}
    prov_1021 = 0
    for o in offers:
        v = str(o.get("verified") or "")
        if v == str(today):
            prov_1021 += 1
        if o.get("confidence") == "high":
            sig["high"] += 1
        else:
            sig["other"] += 1

    src_stat = Counter()
    no_src_ids = []
    for o in offers:
        s = srcs.get(o["id"], {})
        off, th = len(s.get("official") or []), len(s.get("third") or [])
        if off and th:
            src_stat["官方+第三方"] += 1
        elif off:
            src_stat["仅官方"] += 1
        elif th:
            src_stat["仅第三方"] += 1
        else:
            src_stat["无信源"] += 1
            no_src_ids.append(o["provider"])

    stale_over45 = [o["provider"] for o in offers
                    if (stales[o["id"]] or 0) > 45]

    top_cn = [o["provider"] for o in offers if o.get("country") == "中国"]

    verified = {str(o.get("verified") or "") for o in offers}
    batch_day = max(verified) if verified else str(today)

    lines = []
    A = lines.append
    A(f"# free-ai-credits 首批数据统计分析 · {today.isoformat()}")
    A("")
    A(f"**样本**：`data/offers.yml` 全量 {n} 条（批次核查日 {batch_day}，报告生成日 {today.isoformat()}）")
    A("")
    A("## 1. 总览")
    A("")
    A("| 维度 | 结果 |")
    A("|---|---|")
    A(f"| 条目总数 | {n} |")
    A(f"| 中国厂商条目 | {countries.get('中国', 0)}（{countries.get('中国', 0) / n:.0%}）|")
    A(f"| 有可折算价值（持续或一次性） | {n - len(no_val)} / {n} |")
    A(f"| 限速/量级未公布（不折算金额） | {len(no_val)} |")
    A(f"| 置信度 high | {sig['high']}（{sig['high'] / n:.0%}）|")
    A(f"| 批次日（{batch_day}）重新核查 | {prov_1021} |")
    A(f"| 核验超 45 天（stale） | {len(stale_over45)} |")
    A("")
    A("## 2. 国家分布")
    A("")
    A("| 国家 | 条数 | 占比 |")
    A("|---|---|---|")
    for c, cnt in countries.most_common():
        A(f"| {c} | {cnt} | {cnt / n:.0%} |")
    A("")
    A("## 3. 开源属性")
    A("")
    A("| 类型 | 条数 | 占比 |")
    A("|---|---|---|")
    for c, cnt in oss.most_common():
        A(f"| {c} | {cnt} | {cnt / n:.0%} |")
    A("")
    A("## 4. 免费机制类型")
    A("")
    A("| 类型 | 条数 | 占比 |")
    A("|---|---|---|")
    for c, cnt in types.most_common():
        A(f"| {c} | {cnt} | {cnt / n:.0%} |")
    A("")
    A("注：非「免费层/试用金/签到积分/一次性赠送/限时活动」五类的条目（如 OpenCode Zen 无免费层）为对照样本，如实标注。")
    A("")
    A("## 5. 价值分布")
    A("")
    if recurring:
        top_r = recurring[0]
        A(f"- **持续价值榜首**：{top_r[0]} ≈ ${top_r[1]:,.0f}/月")
        rsum = sum(x[1] for x in recurring)
        A(f"- 持续价值合计（全部条目）：≈ ${rsum:,.0f}/月")
        A(f"- 中位数：≈ ${recurring[len(recurring) // 2][1]:,.2f}/月")
    A("")
    A("### 持续价值 Top 10（USD/月）")
    A("")
    A("| # | 厂商 | $/月 |")
    A("|---|---|---|")
    for i, (p, v) in enumerate(recurring[:10], 1):
        A(f"| {i} | {p} | {v:,.2f} |")
    A("")
    A("### 一次性价值 Top 10（USD）")
    A("")
    A("| # | 厂商 | $（一次性） |")
    A("|---|---|---|")
    for i, (p, v) in enumerate(once[:10], 1):
        A(f"| {i} | {p} | {v:,.2f} |")
    A("")
    if no_val:
        A(f"**无金额折算（{len(no_val)} 条）**：{'、'.join(no_val)}——多为纯限速免费层或量级未公布，按数据纪律不编造金额。")
        A("")
    A("## 6. 行业评分覆盖")
    A("")
    A(f"有第三方行业评分（AA Index v4.3 等）的模型厂商：**{len(bench)} / {n}**。")
    A("")
    A("| 厂商 | 代表模型 | 评分 |")
    A("|---|---|---|")
    for p, m, s in sorted(bench, key=lambda x: -x[2]):
        A(f"| {p} | {m} | {s:g} |")
    A("")
    A("## 7. 信源结构")
    A("")
    A("| 信源构成 | 条数 |")
    A("|---|---|")
    for k in ("官方+第三方", "仅官方", "仅第三方", "无信源"):
        A(f"| {k} | {src_stat.get(k, 0)} |")
    A("")
    if no_src_ids:
        A(f"无信源条目：{'、'.join(no_src_ids)}")
        A("")
    A("## 8. 数据质量与局限")
    A("")
    A(f"- 置信度非 high 的条目 {sig['other']} 条（medium/low），README 中 low 标 ⚠️。")
    if stale_over45:
        A(f"- 核验超 45 天：{'、'.join(stale_over45)}（README 标 ⏳，待下轮重核）。")
    A("- 国内外双版本厂商（Qoder/Trae/WorkBuddy/腾讯 TokenHub 等）均拆分为独立条目，各按所在法域政策单独核查，统计不重复计入。")
    A("- 评分未覆盖的厂商（豆包、星火、商汤、文心、Perplexity、混元 Hy3 等）是无法在评分方官方榜单直证的，宁缺毋滥留空。")
    A("")
    A(f"*报告由 `python src/stats.py --write` 生成 · {today.isoformat()}（UTC）*")

    text = "\n".join(lines) + "\n"
    print(text)
    if args.write:
        out = REPO_ROOT / "reports" / f"stats-{today.isoformat()}.md"
        out.parent.mkdir(exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[written] {out}")


if __name__ == "__main__":
    main()
