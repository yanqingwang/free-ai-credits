"""较昨日变化：把今天的扫描结果和 `data/scan-state.json`（昨天提交的基线）做 diff。

`table()` 会把这里产出的 `_delta` 渲染成榜单里的「较昨日」列；state 里额外保存
`snapshot`（offer 关键字段快照），这样明天的 diff 除了价值/链接，还能看到额度、
类型、模型池、到期日等变化。
"""
import json
import datetime as dt

import src.i18n as i18n

# offer 里会影响「免费内容」的字段 → (中文标签, 英文标签)
CONTENT_FIELDS = {
    "credits_usd": ("赠金", "credit"),
    "credits_cny": ("代金券", "voucher"),
    "credits_day": ("每日领取", "daily claim"),
    "requests_day": ("请求/日", "req/day"),
    "tokens_day": ("tokens/日", "tokens/day"),
    "tokens_month": ("tokens/月", "tokens/month"),
    "signup_points": ("注册积分", "signup points"),
    "signup_tokens": ("注册 tokens", "signup tokens"),
    "checkin_tokens_day": ("签到 tokens/日", "check-in tokens/day"),
    "points_monthly": ("积分/月", "points/month"),
    "points_daily": ("签到积分/日", "check-in points/day"),
    "invite_tokens_monthly": ("邀请 tokens/月", "invite tokens/month"),
    "valid_months": ("有效月数", "valid months"),
    "expiry": ("到期日", "expiry"),
}


def load_previous(path) -> dict:
    """读昨天的 state；文件缺失/损坏时返回 {}，首跑按「新增」处理。"""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f) or {}
    except (OSError, json.JSONDecodeError):
        return {}


def _plain(v):
    """YAML 可能给出 date 对象，state 必须是纯 JSON 类型。"""
    if isinstance(v, (dt.date, dt.datetime)):
        return v.isoformat()
    return v


def snapshot(entry: dict) -> dict:
    offer = entry.get("offer") or {}
    snap = {"type": _plain(offer.get("type")),
            "models": [str(m) for m in (entry.get("models") or [])]}
    for key in CONTENT_FIELDS:
        snap[key] = _plain(offer.get(key))
    return snap


def _n(v) -> str:
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, float):
        return f"{v:g}"
    if isinstance(v, int):
        return f"{v:,}"
    return str(v)


def _disp(key: str, v) -> str:
    """单字段展示值：金额带币种符号，其余走千分位。"""
    if v is None or v == "":
        return "—"
    if key == "credits_usd":
        return f"${_n(v)}"
    if key == "credits_cny":
        return f"¥{_n(v)}"
    return _n(v)


def _money(v) -> str:
    return "—" if v is None else f"${float(v):g}"


def _type_en(v) -> str:
    return i18n.TYPE_LABELS.get(v, v) if v else "—"


def changes(entry: dict, old: dict | None) -> list[tuple[str, str]]:
    """返回 [(中文说明, 英文说明)]；空列表 = 无变化。"""
    if not old:
        return [("🆕 新增", "🆕 new")]

    out: list[tuple[str, str]] = []
    new = snapshot(entry)
    old_snap = old.get("snapshot") or {}

    # 类型
    if old_snap.get("type") and new.get("type") and old_snap["type"] != new["type"]:
        out.append((f"类型 {old_snap['type']}→{new['type']}",
                    f"type {_type_en(old_snap['type'])}→{_type_en(new['type'])}"))

    # 双轨估值（旧 state 就有这两个字段）
    for key, zh, en, zh_unit, en_unit in (
        ("recurring_usd", "持续", "recurring", "/月", "/mo"),
        ("once_usd", "一次性", "one-time", "", ""),
    ):
        if key not in old:
            continue
        if old.get(key) != entry.get("_recur" if key == "recurring_usd" else "_once"):
            o = _money(old.get(key))
            n = _money(entry.get("_recur" if key == "recurring_usd" else "_once"))
            out.append((f"{zh} {o}→{n}{zh_unit}", f"{en} {o}→{n}{en_unit}"))

    # 免费内容字段（只比较昨天 snapshot 里存在的字段，避免首次升级误报）
    for key, (zh, en) in CONTENT_FIELDS.items():
        if key not in old_snap:
            continue
        o, n = old_snap.get(key), new.get(key)
        if o == n:
            continue
        out.append((f"{zh} {_disp(key, o)}→{_disp(key, n)}",
                    f"{en} {_disp(key, o)}→{_disp(key, n)}"))

    # 模型池
    if "models" in old_snap:
        o, n = old_snap.get("models") or [], new.get("models") or []
        if set(o) != set(n):
            out.append(("模型池更新", "model lineup updated"))

    # 链接体检 / 数据陈旧
    if "bad_links" in old:
        old_bad = set(old.get("bad_links") or [])
        new_bad = set(entry.get("_bad_links") or [])
        if new_bad - old_bad:
            k = len(new_bad - old_bad)
            out.append((f"🚫 新增死链 {k} 条", f"🚫 {k} new dead link(s)"))
        if old_bad - new_bad:
            k = len(old_bad - new_bad)
            out.append((f"✅ 死链修复 {k} 条", f"✅ {k} dead link(s) fixed"))
    if "stale" in old and bool(old.get("stale")) != bool(entry.get("_stale")):
        out.append(("⚠️ 转为陈旧数据", "⚠️ marked stale") if entry.get("_stale")
                   else ("✅ 陈旧标记解除", "✅ staleness cleared"))

    # 信源数量（核查深度变化）
    for key, zh, en in (("official_sources", "官方信源", "official sources"),
                        ("third_sources", "第三方信源", "third-party sources")):
        if key not in old:
            continue
        field = "official" if key == "official_sources" else "third"
        new_n = len(entry.get("_sources", {}).get(field, []))
        if old.get(key) != new_n:
            out.append((f"{zh} {old.get(key)}→{new_n}", f"{en} {old.get(key)}→{new_n}"))

    return out


def annotate(entries: list, previous: dict) -> list:
    """给每条 entry 挂 `_delta`，返回昨日在榜、今日下线的厂商名列表。"""
    old_offers = (previous or {}).get("offers") or {}
    ids = {e["id"] for e in entries}
    for e in entries:
        e["_delta"] = changes(e, old_offers.get(e["id"]))
    return [old_offers[k].get("provider") or k for k in old_offers if k not in ids]
