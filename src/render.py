"""Render: bilingual auto tables (zh/en) + README injection + report snapshot."""
import datetime as dt

import src.i18n as i18n

CATEGORIES = {"免费层": "🆓", "试用金": "🎁", "签到积分": "✅", "一次性赠送": "💪", "限时活动": "⏳", "其他（非免费）": "ℹ️"}

HEADERS = {
    "zh": "| # | 厂商 | 类型 | 免费内容（模型） | 持续价值(USD/月) | 一次性价值(USD) | 注册方式 | 限制条件 | 有效期 | 官方验证 | 第三方验证 |",
    "en": "| # | Provider | Type | Free content (models) | Recurring value (USD/mo) | One-time value (USD) | Signup | Restrictions | Validity | Official sources | Third-party sources |",
}
SEP = "|---|---|---|---|---|---|---|---|---|---|---|"

L = {
    "zh": {"longterm": "长期有效", "left": "（剩 {d} 天 ⏰）", "expired": "（已过期 ❌）",
           "free_rate": "—（限速内自由）", "total": "> 表内 {n} 条合计：持续 ≈ **${r}/月** · 一次性 ≈ **${o}**", "dash": "—"},
    "en": {"longterm": "ongoing", "left": "({d} days left ⏰)", "expired": "(expired ❌)",
           "free_rate": "— (uncapped within rate limit)", "total": "> Totals over {n} rows: recurring ≈ **${r}/mo** · one-time ≈ **${o}**", "dash": "—"},
}


def _units(lang: str) -> dict:
    zh = {"req": "请求/日", "tok_d": "tokens/日", "tok_m": "tokens/月", "usd": "赠金", "cny": "券",
          "claim": "领", "gift": "注册赠", "gift_p": "注册赠", "gift_tok": "注册赠", "checkin": "签到",
          "pts_m": "积分/月", "pts_d": "/日", "per": "积分", "model": "模型"}
    en = {"req": "req/day", "tok_d": "tokens/day", "tok_m": "tokens/mo", "usd": "credit", "cny": "voucher",
          "claim": "claim", "gift": "signup gift", "gift_p": "signup gift", "gift_tok": "signup gift", "checkin": "check-in",
          "pts_m": "pts/mo", "pts_d": "/day", "per": "pts", "model": "models"}
    return zh if lang == "zh" else en


def _cell(s: str, limit: int) -> str:
    s = (s or "").replace("|", "/").replace("\n", " ")
    return s[: limit - 1] + "…" if len(s) > limit else s


def _host(url: str) -> str:
    import urllib.parse
    return urllib.parse.urlparse(url).netloc or url[:24]


