# 全球大模型厂商「免费 Token / 免费额度 / 签到积分」白皮书

> 一个**开源、每周自动核查**的数据库：扫描全球大模型厂商（国内 + 海外）官方渠道里能白嫖的 API 额度——免费层、注册赠送金、每日签到积分、限时活动；标注模型、折算月价值、注册方法、限制条件、有效期。**PR 欢迎补充新厂商 / 更正数字。**

## 🏆 免费 Token 排行（折算月价值）

<!-- AUTO-TABLE-START -->
_2026-10-21 自动重建 · 数据定义于 [`data/offers.yml`](data/offers.yml)_

| # | 厂商 | 类型 | 免费内容（模型） | 折算月价值 | 注册方式 | 限制条件 | 有效期 | 信号 |
|---|---|---|---|---|---|---|---|---|
| 1 | [智谱 AI BigModel](https://open.bigmodel.cn) | 一次性赠送 | 💪 一次性赠送：注册赠 20,000,000 tokens｜模型：glm-4-flash-250414(永久免费), glm-4.7-flash, glm-4-air, glm-4.6+ 全家 | **$22.00/月** | 手机号注册；实名后完整额度 | 免费模型系列并发 1；邀请要求新用户实名注册起跑 | 长期有效 | ✅双源 |
| 2 | [Mistral La Plateforme](https://console.mistral.ai) | 免费层 | 🆓 免费层：1,000,000,000 tokens/月｜模型：mistral-large, mistral-medium, codestral, mistral-small, pixtral(视模型池为准) | **$15.00/月** | 邮箱/Google 注册即可申请 Experiment（免费）层 API Key；是否需绑手机号以控制台为准 | 限速严格（约 1 req/s），月吞吐上限按平台平均用量池化计；不能用于生产 SLA | 长期有效 | ☑️单源 |
| 3 | [Cerebras](https://cloud.cerebras.ai) | 试用金 | 🎁 试用金：1,000,000 tokens/日 + $5 赠金｜模型：Llama 4 Scout/Qwen3 + 试用金可开全量模型 | **$10.50/月** | 邮箱注册 cloud.cerebras.ai → 取 API Key | 试用层 5 RPM / 30K TPM / 1M tokens per hour&day；$5 一次性credits | 长期有效 | ✅双源 |
| 4 | [硅基流动 SiliconFlow](https://cloud.siliconflow.cn) | 一次性赠送 | 💪 一次性赠送：¥18 券｜模型：Qwen 系列 / DeepSeek 蒸馏 / GLM 等国产开源全量 200+ 模型 | **$2.50/月** | 手机号注册 + 注册送额度（当前口径：实名认证后送 ¥18 通用券） | 以人民币券结算；部分模型强制实名 | 长期有效 | ✅双源 |
| 5 | [Groq](https://console.groq.com) | 免费层 | 🆓 免费层：1,000 请求/日 + 200,000 tokens/日｜模型：openai/gpt-oss-120b, openai/gpt-oss-20b, qwen/qwen3.6-27b, qwen/qwen3.8-27b, moonshotai/k… | **$1.80/月** | 邮箱或 GitHub/Google OAuth 注册 → console.groq.com/keys 取 API Key | 组织级限速（多 key 不叠加）；200K tokens/天为主力阵容；部分模型 TPD 500K | 长期有效 | ✅双源 |
| 6 | [OpenRouter](https://openrouter.ai) | 免费层 | 🆓 免费层：50 请求/日｜模型：19+ 个 :free 后缀文本模型(含 deepseek/qwen/llama 等) + openrouter/free 路由 | —（限速内自由） | 邮箱注册即取 API Key；无需信用卡 | :free 模型 20 RPM / 50 RPD；充值满 $10（历史累计）解锁 1000 RPD；按请求计不限 tokens | 长期有效 | ✅双源 |
| 7 | [Google AI Studio / Gemini API](https://aistudio.google.com) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：gemini-3.8-flash, gemini-3.6-flash, gemini-2.5 系列(免费层口径官方动态调整) | —（限速内自由） | Google 账号登录 AI Studio → Get API key；免费层无需绑卡 | 免费层 RPM 不断下调中（高峰会 429）；部分高级模型(Pro/图像)免费层不可用 | 长期有效 | ✅双源 |
| 8 | [Gemini CLI（终端 agent 客户端）](https://github.com/google-gemini/gemini-cli) | 免费层 | 🆓 免费层：250 请求/日｜模型：gemini-3.8-flash, gemini-3.6-flash（免费层可用阵容动态调整） | —（限速内自由） | Google 账号登录即可，免费层无需绑卡 | 免费层限速较低（高峰 429）；模型阵容与限额动态调整；与 AI Studio 免费层共享池 | 长期有效 | ✅双源 |
| 9 | [腾讯混元 Lite](https://lke.cloud.tencent.com/lke/#/hybrid/home) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：hunyuan-lite（永久免费）, hunyuan-turbos(付费) 等 | —（限速内自由） | 腾讯云账号 → 开通混元 → 用 hunyuan-lite 免费模型 | 并发限制以腾讯云文档为准；lite 系列限速免费 | 长期有效 | ☑️单源 |
| 10 | [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：Llama 3.x / Qwen2.5 / Mistral 7B / SDXL 图像等 | —（限速内自由） | Cloudflare 账号 → Workers AI 直接绑定，或 REST API | 按 neuron 计费；免费 10,000 neurons/天（tokens 数随模型而定） | 长期有效 | ☑️单源 |
| 11 | [火山引擎豆包大模型](https://www.volcengine.com/product/doubao) | 一次性赠送 | 💪 一次性赠送：注册赠 490,000 tokens｜模型：doubao-seed 全线（每个模型赠 49 万 tokens 试用期，以控制台为准） | —（限速内自由） | 手机号注册 → 控制台为每个模型开通 → 赠送试用 tokens | 按模型独立赠送；开通即赠；具体额度以官网控制台校准 | 长期有效 | ☑️单源 |
| 12 | [Qwen Code CLI（终端 agent 客户端）](https://github.com/QwenLM/qwen-code) | 免费层 | 🆓 免费层：2,000 请求/日｜模型：qwen3-coder 系列（OAuth 免费池） | —（限速内自由） | npm 装 @qwen-code/qwen-code → 启动选 qwen-oauth 设备码登录，无需绑卡 | OAuth 免费池限额以官方 docs 实时口径为准；付费 DashScope Key 可再解锁 | 长期有效 | ☑️单源 |
| 13 | [GitHub Copilot Free（IDE/网页 agent 客户端）](https://github.com/features/copilot) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：官方指定的有限模型池（免费层阵容由 GitHub 单方面调整） | —（限速内自由） | GitHub 账号一键开通；认证学生可白嫖 Copilot Student | limited access：补全 + 有限聊天/配额；企业账号禁用；详细数字以 plans 页为准 | 长期有效 | ☑️单源 |
| 14 | [OpenCode Zen（agent 客户端模型网关）](https://opencode.ai/zen) | 其他（非免费） | ℹ️ 其他（非免费）：限速免费（量级未公布）｜模型：GLM/Kimi/Qwen 等精选池（官方统一基准测试） | —（限速内自由） | opencode 客户端配 Zen endpoint，$20 起充 | 无免费层、无注册赠送；卖点为『零加成单价 + 挑过模型的网关』，与 OpenRouter :free 组合可白嫖 | 长期有效 | ☑️单源 |
| 15 | [Kilo Code（IDE/CLI agent 客户端）](https://kilocode.ai) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：500+ 模型零加成；免费模型池（Auto Free 自动路由） | —（限速内自由） | GitHub/邮箱注册 app.kilo.ai → 装 VS Code 插件或 CLI | 免费池额度与模型动态调整；限时活动以站内公告为准；企业版有 Cursor 迁移优惠（非白嫖主线） | 长期有效 | ☑️单源 |
| 16 | **WorkBuddy（示例条目 — 由需求方提供，待核）** | 签到积分 | ✅ 签到积分：积分 500/月 + 100/日｜模型：待核 | —（限速内自由） ⚠️待核 | 见官网（待补） | 待核 | 长期有效 | ⚠️待核 |
| 17 | [阿里云百炼 DashScope](https://bailian.console.aliyun.com) | 一次性赠送 | 💪 一次性赠送：限速免费（量级未公布）｜模型：qwen 系列（各模型免费额度不同） | —（限速内自由） ⚠️待核 | 阿里云账号开通百炼 → 新用户按模型层获得免费试用额度（qwen-turbo 等百万级 tokens；时有时效） | 额度有有效期；具体以控制台展示为准 | 长期有效 | ⚠️待核 |
| 18 | [Hugging Face Inference Providers](https://huggingface.co/inference-providers) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：hf 推理路由全模型（groq/together 等多家后端） | —（限速内自由） ⚠️待核 | HF 账号自带少量月度 free credits（登录即有）；PRO 账号额度更高 | 免费账户 credits 量极小，主要用于试玩；具体钱数官方动态调整 | 长期有效 | ⚠️待核 |
<!-- AUTO-TABLE-END -->

## 免费内容怎么读

- **免费层（Rate-limited free tier）**：永久免费但限速（RPM/TPD/TPM），适合原型和小项目。
- **试用金（Trial credits）**：注册/实名/绑卡送一次性美元额度，按月摊销后对比。
- **签到积分（Check-in）**：每日打卡送积分或 tokens（例如某平台「每月 500 积分 + 每日签到 100 积分」），机器人按 ×30 折算月价值。
- **限时活动（Promo）**：有明确 deadline 的活动，过期前排最前。
- **折算月价值 = 理论可白嫖 tokens × 官方付费价**，标 `—` 表示不限量限速型（价值取决于你的调用密度），标 `⚠️ 待核` 表示信源单一。

## 数据字段（PR 模板见 CONTRIBUTING.md）

| 字段 | 说明 |
|---|---|
| `provider / website / docs` | 厂商名、控制台入口、限额文档 |
| `offer.type` | 免费层 / 试用金 / 签到积分 / 限时活动 |
| `offer.models` | 覆盖模型 |
| `offer.requests_day / tokens_day / tokens_month` | 量级上限 |
| `offer.credits_usd / valid_months` | 一次性金额与摊销 |
| `offer.checkin_tokens_day / checkin_points` | 签到类 |
| `offer.expiry` | 有效期 |
| `restrictions` | 限制条件（并发/商用/实名/网络） |
| `signup` | 注册方法和手段 |
| `verified / confidence` | 最后人工核查日 + 信号强度 |

## 🍋 检索中有意思的发现（人工精选，随扫描更新）

- **Qwen Code CLI 是 agent 客户端里最大方的**：`qwen-oauth` 免费池长期给 **2000 请求/天上限级别**的额度（Gemini CLI 只给 250/日），白嫖终端 agent 首选 Qwen。
- **OpenRouter 的隐藏加速器**：`:free` 模型默认 50 请求/天，但**历史累计充值满 $10（不要求消耗）就永久升到 1000 请求/天**——充 $10 相当于买了张长期饭票。
- **Cerebras 是政策多变教材**：2026-07-21 把“每日 100 万 tokens 永久免费”改成了 **$5 一次性试用金**。这类“免费层随时变试用金”是常态，盯 `verified` 日期比盯排名第一更靠谱。
- **智谱的邀请制经济学**：GLM-4.x-Flash 系**永久免费（并发 1）**已是大礼，但更狠的是邀请制——**每月最多邀 10 个新用户 = 每月最高 2 亿免费 tokens**，按付费价折算约 $22/月。
- **Google 除 Flash 免费外还有暗器**：**Google Search grounding 每月 5000 次免费**（带实时搜索的 RAG），做小时效敏感应用比纯模型免费值钱。
- **Groq 送了个免费的 agentic 模型**：`groq/compound`（会自己调工具的混合模型）在免费层也有 250 请求/天，做 agent demo 零成本。
- **活动下线史值得收藏**：硅基流动“注册送 2000 万 tokens”早已下线，改为实名送 ¥18 通用券；此类“羊毛速朽”提醒我们：看到粥要趁热。

## 自动扫描机制（每周一 10:00 北京时间）

1. `data/offers.yml` 里的每条记录，机器人会：
   - **探活**：访问 `website` 和 `docs` 链接，404/超时的条目会被打上 🚫 标记并开 issue；
   - **新鲜度**：`verified` 超过 45 天未人工复核的条目会标 ⚠️；
   - **折算**：用 `valuecalc.py` 统一换算成「USD/月」重新排序，重建 README 表格 + 生成 `reports/` 周报快照。
2. 数据任何人工变更都会在 git diff 里留下审计痕迹。

## ⚠️ 免责声明

- 一切以**各厂商控制台/定价页为准**，本仓库数据为参考快照，可能滞后 1 周以上；
- 免费额度政策变动频繁（Groq 2026-09 阵容精简、Cerebras 2026-07 取消永久免费层），请以 `verified` 日期自行判断新旧；
- 本仓库与任何厂商无利益关系，排名不含返利链接。

## Roadmap
- [ ] 各厂商页面自动 diff（不只探活，抓正文变化提醒）
- [ ] 每周 issue 自动 @ 上一期挂掉条目的提交者复核
- [ ] 接入社区提交模板（表单式）
