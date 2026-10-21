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
    pv = entry.get("point_value_usd")
    candidates: list[tuple[float, str]] = []

    # 积分制： points_monthly + points_daily×30 按 1 点价值折算
    if pv:
        pm = int(offer.get("points_monthly") or 0)
        pd = int(offer.get("points_daily") or 0)
        pts = pm + pd * 30
        if pts:
            candidates.append((pts * float(pv), f"({pm} + {pd}×30) 点 × ${pv}/点"))

    # credit 类： credits_day×30 有单价则折算
    if pv and offer.get("credits_day"):
        cd = int(offer["credits_day"])
        candidates.append((cd * 30 * float(pv), f"{cd} credits/日 × 30 × ${pv}/点"))

    if not est:
        if candidates:
            return max(candidates, key=lambda x: x[0])
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
    if credit:
        candidates.append((credit, formula))

    day_tokens = int(offer.get("checkin_tokens_day") or 0)
    if day_tokens:
        v = day_tokens * 30 / 1e6 * float(est)
        candidates.append((v, f"签到 {day_tokens}/日 × 30 × ${est}/1M"))

    td = int(offer.get("tokens_day") or 0)
    tm = int(offer.get("tokens_month") or 0)
    if td:
        candidates.append((td * 30 / 1e6 * float(est), f"{td:,} tokens/日 × 30 × ${est}/1M"))
    if tm:
        candidates.append((tm / 1e6 * float(est), f"{tm:,} tokens/月 × ${est}/1M"))

    if candidates:
        return max(candidates, key=lambda x: x[0])
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
