# 全球大模型厂商「免费 Token / 免费额度 / 签到积分」白皮书

> 一个**开源、每日自动核查**的数据库：扫描全球大模型厂商（国内 + 海外）官方渠道里能白嫖的 API 额度——免费层、注册赠送金、每日签到积分、限时活动；标注模型、**持续/一次性双轨价值**、注册方法、限制条件、有效期。**PR 欢迎补充新厂商 / 更正数字。**

**Language / 语言切换：[中文](README.md)（本页） · [English](README_EN.md)**

## 🏆 免费 Token 排行（折算月价值）

<!-- AUTO-TABLE-START -->
_2026-10-21 自动重建 · 数据定义于 [`data/offers.yml`](data/offers.yml)_

| # | 厂商 | 类型 | 免费内容（模型） | 持续价值(USD/月) | 一次性价值(USD) | 注册方式 | 限制条件 | 有效期 | 官方验证 | 第三方验证 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [腾讯 WorkBuddy（AI Agent 办公台）](https://www.workbuddy.ai) | 签到积分 | ✅ 签到积分：注册赠 2,000 点 + 500 积分/月 + 签到 100 点/日｜模型：Kimi-K3, GLM-5.3, DeepSeek-V4.1-Flash, Hy4（限时免费） | $**105/月**<br>_(500 月包+100×30 签到) × $0.03/点 · 注册赠 2,000 点 × $0.03/点_ | $**60** | 官网/App（含 Microsoft Store）/国内版 workbuddy.cn 注册；部分活动需从邀请链接进入 | 积分为统一用量单位，不同模型消耗不同；纯月包 500 积分重度使用 2-3 天烧完；社区发文/任务可再挣积分（zdm 称月合计 6000+） | 长期有效 | ✅ [www.workbuddy.ai](https://www.workbuddy.ai/docs/zh/workbuddy/credits)<br>✅ [www.workbuddy.ai](https://www.workbuddy.ai/docs/zh/workbuddy/pricing)<br>✅ [apps.microsoft.com](https://apps.microsoft.com/detail/xpfg2p1xdmx1x0) | 📄 [cloud.tencent.com](https://cloud.tencent.com/developer/article/2712113)<br>📄 [post.m.smzdm.com](https://post.m.smzdm.com/p/a0300z28/)<br>📄 [github.com](https://github.com/88lin/workbuddy-auto-signin) |
| 2 | [Modal](https://modal.com) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：自托管任意开源模型（BYO image，如 vLLM） | $**30/月**<br>_人工指定_ | — | GitHub/Google 一键注册，Starter 档自动享每月 $30 算力金 | $30/月按秒计费，月底清零不结转；无月费、无需信用卡 | 长期有效 | ✅ [modal.com](https://modal.com/pricing) | —（本会话未直接读到第三方源） |
| 3 | [智谱 AI BigModel](https://open.bigmodel.cn) | 一次性赠送 | 💪 一次性赠送：注册赠 200,000,000 tokens/月 + 注册赠 20,000,000 tokens｜模型：glm-4-flash-250414(永久免费), glm-4.7-flash, glm-4-air, glm-4.6+ 全家 | $**22/月**<br>_人工指定 · 注册赠 20,000,000 tokens × $0.11/1M_ | $**2.2** | 手机号注册；实名后完整额度 | 免费模型系列并发 1；邀请要求新用户实名注册起跑 | 长期有效 | ✅ [bigmodel.cn](https://bigmodel.cn/dev/activities/free/glm-4-flash)<br>✅ [docs.bigmodel.cn](https://docs.bigmodel.cn/cn/update/promotion) | 📄 [www.cnblogs.com](https://www.cnblogs.com/justin-Y/p/20078212)<br>📄 [cloud.tencent.com](https://cloud.tencent.com/developer/article/2638288) |
| 4 | [Mistral La Plateforme](https://console.mistral.ai) | 免费层 | 🆓 免费层：1,000,000,000 tokens/月｜模型：mistral-large, mistral-medium, codestral, mistral-small, pixtral(视模型池为准) | $**15/月**<br>_人工指定_ | — | 邮箱/Google 注册即可申请 Experiment（免费）层 API Key；是否需绑手机号以控制台为准 | 限速严格（约 1 req/s），月吞吐上限按平台平均用量池化计；不能用于生产 SLA | 长期有效 | ✅ [mistral.ai](https://mistral.ai/pricing/)<br>✅ [docs.mistral.ai](https://docs.mistral.ai/admin/billing-usage/usage-limits) | 📄 [pricepertoken.com](https://pricepertoken.com/endpoints/mistral/free)<br>📄 [www.reddit.com](https://www.reddit.com/r/MistralAI/comments/1rc8rwf/mistral_api_quota_and_rate_limits_pools_analysis/) |
| 5 | [Cerebras](https://cloud.cerebras.ai) | 试用金 | 🎁 试用金：1,000,000 tokens/日 + $5 赠金｜模型：Llama 4 Scout/Qwen3 + 试用金可开全量模型 | $**10.5/月**<br>_1,000,000 tokens/日 × 30 × $0.35/1M · $5 一次性（摊 1 月）_ 🔒 | $**5** | 邮箱注册 cloud.cerebras.ai → 取 API Key | 试用层 5 RPM / 30K TPM / 1M tokens per hour&day；$5 一次性credits | 长期有效 | ✅ [inference-docs.cerebras.ai](https://inference-docs.cerebras.ai/support/rate-limits)<br>✅ [www.cerebras.ai](https://www.cerebras.ai/pricing) | 📄 [pricepertoken.com](https://pricepertoken.com/endpoints/cerebras/free)<br>📄 [www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1mfeazc/cerebras_pro_coder_deceptive_limits/) |
| 6 | [Groq](https://console.groq.com) | 免费层 | 🆓 免费层：1,000 请求/日 + 200,000 tokens/日｜模型：openai/gpt-oss-120b, openai/gpt-oss-20b, qwen/qwen3.6-27b, qwen/qwen3.8-27b, moonshotai/k… | $**1.8/月**<br>_200,000 tokens/日 × 30 × $0.3/1M_ 🔒 | — | 邮箱或 GitHub/Google OAuth 注册 → console.groq.com/keys 取 API Key | 组织级限速（多 key 不叠加）；200K tokens/天为主力阵容；部分模型 TPD 500K | 长期有效 | ✅ [console.groq.com](https://console.groq.com/docs/rate-limits) | 📄 [klymentiev.com](https://klymentiev.com/articles/groq-api-free-tier-limits-2026)<br>📄 [www.grizzlypeaksoftware.com](https://www.grizzlypeaksoftware.com/articles/p/groq-api-free-tier-limits-in-2026-what-you-actually-get-uwysd6mb) |
| 7 | [iFLYTEK Spark (讯飞星火)](https://www.xfyun.cn/doc/spark/HTTP调用文档.html) | 一次性赠送 | 💪 一次性赠送：注册赠 2,000,000 tokens｜模型：spark-v3.0, spark-lite(活动标价体系内) | $**0.69/月**<br>_注册 2,000,000 tokens 摊 12 月 × $4.17/1M_ 🚫 | — | console.xfyun.cn 注册 → 活动页 0 元下单领取免费包 | 仅个人免费包 QPS=2；企业包 500万 tokens/1 年；到期时间未公示 | 长期有效 | ✅ [www.xfyun.cn](https://www.xfyun.cn/activities/discount) | —（本会话未直接读到第三方源） |
| 8 | [SCNet National Supercomputing (国家超算互联网)](https://www.scnet.cn/) | 一次性赠送 | 💪 一次性赠送：注册赠 10,000,000 tokens｜模型：DeepSeek-R1, Qwen3, MiniMax-M2.5 | $**0.28/月**<br>_注册 10,000,000 tokens 摊 0.5 月 × $0.014/1M_ | — | 注册后在活动页一键领取 | 限时活动（媒体口径 2 周）；3000万 tokens 档活动以领取页实时为准 | 长期有效 | ✅ [www.scnet.cn](https://www.scnet.cn/home/subject/hxjd/index.html) | —（本会话未直接读到第三方源） |
| 9 | [Scaleway Generative APIs](https://console.scaleway.com) | 免费层 | 🆓 免费层：1,000,000 tokens/月｜模型：qwen3.5-397b-a17b, mistral-small-3.2-24b | $**0.18/月**<br>_1,000,000 tokens/月 × $0.18/1M_ 🔒 | — | 注册建项目即享 Free Tier；OpenAI 兼容 endpoint | 1M 免费额度优先抵扣最贵 token；官方未确认是否每月重置，保守按一次性/月度首冲 | 长期有效 | ✅ [www.scaleway.com](https://www.scaleway.com/en/docs/generative-apis/faq/) | —（本会话未直接读到第三方源） |
| 10 | [Baidu Qianfan ModelBuilder (百度千帆)](https://cloud.baidu.com/product/qianfan.html) | 一次性赠送 | 💪 一次性赠送：注册赠 1,000,000 tokens｜模型：ERNIE-4.5-Turbo-128K, ERNIE-X1-Turbo-32K, DeepSeek-R1, DeepSeek-V3.1-250821, Kimi-K2-Inst… | $**0.04/月**<br>_注册 1,000,000 tokens 摊 3 月 × $0.11/1M_ | — | 访问千帆平台同意协议，系统自动发放新用户额度 | 17 个预置模型各 100 万 tokens 独立配额；仅抵扣在线推理 | 长期有效 | ✅ [cloud.baidu.com](https://cloud.baidu.com/doc/qianfan/s/Imi2rpirg)<br>✅ [cloud.baidu.com](https://cloud.baidu.com/product/qianfan.html) | —（本会话未直接读到第三方源） |
| 11 | [OVHcloud AI Endpoints](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/) | 一次性赠送 | 💪 一次性赠送：$200 赠金｜模型：gpt-oss-120b, qwen3.5, stable-diffusion-xl(免费), qwen3guard-8b(免费), nvidia-riva-tts(免费) | —<br>_$200 一次性（摊 1 月）_ | $**200** | 注册建首个 Public Cloud project 激活试用 token | $200 免费额度 1 个月；需绑卡且限每法人一张；SDXL/Riva/Qwen3Guard 长期免费模型 | 长期有效 | ✅ [www.ovhcloud.com](https://www.ovhcloud.com/en/public-cloud/free-ai-api) | —（本会话未直接读到第三方源） |
| 12 | [Baseten](https://app.baseten.co) | 试用金 | 🎁 试用金：$30 赠金｜模型：gpt-oss-120b, deepseek-v4-flash, glm-5.3-flash, kimi-k3 | —<br>_$30 一次性（摊 1 月）_ | $**30** | 注册新 workspace 自动入账起赠 credits | 一次性起赠金；用尽且无支付方式则模型停用 | 长期有效 | ✅ [www.baseten.co](https://www.baseten.co/resources/changelog/usage-based-pricing-with-free-credits)<br>✅ [docs.baseten.co](https://docs.baseten.co/organization/billing) | —（本会话未直接读到第三方源） |
| 13 | [Exa AI](https://dashboard.exa.ai) | 试用金 | 🎁 试用金：$20 赠金｜模型：exa-search, exa-deep-search, exa-answer, exa-agent | —<br>_$20 一次性（摊 1 月）_ 🚫 | $**20** | 注册即得 $10；完成 onboarding 首个 team 再奖 $10 | Free Tier 每月 1 号重置 $10（持续性）；$20 为一次性合计；无需绑卡 | 长期有效 | ✅ [exa.ai](https://exa.ai/docs/reference/pricing) | —（本会话未直接读到第三方源） |
| 14 | [Nscale](https://console.nscale.com) | 试用金 | 🎁 试用金：$5 赠金｜模型：llama-3.3-70b-instruct, qwen3-coder, deepseek-r1 | —<br>_$5 一次性（摊 1 月）_ | $**5** | console.nscale.com Google 登录后 Claim $5 free credit | 用完即止，未绑卡不可续 | 长期有效 | ✅ [www.nscale.com](https://www.nscale.com/blog/introducing-nscale-serverless-inference-scalable-ai-without-infrastructure-hassles) | —（本会话未直接读到第三方源） |
| 15 | [硅基流动 SiliconFlow](https://cloud.siliconflow.cn) | 一次性赠送 | 💪 一次性赠送：¥18 券｜模型：Qwen 系列 / DeepSeek 蒸馏 / GLM 等国产开源全量 200+ 模型 | —<br>_¥18 ≈ $2.50 一次性_ | $**2.5** | 手机号注册 + 注册送额度（当前口径：实名认证后送 ¥18 通用券） | 以人民币券结算；部分模型强制实名 | 长期有效 | ✅ [www.siliconflow.com](https://www.siliconflow.com/zh/pricing)<br>✅ [www.siliconflow.cn](https://www.siliconflow.cn/developer-talk/od7wj9rr23p95uhihmhrombp) | 📄 [www.beizigen.com](https://www.beizigen.com/post/siliconflow-invitation-code/)<br>📄 [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/712780071) |
| 16 | [MiniMax Open Platform (稀宇科技)](https://platform.minimaxi.com/) | 试用金 | 🎁 试用金：¥15 券｜模型：MiniMax-M3, MiniMax-M3.1-Flash, Speech-2.8-HD | —<br>_¥15 ≈ $2.08 一次性_ | $**2.08** ⚠️ | 注册并完成实名认证 | 注册赠金未在官方页面公示，数值为多第三方源交叉；用完即停 | 长期有效 | ✅ [platform.minimaxi.com](https://platform.minimaxi.com/) | —（本会话未直接读到第三方源） |
| 17 | [Moonshot Kimi Open Platform (月之暗面)](https://platform.kimi.com/) | 一次性赠送 | 💪 一次性赠送：¥15 券｜模型：kimi-k3, kimi-k2.5, kimi-k2 | —<br>_¥15 ≈ $2.08 一次性_ | $**2.08** | 国内手机号注册开放平台并实名，代金券自动发放抵扣 | 仅国内新用户实名发放；不可用于 Kimi K3（需充值解锁）；用尽自动停 | 长期有效 | ✅ [www.kimi.com](https://www.kimi.com/help/kimi-api/api-free-trial) | —（本会话未直接读到第三方源） |
| 18 | [Fireworks AI](https://fireworks.ai) | 试用金 | 🎁 试用金：$1 赠金｜模型：kimi-k3, glm-5.3, deepseek-v4.1-flash | —<br>_$1 一次性（摊 1 月）_ | $**1** | Get Started 注册，新账户自动入账 $1 起始 credits | 无绑卡时全账户 10 RPM；$1 用完且未绑卡即停 | 长期有效 | ✅ [fireworks.ai](https://fireworks.ai/pricing)<br>✅ [docs.fireworks.ai](https://docs.fireworks.ai/faq-new/billing-pricing) | —（本会话未直接读到第三方源） |
| 19 | [Hyperbolic](https://app.hyperbolic.ai) | 试用金 | 🎁 试用金：$1 赠金｜模型：meta-llama/Llama-3.3-70B, deepseek-v3, qwen3-235b | —<br>_$1 一次性（摊 1 月）_ 🚫 | $**1** | 注册（Google/GitHub/邮箱）即获推理试用金 | Basic 免费层 60 RPM；$5+ 充值解锁 Pro 600 RPM | 长期有效 | ✅ [www.hyperbolic.xyz](https://www.hyperbolic.xyz/pricing) | —（本会话未直接读到第三方源） |
| 20 | [Xiaomi MiMo Open Platform (小米)](https://mimo.mi.com/) | 一次性赠送 | 💪 一次性赠送：¥5 券｜模型：MiMo-V2.6, MiMo-V2.5-ASR, MiMo-V2.5-TTS | —<br>_¥5 ≈ $0.69 一次性_ | $**0.69** | 注册并在个人中心完成首笔实名认证，¥5 赠金即时到账 | 赠金 40 天有效、仅抵扣 API 费用；受邀邀请双方各再得 ¥10 | 长期有效 | ✅ [mimo.mi.com](https://mimo.mi.com/docs/zh-CN/quick-start/promotions/new%20user) | —（本会话未直接读到第三方源） |
| 21 | [Novita AI](https://novita.ai) | 试用金 | 🎁 试用金：$0.5 赠金｜模型：deepseek-v4-flash, llama-3.1-8b-instruct, qwen2.5-7b-instruct, glm-4-9b-0414 | —<br>_$0.5 一次性（摊 12 月）_ | $**0.5** | 注册即得小额 voucher | 注册 voucher 金额官方未公布（第三方口径 ~$0.5/1年）；referral 双向各 $10 | 长期有效 | ✅ [docs.novita.ai](https://docs.novita.ai/guides/sandbox-pricing) | —（本会话未直接读到第三方源） |
| 22 | [腾讯混元 Lite](https://lke.cloud.tencent.com/lke/#/hybrid/home) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：hunyuan-lite（永久免费）, hunyuan-turbos(付费) 等 | — | — | 腾讯云账号 → 开通混元 → 用 hunyuan-lite 免费模型 | 并发限制以腾讯云文档为准；lite 系列限速免费 | 长期有效 | ✅ [cloud.tencent.com](https://cloud.tencent.com/document/product/1729) | 📄 [www.cnblogs.com](https://www.cnblogs.com/justin-Y/p/20078212) |
| 23 | [Qoder（阿里，国际版 AI IDE）](https://qoder.com) | 签到积分 | ✅ 签到积分：领 100 credits/日｜模型：Qwen 系列专属池, SOTA 模型（活动期轮换） | — | — | 官网下载桌面端（国际版）→ 邮箱注册；免费体验版即可参与活动 | 每日额度需当天手动领取、不累计至次日；免费及个人付费用户均可领；Credit 换算美元未公示 | 长期有效 | ✅ [docs.qoder.com](https://docs.qoder.com/zh/events/100credits)<br>✅ [docs.qoder.com](https://docs.qoder.com/zh/account/pricing)<br>✅ [docs.qoder.com](https://docs.qoder.com/zh/events/sotafree)<br>✅ [forum.qoder.com](https://forum.qoder.com/t/qoder/6368) | 📄 [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/2058865181518717227) |
| 24 | [Trae（字节，AI IDE）](https://www.trae.ai) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：Claude / GPT / Gemini / DeepSeek 池（IDE 内可切） | — | — | GitHub/Google/邮箱注册 IDE 即用 | 按 token 折算 Dollar Usage 月度赠送，免费档排队优先级低（高峰等待）；商用受限；具体赠送金额以控制台展示 | 长期有效 | ✅ [www.trae.ai](https://www.trae.ai/pricing)<br>✅ [www.trae.ai](https://www.trae.ai/blog/trae_membership_0213)<br>✅ [docs.trae.ai](https://docs.trae.ai/ide/new-plans-and-billing) | 📄 [www.reddit.com](https://www.reddit.com/r/TraeIDE/comments/1laiiez/traeai_ide_free_vs_prosubscription/)<br>📄 [resourify.com](https://resourify.com/resources/trae) |
| 25 | [OpenRouter](https://openrouter.ai) | 免费层 | 🆓 免费层：50 请求/日｜模型：19+ 个 :free 后缀文本模型(含 deepseek/qwen/llama 等) + openrouter/free 路由 | — | — | 邮箱注册即取 API Key；无需信用卡 | :free 模型 20 RPM / 50 RPD；充值满 $10（历史累计）解锁 1000 RPD；按请求计不限 tokens | 长期有效 | ✅ [openrouter.ai](https://openrouter.ai/docs/api_reference/limits)<br>✅ [openrouter.ai](https://openrouter.ai/pricing)<br>✅ [openrouter.ai](https://openrouter.ai/docs/faq) | —（本会话未直接读到第三方源） |
| 26 | [Google AI Studio / Gemini API](https://aistudio.google.com) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：gemini-3.8-flash, gemini-3.6-flash, gemini-2.5 系列(免费层口径官方动态调整) | — | — | Google 账号登录 AI Studio → Get API key；免费层无需绑卡 | 免费层 RPM 不断下调中（高峰会 429）；部分高级模型(Pro/图像)免费层不可用 | 长期有效 | ✅ [ai.google.dev](https://ai.google.dev/gemini-api/docs/rate-limits)<br>✅ [ai.google.dev](https://ai.google.dev/gemini-api/docs/pricing) | —（本会话未直接读到第三方源） |
| 27 | [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：Llama 3.x / Qwen2.5 / Mistral 7B / SDXL 图像等 | — | — | Cloudflare 账号 → Workers AI 直接绑定，或 REST API | 按 neuron 计费；免费 10,000 neurons/天（tokens 数随模型而定） | 长期有效 | ✅ [developers.cloudflare.com](https://developers.cloudflare.com/workers-ai/platform/pricing/) | —（本会话未直接读到第三方源） |
| 28 | [火山引擎豆包大模型](https://www.volcengine.com/product/doubao) | 一次性赠送 | 💪 一次性赠送：注册赠 490,000 tokens｜模型：doubao-seed 全线（每个模型赠 49 万 tokens 试用期，以控制台为准） | — | — | 手机号注册 → 控制台为每个模型开通 → 赠送试用 tokens | 按模型独立赠送；开通即赠；具体额度以官网控制台校准 | 长期有效 | ✅ [www.volcengine.com](https://www.volcengine.com/docs/82379) | —（本会话未直接读到第三方源） |
| 29 | [阿里云百炼 DashScope](https://bailian.console.aliyun.com) | 一次性赠送 | 💪 一次性赠送：一次性赠送｜模型：qwen 系列（各模型免费额度不同） | — | — ⚠️ | 阿里云账号开通百炼 → 新用户按模型层获得免费试用额度（qwen-turbo 等百万级 tokens；时有时效） | 额度有有效期；具体以控制台展示为准 | 长期有效 | ✅ [help.aliyun.com](https://help.aliyun.com/zh/model-studio/getting-started/models) | —（本会话未直接读到第三方源） |
| 30 | [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：hf 推理路由全模型（groq/together 等多家后端） | — | — ⚠️ | HF 账号自带少量月度 free credits（登录即有）；PRO 账号额度更高 | 免费账户 credits 量极小，主要用于试玩；具体钱数官方动态调整 | 长期有效 | ✅ [huggingface.co](https://huggingface.co/docs/inference-providers)<br>✅ [huggingface.co](https://huggingface.co/docs/inference-providers/pricing) | —（本会话未直接读到第三方源） |
| 31 | [Gemini CLI（终端 agent 客户端）](https://github.com/google-gemini/gemini-cli) | 免费层 | 🆓 免费层：250 请求/日｜模型：gemini-3.8-flash, gemini-3.6-flash（免费层可用阵容动态调整） | — | — | Google 账号登录即可，免费层无需绑卡 | 免费层限速较低（高峰 429）；模型阵容与限额动态调整；与 AI Studio 免费层共享池 | 长期有效 | ✅ [ai.google.dev](https://ai.google.dev/gemini-api/docs/rate-limits) | —（本会话未直接读到第三方源） |
| 32 | [Qwen Code CLI（终端 agent 客户端）](https://github.com/QwenLM/qwen-code) | 免费层 | 🆓 免费层：2,000 请求/日｜模型：qwen3-coder 系列（OAuth 免费池） | — | — | npm 装 @qwen-code/qwen-code → 启动选 qwen-oauth 设备码登录，无需绑卡 | OAuth 免费池限额以官方 docs 实时口径为准；付费 DashScope Key 可再解锁 | 长期有效 | ✅ [qwenlm.github.io](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/)<br>✅ [github.com](https://github.com/QwenLM/qwen-code) | —（本会话未直接读到第三方源） |
| 33 | [GitHub Copilot Free（IDE/网页 agent 客户端）](https://github.com/features/copilot) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：官方指定的有限模型池（免费层阵容由 GitHub 单方面调整） | — | — | GitHub 账号一键开通；认证学生可白嫖 Copilot Student | limited access：补全 + 有限聊天/配额；企业账号禁用；详细数字以 plans 页为准 | 长期有效 | ✅ [docs.github.com](https://docs.github.com/en/copilot/get-started/plans) | —（本会话未直接读到第三方源） |
| 34 | [OpenCode Zen（agent 客户端模型网关）](https://opencode.ai/zen) | 其他（非免费） | ℹ️ 其他（非免费）：其他（非免费）｜模型：GLM/Kimi/Qwen 等精选池（官方统一基准测试） | — | — | opencode 客户端配 Zen endpoint，$20 起充 | 无免费层、无注册赠送；卖点为『零加成单价 + 挑过模型的网关』，与 OpenRouter :free 组合可白嫖 | 长期有效 | ✅ [opencode.ai](https://opencode.ai/zen) | —（本会话未直接读到第三方源） |
| 35 | [Kilo Code（IDE/CLI agent 客户端）](https://kilocode.ai) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：500+ 模型零加成；免费模型池（Auto Free 自动路由） | — | — | GitHub/邮箱注册 app.kilo.ai → 装 VS Code 插件或 CLI | 免费池额度与模型动态调整；限时活动以站内公告为准；企业版有 Cursor 迁移优惠（非白嫖主线） | 长期有效 | ✅ [kilocode.ai](https://kilocode.ai)<br>✅ [kilocode.ai](https://kilocode.ai/pricing) | —（本会话未直接读到第三方源） |
| 36 | [StepFun (阶跃星辰)](https://platform.stepfun.com/) | 限时活动 | ⏳ 限时活动：限时活动｜模型：stepaudio-3-chat-preview, stepaudio-3-realtime-preview, stepaudio-3-music-preview | — | — | 注册即可申请 API Key | 仅 stepaudio-3 系列 preview 模型标『限时免费』，随时可移出；text 模型无免费层 | 长期有效 | ✅ [platform.stepfun.com](https://platform.stepfun.com/docs/zh/guides/pricing/details) | —（本会话未直接读到第三方源） |
| 37 | [SenseTime SenseNova (商汤日日新)](https://token.sensenova.cn/) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：sensenova-u1.5-lite, sensenova-6.7-flash-lite | — 🚫 | — | Token Plan 页免费开始并申请 API Key | 公测期免费：每 5 小时 1500 次请求，模型独立计数；公测截止未公示 | 长期有效 | ✅ [www.sensetime.com](https://www.sensetime.com/cn/news/sensenova-u1-5-lite-token-plan-20260911-1741) | —（本会话未直接读到第三方源） |
| 38 | [Alibaba Tongyi Lingma (通义灵码)](https://lingma.aliyun.com/) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：tongyi-lingma(qwen 系列内置) | — | — | 下载 IDE 插件登录阿里账号即可 | 个人版不限时长免费；专业版 59 元/月（多渠道限时免费，活动制可收回） | 长期有效 | ✅ [lingma.aliyun.com](https://lingma.aliyun.com/) | —（本会话未直接读到第三方源） |
| 39 | [Baidu Comate (文心快码)](https://comate.baidu.com/) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：comate(文心内置) | — | — | 安装 VSCode/JetBrains 插件并登录 | 个人标准版免费；专业/企业版按人头收费 | 长期有效 | ✅ [comate.baidu.com](https://comate.baidu.com/zh/page/un1ao36mvok) | —（本会话未直接读到第三方源） |
| 40 | [Fitten Code (非十科技)](https://code.fittentech.com/) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：fittencode(自研代码模型) | — | — | 官网注册免费账户，装 VSCode/JetBrains 插件即用 | Individual 档 Free；部分 Pro 能力『限时免费』；无 API 出口 | 长期有效 | ✅ [code.fittentech.com](https://code.fittentech.com/) | —（本会话未直接读到第三方源） |
| 41 | [Zhipu CodeGeeX (智谱)](https://codegeex.cn/) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：codegeex-4(基于 GLM 自研) | — | — | 官网下载插件注册即用 | 个人用户免费；插件型无 API 赠金语义（不与 zhipu-bigmodel 重复计） | 长期有效 | ✅ [codegeex.cn](https://codegeex.cn/) | —（本会话未直接读到第三方源） |
| 42 | [NVIDIA NIM](https://build.nvidia.com) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：nvidia/nemotron-3-ultra-550b-a55b, deepseek-ai/deepseek-v4, qwen/qwen3-coder | — | — | build.nvidia.com 注册后 Dashboard 生成 API key | 免费原型层按限速运行（多数模型 40 RPM），不按 token 计费 | 长期有效 | ✅ [build.nvidia.com](https://build.nvidia.com/en-us) | —（本会话未直接读到第三方源） |
| 43 | [Cohere](https://dashboard.cohere.com) | 免费层 | 🆓 免费层：33 请求/日｜模型：command-a-plus, command-a, command-a-reasoning, command-r7b, embed-4, rerank-3.5 | — | — | 注册即自动创建 Trial key | 1000 API calls/月（全端点合计）；Chat 20 RPM / Rerank 10 RPM；禁商用 | 长期有效 | ✅ [docs.cohere.com](https://docs.cohere.com/docs/rate-limits) | —（本会话未直接读到第三方源） |
| 44 | [Perplexity](https://www.perplexity.ai) | 免费层 | 🆓 免费层：3 请求/日｜模型：perplexity-web-pro-search, sonar | — 🔒 | — | 邮箱/Google 注册即享免费层 | 免费层约 3-5 次 Pro Search/天 + 1 次深度研究/月；API 侧无免费积分 | 长期有效 | ✅ [docs.perplexity.ai](https://docs.perplexity.ai/getting-started/pricing) | —（本会话未直接读到第三方源） |
| 45 | [Poe (Quora)](https://poe.com) | 签到积分 | ✅ 签到积分：签到 300 点/日｜模型：poe-bot-claude, poe-bot-gpt, poe-bot-gemini, poe-bot-grok | — 🔒 | — ⚠️ | 注册免费账户自动每日发放 points | 每日 points 24h 重置不结转；不可用于前沿模型；官方不公布具体点数 | 长期有效 | ✅ [help.poe.com](https://help.poe.com/hc/en-us/articles/19944206309524-Poe-FAQs) | —（本会话未直接读到第三方源） |
| 46 | [Cursor](https://cursor.com) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：composer, tab (completion), agent (受限) | — | — | 下载安装器+注册，无需信用卡入 Hobby 免费层 | Agent/Tab 有配额限制但官方从未公布具体数字；高峰 slow_queue 延迟 | 长期有效 | ✅ [cursor.com](https://cursor.com/pricing) | —（本会话未直接读到第三方源） |
| 47 | [Windsurf (Devin Desktop)](https://windsurf.com) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：swe-1.x, tab (completion), cascade-agent (受限) | — | — | windsurf.com/pricing 选 Free | Free 档 daily/weekly token 配额，官方未公布具体数值 | 长期有效 | ✅ [windsurf.com](https://windsurf.com/pricing) | —（本会话未直接读到第三方源） |
| 48 | [xAI Grok](https://grok.com) | 免费层 | 🆓 免费层：限速免费（量级未公布）｜模型：grok-4.7-fast | — 🔒 | — | X 或 grok.com 登录免费账户即享 Limited 使用 | free tier Limited（Chat+图像+Build）；具体数字官方未公布；无 API | 长期有效 | ✅ [x.ai](https://x.ai/pricing) | —（本会话未直接读到第三方源） |
| 49 | [Google Gemini Code Assist (individuals)](https://developers.google.com/gemini-code-assist) | 免费层 | 🆓 免费层：6,000 请求/日｜模型：gemini-code-assist(auto), gemini-cli(合并额度) | — | — | Google 账号登录装 IDE 插件即可，无信用卡 | 代码请求 6000/天 + 聊天 240/天；Agent/Gemini CLI 共享上限 | 长期有效 | ✅ [developers.google.com](https://developers.google.com/gemini-code-assist) | —（本会话未直接读到第三方源） |
| 50 | [MiniMax Code (international)](https://agent.minimax.io) | 签到积分 | ✅ 签到积分：签到 400 点/日｜模型：minimax-m3, minimax-m3.1-flash | — | — | 注册后每日完成 check-in 赚积分 | check-in 400 点/天，第 4/7 天各 1000 点/天，满周共 4000；积分 30 天有效；限于 MiniMax Code 客户端 | 长期有效 | ✅ [agent.minimax.io](https://agent.minimax.io/docs/code/account/usage) | —（本会话未直接读到第三方源） |
> 表内 50 条合计：持续 ≈ **$185/月** · 一次性 ≈ **$332**
<!-- AUTO-TABLE-END -->

## 免费内容怎么读

价值已**拆成两栏**，避免"一次性薅 5000 积分"和"天天能领"混在一个数字里：

- **持续价值（USD/月）**：政策存活期内可重复薅的部分——免费层日额度（日额度×30 折算）、每日签到积分、每月邀请返利、活动日领 credits。用厂商付费价（`est_usd_per_mtok` 或 `point_value_usd`）折算。
- **一次性价值（USD）**：只到账一次的部分——注册赠金/积分/tokens、试用金、人民币券。展示原始金额（有摊销说明写注）。
- **免费层（Rate-limited free tier）**：永久免费但限速（RPM/TPD/TPM），适合原型和小项目。
- **签到积分（Check-in）**：每日打卡送积分或 tokens（例如腾讯 WorkBuddy「月包 500 积分 + 签到/日」，以官方加量包价 1 积分=$0.03 锚定折算）。
- **限时活动（Promo）**：有明确 deadline 的活动，过期前排最前。
- 标 `—` 表示不限量限速型（价值取决于你的调用密度），标 `⚠️` 表示信源待核或数据陈旧，🔒 表示需登录页（非死链）。
- **官方验证 / 第三方验证两列**：按 `data/sources.yml` 如实列举本仓库**真实读到过**的信源（官方 docs/活动页 vs 独立媒体/社区），两列都不空 = 双源交叉印证；缺一边即为单源，两边都没有的条目排表尾并标 ⚠️。没核实过的页面不会进列——宁缺毋滥。

## 数据字段（PR 模板见 CONTRIBUTING.md）

| 字段 | 说明 |
|---|---|
| `provider / website / docs` | 厂商名、控制台入口、限额文档 |
| `offer.type` | 免费层 / 试用金 / 签到积分 / 一次性赠送 / 限时活动 |
| `offer.models` | 覆盖模型 |
| `offer.requests_day / tokens_day / tokens_month` | 量级上限 |
| `offer.points_daily / points_monthly / credits_day` | 签到与日领机制 |
| `offer.credits_usd / credits_cny / valid_months` | 一次性金额与摊销 |
| `offer.signup_tokens / signup_points` | 注册赠送 |
| `point_value_usd / est_usd_per_mtok` | 折算价格锚 |
| `value_override_recurring_usd / value_override_once_usd` | 人工指定某侧价值 |
| `restrictions` | 限制条件（并发/商用/实名/网络） |
| `signup` | 注册方法和手段 |
| `verified / confidence` | 最后人工核查日 + 信号强度 |

## 🍋 检索中有意思的发现（人工精选，随扫描更新）

- **WorkBuddy 的积分有官方价格锚**：免费版每月 500 积分 + 每日签到，而官方加量包是 **500 积分 = $15**——即 1 积分 $0.03，折算下来白嫖层月价值超 $100（含签到）。模型池含 Kimi-K3、GLM-5.3、DeepSeek-V4.1-Flash，Hy4 限时免费。社区已有人做了**自动签到脚本**（`88lin/workbuddy-auto-signin`，行动前先读它是否违反服务条款）。
- **Qoder（阿里国际版）天天有面包屑**：免费用户**每日桌面端领 100 通用 Credits**（2026-09-18 起长期活动），当天不领不累计；另有轮换的 SOTA 模型限时活动。CN 版（原灵码）社区版免费、Pro ¥59/月。
- **Qwen Code CLI 是其余 agent 客户端里最慷慨的**：`qwen-oauth` 免费池长期给 **2000 请求/天上限级别**的额度（Gemini CLI 只给 250/日），白嫖终端 agent 首选 Qwen。
- **OpenRouter 的隐藏加速器**：`:free` 模型默认 50 请求/天，但**历史累计充值满 $10（不要求消耗）就永久升到 1000 请求/天**——充 $10 相当于买了张长期饭票。
- **Cerebras 是政策多变教材**：2026-07-21 把“每日 100 万 tokens 永久免费”改成了 **$5 一次性试用金**。这类“免费层随时变试用金”是常态，盯 `verified` 日期比盯排名第一更靠谱。
- **智谱的邀请制经济学**：GLM-4.x-Flash 系**永久免费（并发 1）**已是大礼，但更狠的是邀请制——**每月最多邀 10 个新用户 = 每月最高 2 亿免费 tokens**，按付费价折算约 $22/月。
- **Google 除 Flash 免费外还有暗器**：**Google Search grounding 每月 5000 次免费**（带实时搜索的 RAG），做小时效敏感应用比纯模型免费值钱。
- **Groq 送了个免费的 agentic 模型**：`groq/compound`（会自己调工具的混合模型）在免费层也有 250 请求/天，做 agent demo 零成本。
- **活动下线史值得收藏**：硅基流动“注册送 2000 万 tokens”早已下线，改为实名送 ¥18 通用券；此类“羊毛速朽”提醒我们：看到粥要趁热。

## 自动扫描机制（每日 10:00 北京时间，结果发邮件日报）

1. `data/offers.yml` 里的每条记录，机器人每天会：
   - **探活**：访问 `website` 和 `docs` 链接，404/超时的条目会被打上 🚫 标记并开 issue；
   - **新鲜度**：`verified` 超过 45 天未人工复核的条目会标 ⚠️；
   - **折算**：拆分「持续 vs 一次性」两部分价值重新排序，同步重建**中英双语 README**（`README.md` / `README_EN.md`）+ `reports/` 快照 + **每日邮件**（HTML 正文 + md 附件，Secrets 缺失时自动跳过发送）；英文长文本单元格由 `src/i18n.py` 按条目维护，缺失时回落中文。
2. 数据任何人工变更都会在 git diff 里留下审计痕迹。

## 📮 订阅邮件（周自动送达）

不想自己跑机器人？**在 [Issues](https://github.com/yanqingwang/free-ai-credits/issues/new/choose) 选「📮 订阅 / 退订邮件」模板**，填邮箱提 issue，机器自动加密入档并回复确认：

- **默认每周一**收到整理好的《免费额度周报》（也可勾选每日）；
- 邮箱以 **AES-256 加密后**（`data/subscribers.enc`）随仓库公开——密文向爬虫不透明，维护者也**读不出明文**，发送时才由工作流解密；
- **表单环节**：机器人会在处理完的**几十秒内**自动把 issue 标题/正文脱敏（改为"已加密入档"），明文不长期留在公开页面；仓库 watcher 的实时通知邮件会包含原文（当前 watcher 实际上只有维护者一个人）；
- 退订：随时再开一个同样的 issue 把「动作」切到退订；
- 没有二次点击确认机制（无后端限制）；若有人冒名订阅了你的邮箱，邮件尾部有退订指引，也可提 issue 请维护者删除。

## ⚠️ 免责声明

- 一切以**各厂商控制台/定价页为准**，本仓库数据为参考快照，可能滞后 1 周以上；
- 免费额度政策变动频繁（Groq 2026-09 阵容精简、Cerebras 2026-07 取消永久免费层），请以 `verified` 日期自行判断新旧；
- 本仓库与任何厂商无利益关系，排名不含返利链接。

## Roadmap
- [ ] 各厂商页面自动 diff（不只探活，抓正文变化提醒）
- [ ] 每周 issue 自动 @ 上一期挂掉条目的提交者复核
- [ ] 接入社区提交模板（表单式）
