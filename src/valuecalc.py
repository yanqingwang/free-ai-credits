"""统一折算：一条 offer 的「月价值（USD）」。

优先级：
1. value_override_usd         —— 人工指定
2. credits_usd / valid_months —— 一次性金额摊销
3. checkin_tokens_day×30      —— 每日签到送 tokens
4. tokens_day×30 / tokens_month —— 限速型免费层的理论上限
其他情况返回 None（渲染为「— 限速免费」或「待核」）。
"""
import datetime as dt

CNY_PER_USD = 7.2


def _offer(e: dict) -> dict:
    return e.get("offer") or {}


def monthly_value(entry: dict) -> tuple[float | None, str]:
    """Returns (usd_per_month|None, formula_text)."""
    offer = _offer(entry)
    if entry.get("value_override_usd") is not None:
        return float(entry["value_override_usd"]), "人工指定"

    est = entry.get("est_usd_per_mtok")
    if not est:
        return None, ""

    credit = None
    if offer.get("credits_usd"):
        months = offer.get("valid_months") or 1
        credit = float(offer["credits_usd"]) / max(int(months), 1)
        formula = f"${offer['credits_usd']} 摊 {months} 月"
    elif offer.get("credits_cny"):
        months = offer.get("valid_months") or 1
        credit = float(offer["credits_cny"]) / CNY_PER_USD / max(int(months), 1)
        formula = f"¥{offer['credits_cny']} ≈ $(摊 {months} 月)"

    day_tokens = int(offer.get("checkin_tokens_day") or 0)
    if day_tokens:
        v = day_tokens * 30 / 1e6 * float(est)
        if credit and credit > v:
            return credit, formula or ""
        return v, f"签到 {day_tokens}/日 × 30 × ${est}/1M"

    td = int(offer.get("tokens_day") or 0)
    tm = int(offer.get("tokens_month") or 0)
    if td:
        v = td * 30 / 1e6 * float(est)
        if credit and credit > v:
            return credit, formula or ""
        return v, f"{td:,} tokens/日 × 30 × ${est}/1M"
    if tm:
        v = tm / 1e6 * float(est)
        if credit and credit > v:
            return credit, formula or ""
        return v, f"{tm:,} tokens/月 × ${est}/1M"

    if credit:
        return credit, formula or ""
    return None, ""


def staleness(entry: dict, max_days: int = 45) -> int | None:
    v = entry.get("verified")
    if not v:
        return None
    try:
        d = dt.date.fromisoformat(str(v))
        return (dt.date.today() - d).days
    except ValueError:
        return None
