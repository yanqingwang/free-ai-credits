"""统一折算：把一条 offer 拆成「持续价值」与「一次性价值」两部分。

- 持续价值（recurring）：可长期每天/每月重复薅的部分——免费层日额度、签到积分、
  月度邀请返利等，按 30 天/月折算成 USD/月。
- 一次性价值（once）：只有一次的部分——注册赠金/积分/送 tokens、试用金，按
  原始金额展示（摊销月数写进公式备注，不除）。
- value_override_recurring_usd / value_override_once_usd 可人工指定任一侧。
"""
import datetime as dt

CNY_PER_USD = 7.2


def _offer(e: dict) -> dict:
    return e.get("offer") or {}


def valuations(entry: dict) -> dict:
    """Returns {"recurring": (usd|None, text), "once": (usd|None, text)}."""
    offer = _offer(entry)
    est = entry.get("est_usd_per_mtok")
    pv = entry.get("point_value_usd")
    recur: list[tuple[float, str]] = []
    once: list[tuple[float, str]] = []

    if entry.get("value_override_recurring_usd") is not None:
        recur.append((float(entry["value_override_recurring_usd"]), "人工指定（持续）"))
    if entry.get("value_override_once_usd") is not None:
        once.append((float(entry["value_override_once_usd"]), "人工指定（一次性）"))

    def per_mtok(a: float, b: float) -> float:
        return a / 1e6 * float(b)

    def p2s(x: float) -> str:
        return f"{x:,}"

    # ---------- 持续部分 ----------
    if pv:
        # 积分/credits 同属一个累计池，可加和；token 日额（多模型互斥）后面单独取 max
        pm = int(offer.get("points_monthly") or 0)
        pd = int(offer.get("points_daily") or 0)
        cd = int(offer.get("credits_day") or 0)
        pts = pm + pd * 30 + cd * 30
        if pts:
            parts = "+".join(x for x in (p2s(pm) + " 月包" if pm else "", f"{pd}×30 签到" if pd else "",
                                         f"{cd}×30 日领" if cd else "") if x)
            recur.append((pts * float(pv), f"({parts}) × ${pv}/点"))
    if est:
        ctd = int(offer.get("checkin_tokens_day") or 0)
        td = int(offer.get("tokens_day") or 0)
        tm = int(offer.get("tokens_month") or 0)
        im = int(offer.get("invite_tokens_monthly") or 0)
        if ctd:
            recur.append((per_mtok(ctd, est) * 30, f"签到 {ctd:,} tokens/日 × 30 × ${est}/1M"))
        if td:
            recur.append((per_mtok(td, est) * 30, f"{td:,} tokens/日 × 30 × ${est}/1M"))
        if tm:
            recur.append((per_mtok(tm, est), f"{tm:,} tokens/月 × ${est}/1M"))
        if im:
            recur.append((per_mtok(im, est), f"邀请返 {im:,} tokens/月 × ${est}/1M"))
        sp = int(offer.get("signup_tokens") or 0)
        if offer.get("valid_months") and sp:
            # 明确写 valid_months 的注册赠可视为摊销后的持续收益
            months = int(offer["valid_months"])
            recur.append((per_mtok(sp, est) / months, f"注册 {sp:,} tokens 摊 {months} 月 × ${est}/1M"))

    # ---------- 一次性部分 ----------
    credit = None
    if offer.get("credits_usd"):
        credit = float(offer["credits_usd"])
        months = offer.get("valid_months") or 1
        once.append((credit, f"${credit:g} 一次性（摊 {months} 月）"))
    elif offer.get("credits_cny"):
        credit = float(offer["credits_cny"]) / CNY_PER_USD
        once.append((credit, f"¥{offer['credits_cny']} ≈ ${credit:.2f} 一次性"))
    if pv:
        sp = int(offer.get("signup_points") or 0)
        if sp:
            once.append((sp * float(pv), f"注册赠 {sp:,} 点 × ${pv}/点"))
    if est:
        sp = int(offer.get("signup_tokens") or 0)
        if sp and not offer.get("valid_months"):   # 未声明摊销的注册赠按一次性展示
            once.append((per_mtok(sp, est), f"注册赠 {sp:,} tokens × ${est}/1M"))

    out = {}
    overrides = {
        "recurring": entry.get("value_override_recurring_usd"),
        "once": entry.get("value_override_once_usd"),
    }
    for key, pool in (("recurring", recur), ("once", once)):
        if overrides[key] is not None:          # 人工指定：完全短路该侧
            out[key] = (round(float(overrides[key]), 2), "人工指定")
        elif pool:
            best = max(pool, key=lambda x: x[0])
            out[key] = (round(best[0], 2), best[1])
        else:
            out[key] = (None, "")
    return out


def staleness(entry: dict, max_days: int = 45) -> int | None:
    v = entry.get("verified")
    if not v:
        return None
    try:
        d = dt.date.fromisoformat(str(v))
        return (dt.date.today() - d).days
    except ValueError:
        return None
