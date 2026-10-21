# 贡献指南：怎么补一条免费额度

直接编辑 `data/offers.yml`，每条 offer 一个 YAML 项。**描述尽可能带官方控制台链接 + 一手截图/文档页**，机器人每周复核探活。

## 模板

```yaml
  - id: <kebab-case-唯一id>            # 如 moonshot-kim
    provider: <品牌显示名>
    website: <控制台入口 URL>
    docs: <限额/定价文档 URL>
    region: 中国大陆可直连 | 全球(需梯子) | 全球
    signup: <用 1-2 句话讲清注册步骤>
    models:
      - 模型A
      - 模型B
    offer:
      type: 免费层 | 试用金 | 签到积分 | 一次性赠送 | 限时活动
      requests_day: 1000            # 可选
      tokens_day: 200000            # 可选
      tokens_month: 1000000000      # 可选
      credits_usd: 5                # 可选（一次性赠金）
      credits_cny: 18               # 可选（人民币券）
      signup_tokens: 20000000       # 可选（注册送 token）
      checkin_tokens_day: 100       # 可选（每日签到）
      points_monthly: 500           # 可选（积分制）
      points_daily: 100             # 可选
      valid_months: 1               # 试用金摊销月数
      expiry: null                  # 或 "2026-12-31"
    restrictions: <并发/商用/实名/网络等限制>
    est_usd_per_mtok: 0.30          # 折算用的官方付费价
    value_override_usd: null        # 特殊公价时人工指定
    verified: YYYY-MM-DD
    confidence: high | medium | low
    notes: <可选的上下文，比如旧政策何时改>
```

## 估值口径

- 折算月价值 = 白嫖 tokens 量 × `est_usd_per_mtok`（填官方付费价）；
- 一次性赠送金：`valid_months` 摊销（默认 1 月，永久额度用 notes 说明）；
- 签到积分制：`checkin_tokens_day × 30`；纯积分制（单位非 tokens）估值为 0 并解释。

## 信源要求

- **high（✅双源）**：官方文档 + 任一第三方佐证；
- **medium（☑️单源）**：仅官方可查；
- **low（⚠️待核）**：口述/未验证，标注需要补什么。

## 冲突怎么办

如果你发现表格里某行已过期（比如 Cerebras 的 Free Trial 政策），直接改 `data/offers.yml` 对应字段 + 更新 `verified`，PR 标题写 `[update] <id>`。