def table(entries: list, lang: str = "zh") -> str:
    U = _units(lang)
    T = L[lang]
    rows = [HEADERS[lang], SEP]
    no = 0
    tot_recur = 0.0
    tot_once = 0.0

    for e in entries:
        no += 1
        offer = e.get("offer") or {}
        typ_zh = offer.get("type", "?")
        typ = i18n.TYPE_LABELS.get(typ_zh, typ_zh) if lang == "en" else typ_zh
        cat = CATEGORIES.get(typ_zh, "✔️")

        provider = e["provider"]
        link = f"[{provider}]({e.get('website') or ''})" if e.get("website") else f"**{provider}**"

        if lang == "en" and e["id"] in i18n.MODELS:
            models = ", ".join(i18n.MODELS[e["id"]])
        else:
            models = ", ".join(e.get("models") or []) or "—"
        if len(models) > 90:
            models = models[:89] + "…"

        quant = []
        if offer.get("requests_day"):
            quant.append(f"{offer['requests_day']:,} {U['req']}")
        if offer.get("tokens_day"):
            quant.append(f"{offer['tokens_day']:,} {U['tok_d']}")
        if offer.get("tokens_month"):
            quant.append(f"{offer['tokens_month']:,} {U['tok_m']}")
        if offer.get("invite_tokens_monthly"):
            quant.append(f"{U['gift_tok']} {(offer['invite_tokens_monthly']):,} {U['tok_m']}")
        if offer.get("credits_usd"):
            quant.append(f"${offer['credits_usd']} {U['usd']}")
        if offer.get("credits_cny"):
            quant.append(f"¥{offer['credits_cny']} {U['cny']}")
        if offer.get("credits_day"):
            quant.append(f"{U['claim']} {offer['credits_day']:,} credits/日")
        if offer.get("signup_points"):
            quant.append(f"{U['gift_p']} {offer['signup_points']:,} 点")
        if offer.get("signup_tokens"):
            quant.append(f"{U['gift_tok']} {offer['signup_tokens']:,} tokens")
        if offer.get("checkin_tokens_day"):
            quant.append(f"{U['checkin']} {offer['checkin_tokens_day']:,} tokens/日")
        if offer.get("points_monthly"):
            quant.append(f"{offer['points_monthly']:,} {U['pts_m']}")
        if offer.get("points_daily"):
            quant.append(f"{U['checkin']} {offer['points_daily']:,} 点{U['pts_d']}")
        msg = " + ".join(quant)

        if lang == "zh":
            msg_zh = msg if msg else ("限速免费（量级未公布）" if typ_zh == "免费层" else typ_zh)
            free = f"{cat} {typ_zh}：{msg_zh}｜模型：{models}"
        else:
            defq = ("rate-limited free (no published volume)" if typ_zh == "免费层" else typ)
            free = f"{cat} {typ}：{msg if msg else defq}｜{U['model']}：{models}"

        def fmt(v, once=False):
            if v is None:
                return T["dash"]
            return f"$**{v:g}{'' if once else '/月'}**" if lang == "zh" else f"**${v:g}{'' if once else '/mo'}**"

        vals = e.get("_vals") or {}
        rv, rt = vals.get("recurring", (None, ""))
        ov, ot = vals.get("once", (None, ""))
        if rv is not None:
            tot_recur += rv
        if ov is not None:
            tot_once += ov
        recur_d = fmt(rv)
        once_d = fmt(ov, once=True)
        if (ot or rt):
            formulas = " · ".join(x for x in (rt, ot) if x)
            if len(formulas) > 60:
                formulas = formulas[:59] + "…"
            recur_d += f"<br>_{_cell(formulas, 60)}_"
        if e.get("confidence") == "low":
            once_d += " ⚠️"
        if e.get("_stale"):
            recur_d += " ⏳"
        if e.get("_link_bad"):
            recur_d += " 🚫"
        if e.get("_locked"):
            recur_d += " 🔒"

        signup = (i18n.SIGNUP.get(e["id"], e.get("signup") or "见官网") if lang == "en" else (e.get("signup") or "见官网"))
        restr = (i18n.RESTRICTIONS.get(e["id"], e.get("restrictions") or "—") if lang == "en" else (e.get("restrictions") or "—"))

        exp = offer.get("expiry")
        if exp:
            try:
                d = dt.date.fromisoformat(str(exp))
                left = (d - dt.date.today()).days
                valid = f"{exp}{(T['left'].format(d=left) if left >= 0 else T['expired'])}"
            except ValueError:
                valid = str(exp)
        else:
            valid = T["longterm"]

        conf = e.get("confidence") or ""
        sig = e.get("_sources") or {}
        sig_official = sig.get("official") or []
        sig_third = sig.get("third") or []
        empty = {"zh": "—（本会话未直接读到第三方源）", "en": "— (no third-party source read)"}
        vals_key = "zh" if lang == "zh" else "en"
        off_d = "<br>".join(f"✅ [{_host(u)}]({u})" for u in sig_official) or "—"
        third_d = "<br>".join(f"📄 [{_host(u)}]({u})" for u in sig_third) or empty[vals_key]

        rows.append(f"| {no} | {link} | {typ} | {free} | {recur_d} | {once_d} | {_cell(signup, 80)} | {_cell(restr, 90)} | {valid} | {off_d} | {third_d} |")

    if tot_recur or tot_once:
        rows.append(T["total"].format(n=no, r=round(tot_recur), o=round(tot_once)))
    return "\n".join(rows)


def inject_readme(readme_path: str, table_text: str, generated_on: str, lang: str = "zh") -> None:
    with open(readme_path, encoding="utf-8") as f:
        md = f.read()
    src = {"zh": data_src_lang(lang), "en": "data/offers.yml"}[lang]
    caption = {"zh": f"_{generated_on} 自动重建 · 数据定义于 [`data/offers.yml`]({src})_",
               "en": f"_{generated_on} auto-rebuilt · source of truth in [`data/offers.yml`]({src})_"}[lang]
    block = (
        "<!-- AUTO-TABLE-START -->\n"
        + caption + "\n\n"
        + table_text
        + "\n<!-- AUTO-TABLE-END -->"
    )
    start = md.index("<!-- AUTO-TABLE-START -->")
    end = md.index("<!-- AUTO-TABLE-END -->") + len("<!-- AUTO-TABLE-END -->")
    md = md[:start] + block + md[end:]
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md)


def data_src_lang(lang: str) -> str:
    return "data/offers.yml"


def report(entries: list, path: str) -> str:
    zh = table(entries, "zh")
    en = table(entries, "en")
    today = dt.date.today().isoformat()
    lines = [
        "# 免费额度日报快照",
        "",
        f"**生成日：{today}（UTC）**",
        "",
        "数据源：`data/offers.yml`（当期探活 + 估值重排），结论以官方控制台为准。",
        "",
        "## 中文榜",
        "",
        zh,
        "",
        "## English table",
        "",
        en,
        "",
        "## 链接体检",
        "",
    ]
    bad = [f"- 🚫 [{e['provider']}] {u}" for e in entries for u in (e.get("_bad_links") or [])]
    locked = [f"- 🔒 [{e['provider']}] {u}（403：需登录/反爬，非死链）" for e in entries for u in (e.get("_locked") or [])]
    if bad or locked:
        lines += bad + locked
    else:
        lines.append("全部官方链接探活通过 ✅ / All links alive")
    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path
