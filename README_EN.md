# Free AI Tokens: a bilingual watchlist of free LLM credits worldwide

> An open-source, **daily auto-verified** database scanning global LLM vendors (CN + intl) for free API gifts — free tiers, signup credits, daily check-in points, limited-time promos. Each row shows the model coverage, **recurring vs one-time value split in USD**, signup path, restrictions, and validity. **PRs welcome** for new vendors or corrections.

**Language / 语言切换：English (this page) · [中文](README.md)**

## 🏆 Free-token rankings (recurring value first)

<!-- AUTO-TABLE-START -->
_2026-10-21 auto-rebuilt · source of truth in [`data/offers.yml`](data/offers.yml)_

| # | Provider | Type | Free content (models) | Recurring value (USD/mo) | One-time value (USD) | Signup | Restrictions | Validity | Conf |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [腾讯 WorkBuddy（AI Agent 办公台）](https://www.workbuddy.ai) | Check-in points | ✅ Check-in points：signup gift 2,000 点 + 500 pts/mo + check-in 100 点/day｜models：Kimi-K3, GLM-5.3, DeepSeek-V4.1-Flash, Hy4 (limited-time free) | **$105/mo**<br>_(500 月包+100×30 签到) × $0.03/点 · 注册赠 2,000 点 × $0.03/点_ | **$60** | Register on workbuddy site/App (incl. Microsoft Store); some promos require inv… | Points are the unified unit, consumed per model; base 500/mo burns in 2-3 days of heavy u… | ongoing | ☑️ one-source |
| 2 | [智谱 AI BigModel](https://open.bigmodel.cn) | One-time gift | 💪 One-time gift：signup gift 200,000,000 tokens/mo + signup gift 20,000,000 tokens｜models：glm-4-flash-250414 (free forever), glm-4.7-flash, glm-4-air | **$22/mo**<br>_人工指定 · 注册赠 20,000,000 tokens × $0.11/1M_ | **$2.2** | Phone signup; full quota after real-name KYC | Free model family capped at 1 concurrent; invites require new-user KYC | ongoing | ✅ two-source |
| 3 | [Mistral La Plateforme](https://console.mistral.ai) | Free tier | 🆓 Free tier：1,000,000,000 tokens/mo｜models：mistral-large, mistral-medium, codestral, mistral-small | **$15/mo**<br>_人工指定_ | — | Email/Google signup for the Experiment (free) tier API key; phone binding at co… | Strict throttling (~1 req/s); pooled monthly cap — real fill-rate far below; not for prod… | ongoing | ☑️ one-source |
| 4 | [Cerebras](https://cloud.cerebras.ai) | Trial credits | 🎁 Trial credits：1,000,000 tokens/day + $5 credit｜models：Llama 4 Scout/Qwen3 + all models on trial credits | **$10.5/mo**<br>_1,000,000 tokens/日 × 30 × $0.35/1M · $5 一次性（摊 1 月）_ | **$5** | Email signup at cloud.cerebras.ai → API Key | Trial tier: 5 RPM / 30K TPM / 1M tokens per hour & day; $5 one-time credits | ongoing | ✅ two-source |
| 5 | [Groq](https://console.groq.com) | Free tier | 🆓 Free tier：1,000 req/day + 200,000 tokens/day｜models：gpt-oss-120b/20b, qwen3.6/3.8-27b, kimi-k2-instruct, whisper-large-v3 (audio) | **$1.8/mo**<br>_200,000 tokens/日 × 30 × $0.3/1M_ | — | Email/GitHub OAuth signup → API Key at console.groq.com/keys | Org-level rate caps; 200K tokens/day on main chat models; some models 500K TPD | ongoing | ✅ two-source |
| 6 | [硅基流动 SiliconFlow](https://cloud.siliconflow.cn) | One-time gift | 💪 One-time gift：¥18 voucher｜models：200+ open-source CN models: Qwen / DeepSeek distills / GLM... | —<br>_¥18 ≈ $2.50 一次性_ | **$2.5** | Phone signup; current offer: ¥18 voucher after KYC | Voucher settles in CNY; KYC mandatory for some models | ongoing | ✅ two-source |
| 7 | [OpenRouter](https://openrouter.ai) | Free tier | 🆓 Free tier：50 req/day｜models：19+ of :free-suffix text models (deepseek/qwen/llama...) + openrouter/free router | — | — | Email signup, API key right away; no card needed | :free models 20 RPM / 50 RPD; $10 lifetime top-up unlocks 1000 RPD; request-based, token-… | ongoing | ✅ two-source |
| 8 | [Google AI Studio / Gemini API](https://aistudio.google.com) | Free tier | 🆓 Free tier：rate-limited free (no published volume)｜models：gemini-3.8-flash, gemini-3.6-flash (free lineup shifts) | — | — | Sign in with Google → Get API key; free tier needs no card | Free-tier RPM keeps shrinking (429 at peak); Pro/advanced models excluded; own network ne… | ongoing | ✅ two-source |
| 9 | [Qoder（阿里，国际版 AI IDE）](https://qoder.com) | Check-in points | ✅ Check-in points：claim 100 credits/日｜models：Qwen exclusive pool, SOTA models (rotating promos) | — | — | Download desktop client (intl) → email signup; free tier eligible | Claim 100 credits/day manually in-app, non-cumulative; free & paid individuals both; cred… | ongoing | ✅ two-source |
| 10 | [Gemini CLI（终端 agent 客户端）](https://github.com/google-gemini/gemini-cli) | Free tier | 🆓 Free tier：250 req/day｜models：gemini-3.8-flash, gemini-3.6-flash | — | — | Google account login; free tier needs no card | Low free RPM/TPD (429 at peaks); model lineup shifts; shares pool with AI Studio | ongoing | ✅ two-source |
| 11 | [腾讯混元 Lite](https://lke.cloud.tencent.com/lke/#/hybrid/home) | Free tier | 🆓 Free tier：rate-limited free (no published volume)｜models：hunyuan-lite (free forever) | — | — | Tencent Cloud account → enable Hunyuan → use hunyuan-lite | Concurrency per Tencent Cloud docs; lite series is rate-limited free | ongoing | ☑️ one-source |
| 12 | [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | Free tier | 🆓 Free tier：rate-limited free (no published volume)｜models：Llama 3.x / Qwen2.5 / Mistral 7B / SDXL image | — | — | Cloudflare account → bind Workers AI, or REST API | Neuron-billed; 10,000 free neurons/day (token count varies by model) | ongoing | ☑️ one-source |
| 13 | [Trae（字节，AI IDE）](https://www.trae.ai) | Free tier | 🆓 Free tier：rate-limited free (no published volume)｜models：Claude / GPT / Gemini / DeepSeek pools | — | — | GitHub/Google/email to create the IDE account | Token-billed Dollar Usage monthly grant; free tier queues first at peak; amounts per cons… | ongoing | ☑️ one-source |
| 14 | [火山引擎豆包大模型](https://www.volcengine.com/product/doubao) | One-time gift | 💪 One-time gift：signup gift 490,000 tokens｜models：doubao-seed full lineup (490K tokens per model) | — | — | Phone signup → enable each model in console → trial tokens granted | Granted per model on activation; exact amounts shown in console | ongoing | ☑️ one-source |
| 15 | [Qwen Code CLI（终端 agent 客户端）](https://github.com/QwenLM/qwen-code) | Free tier | 🆓 Free tier：2,000 req/day｜models：qwen3-coder series (OAuth free pool) | — | — | npm i @qwen-code/qwen-code → auth via qwen-oauth device code; no card | OAuth free-pool limits per official docs; a paid DashScope key unlocks more | ongoing | ☑️ one-source |
| 16 | [GitHub Copilot Free（IDE/网页 agent 客户端）](https://github.com/features/copilot) | Free tier | 🆓 Free tier：rate-limited free (no published volume)｜models：GitHub-designated limited model pool | — | — | One-click enable with a GitHub account; students get Copilot Student | Limited access: completions + capped chats; enterprise accounts disabled; numbers per pla… | ongoing | ☑️ one-source |
| 17 | [OpenCode Zen（agent 客户端模型网关）](https://opencode.ai/zen) | Other (not free) | ℹ️ Other (not free)：Other (not free)｜models：GLM/Kimi/Qwen vetted pool (officially benchmarked) | — | — | Configure the Zen endpoint in the opencode client; $20 minimum top-up | No free tier, no signup grant; sells zero-markup rates with a vetted pool; pair with Open… | ongoing | ☑️ one-source |
| 18 | [Kilo Code（IDE/CLI agent 客户端）](https://kilocode.ai) | Free tier | 🆓 Free tier：rate-limited free (no published volume)｜models：500+ zero-markup models; free model pool (Auto Free routing) | — | — | GitHub/email signup at app.kilo.ai → VS Code plugin or CLI | Free-pool quotas/models shift; time-limited promos on the site board; enterprise Cursor d… | ongoing | ☑️ one-source |
| 19 | [阿里云百炼 DashScope](https://bailian.console.aliyun.com) | One-time gift | 💪 One-time gift：One-time gift｜models：qwen series (per-model quotas) | — | — ⚠️ | Alibaba Cloud account → activate Bailian; new users get per-model quotas | Quotas have expiry; exact amounts in console only | ongoing | ⚠️ unverified |
| 20 | [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) | Free tier | 🆓 Free tier：rate-limited free (no published volume)｜models：HF routed inference, multi-backend (groq/together...) | — | — ⚠️ | HF account ships small monthly free credits (login only); PRO gets more | Free-account credits are tiny, mainly for trials; amounts shift | ongoing | ⚠️ unverified |
> Totals over 20 rows: recurring ≈ **$154/mo** · one-time ≈ **$70**
<!-- AUTO-TABLE-END -->

## How to read the value columns

- **Recurring value (USD/mo)** — what keeps flowing as long as the deal lives: daily free-tier caps, check-in points, monthly invite rebates, credits-per-day promos. Converted with the vendor's paid price (`est_usd_per_mtok` or `point_value_usd`).
- **One-time value (USD)** — what lands once: signup token/point gifts, trial credits, CN¥ vouchers. Raw amounts, not monthly; the amortization note (if any) sits under the value cell.
- `—` means an uncapped rate-limited tier (value depends on your call density); `⚠️` marks weak sourcing or stale data; 🔒 marks login-walled pages (not dead links).

## Key data fields (template in CONTRIBUTING.md)

| Field | Meaning |
|---|---|
| `provider / website / docs` | Vendor, console entry, quota docs |
| `offer.type` | Free tier / Trial credits / Check-in / One-time gift / Promo |
| `offer.requests_day, tokens_day/month` | Volume caps |
| `offer.points_daily/monthly`, `credits_day` | Check-in & claim mechanics |
| `offer.credits_usd, credits_cny, valid_months` | One-shot grants & amortization |
| `point_value_usd / est_usd_per_mtok` | Price anchors used for conversion |
| `value_override_recurring_usd / once_usd` | Manual override, per side |
| `restrictions, signup` | Limits & how to register |
| `verified / confidence` | Last human check + signal strength |

## Automation (daily, 10:00 Beijing time)

1. Every row in `data/offers.yml` gets:
   - **Link check** — dead links get 🚫, login-walled 403s get 🔒 (kept visible, not counted dead);
   - **Freshness** — rows untouched by a human for 45+ days get flagged;
   - **Valuation** — recurring/one-time split is recomputed, rankings re-sorted, and both language READMEs are rebuilt; a snapshot lands in `reports/`; a **daily digest email** (HTML + `.md` attachment) goes out when SMTP secrets exist.
2. Every human data change leaves an auditable git diff.

## ⚠️ Disclaimer

- The consoles / pricing pages are always the truth; this repo is a reference snapshot and can lag by a day or more. Free tiers mutate — Cerebras swapped its forever-free tier for a $5 trial in 2026-07 — so judge by the `verified` date.
- No affiliate links, no vendor relationship.

## Roadmap

- [ ] Page-body diffs (not just liveness) for each vendor
- [ ] Weekly issue pinging the author of previously broken rows
- [ ] Community submission via form template
