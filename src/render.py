"""Render: README table injection + weekly snapshot report."""
import datetime as dt

CATEGORIES = {"免费层": "🆓", "试用金": "🎁", "签到积分": "✅", "一次性赠送": "💪", "限时活动": "⏳", "其他（非免费）": "ℹ️"}


def _expiry_display(offer: dict) -> str:
    exp = offer.get("expiry")
    if exp:
        try:
            d = dt.date.fromisoformat(str(exp))
            left = (d - dt.date.today()).days
            return f"{exp}（剩 {left} 天 ⏰）" if left >= 0 else f"{exp}（已过期 ❌）"
        except ValueError:
            return str(exp)
    return "长期有效"


def table(entries: list) -> str:
    rows = [
        "| # | 厂商 | 类型 | 免费内容（模型） | 折算月价值 | 注册方式 | 限制条件 | 有效期 | 信号 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    no = 0
    for e in entries:
        no += 1
        offer = e.get("offer") or {}
        typ = offer.get("type", "?")
        cat = CATEGORIES.get(typ, "✔️")
        web = e.get("website") or ""
        link = f"[{e['provider']}]({web})" if web else f"**{e['provider']}**"
        models = ", ".join(e.get("models") or []) or "—"
        if len(models) > 90:
            models = models[:89] + "…"

        quant = []
        if offer.get("requests_day"):
            quant.append(f"{offer['requests_day']:,} 请求/日")
        if offer.get("tokens_day"):
            quant.append(f"{offer['tokens_day']:,} tokens/日")
        if offer.get("tokens_month"):
            quant.append(f"{offer['tokens_month']:,} tokens/月")
        if offer.get("credits_usd"):
            quant.append(f"${offer['credits_usd']} 赠金")
        if offer.get("credits_cny"):
            quant.append(f"¥{offer['credits_cny']} 券")
        if offer.get("signup_tokens"):
            quant.append(f"注册赠 {offer['signup_tokens']:,} tokens")
        if offer.get("checkin_tokens_day"):
            quant.append(f"签到 {offer['checkin_tokens_day']:,} tokens/日")
        if offer.get("points_monthly") or offer.get("points_daily"):
            quant.append(f"积分 {offer.get('points_monthly') or 0}/月 + {offer.get('points_daily') or 0}/日")
        msg = " + ".join(quant) or "限速免费（量级未公布）"
        free = f"{cat} {typ}：{msg}｜模型：{models}"

        val = e.get("_value")
        val_d = ("**$%.2f/月**" % val) if val is not None else "—（限速内自由）"
        if e.get("confidence") == "low":
            val_d += " ⚠️待核"
        if e.get("_stale"):
            val_d += " ⚠️数据>45天未复核"
        if e.get("_link_bad"):
            val_d += " 🚫链接失效"

        signup = (e.get("signup") or "见官网").replace("|", "/").replace("\n", " ")
        if len(signup) > 80:
            signup = signup[:79] + "…"
        restr = (e.get("restrictions") or "—").replace("|", "/").replace("\n", " ")
        if len(restr) > 90:
            restr = restr[:89] + "…"
        conf = {"high": "✅双源", "medium": "☑️单源", "low": "⚠️待核"}.get(e.get("confidence"), "")
        rows.append(
            f"| {no} | {link} | {typ} | {free} | {val_d} | {signup} | {restr} | {_expiry_display(offer)} | {conf} |"
        )
    return "\n".join(rows)


def inject_readme(readme_path: str, table_text: str, generated_on: str) -> None:
    with open(readme_path, encoding="utf-8") as f:
        md = f.read()
    block = (
        "<!-- AUTO-TABLE-START -->\n"
        f"_{generated_on} 自动重建 · 数据定义于 [`data/offers.yml`](data/offers.yml)_{_now()}\n\n"
        + table_text
        + "\n<!-- AUTO-TABLE-END -->"
    )
    start = md.index("<!-- AUTO-TABLE-START -->")
    end = md.index("<!-- AUTO-TABLE-END -->") + len("<!-- AUTO-TABLE-END -->")
    md = md[:start] + block + md[end:]
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md)


def _now() -> str:
    return ""


def report(entries: list, path: str) -> str:
    today = dt.date.today().isoformat()
    lines = [
        "# 免费额度周报快照",
        "",
        f"**生成日：{today}（UTC）**",
        "",
        "数据源：`data/offers.yml`（当周探活 + 估值重排），结论以官方控制台为准。",
        "",
        table(entries),
        "",
        "## 本期挂掉的链接（探活失败）",
        "",
    ]
    bad = [f"- 🚫 [{e['provider']}] {u}" for e in entries for u in (e.get("_bad_links") or [])]
    if bad:
        lines += [x for x in bad if x]
    else:
        lines.append("- 全部官方链接探活通过 ✅")
    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path
