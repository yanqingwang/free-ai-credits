"""EN strings for README_EN.md auto table (prose stays in README_EN.md).

Free-text cells (signup / restrictions / models) are maintained here keyed by
`id` in data/offers.yml; any id missing from these dicts silently falls back to
the Chinese source texts so the table never breaks.
"""

TYPE_LABELS = {
    "免费层": "Free tier",
    "试用金": "Trial credits",
    "签到积分": "Check-in points",
    "一次性赠送": "One-time gift",
    "限时活动": "Limited-time promo",
    "其他（非免费）": "Other (not free)",
}

CONF_LABELS = {"high": "✅ two-source", "medium": "☑️ one-source", "low": "⚠️ unverified"}

SIGNUP = {
    "groq": "Email/GitHub OAuth signup → API Key at console.groq.com/keys",
    "openrouter": "Email signup, API key right away; no card needed",
    "cerebras": "Email signup at cloud.cerebras.ai → API Key",
    "google-ai-studio": "Sign in with Google → Get API key; free tier needs no card",
    "mistral": "Email/Google signup for the Experiment (free) tier API key; phone binding at console's discretion",
    "zhipu-bigmodel": "Phone signup; full quota after real-name KYC",
    "siliconflow": "Phone signup; current offer: ¥18 voucher after KYC",
    "tencent-hunyuan-lite": "Tencent Cloud account → enable Hunyuan → use hunyuan-lite",
    "cloudflare-workers-ai": "Cloudflare account → bind Workers AI, or REST API",
    "workbuddy": "Register on workbuddy site/App (incl. Microsoft Store); some promos require invite links",
    "volcengine-doubao": "Phone signup → enable each model in console → trial tokens granted",
    "alibaba-bailian": "Alibaba Cloud account → activate Bailian; new users get per-model quotas",
    "hf-inference": "HF account ships small monthly free credits (login only); PRO gets more",
    "gemini-cli": "Google account login; free tier needs no card",
    "qwen-code-cli": "npm i @qwen-code/qwen-code → auth via qwen-oauth device code; no card",
    "github-copilot-free": "One-click enable with a GitHub account; students get Copilot Student",
    "opencode-zen": "Configure the Zen endpoint in the opencode client; $20 minimum top-up",
    "kilo-code": "GitHub/email signup at app.kilo.ai → VS Code plugin or CLI",
    "qoder": "Download desktop client (intl) → email signup; free tier eligible",
    "trae": "GitHub/Google/email to create the IDE account",
}

RESTRICTIONS = {
    "groq": "Org-level rate caps; 200K tokens/day on main chat models; some models 500K TPD",
    "openrouter": ":free models 20 RPM / 50 RPD; $10 lifetime top-up unlocks 1000 RPD; request-based, token-free",
    "cerebras": "Trial tier: 5 RPM / 30K TPM / 1M tokens per hour & day; $5 one-time credits",
    "google-ai-studio": "Free-tier RPM keeps shrinking (429 at peak); Pro/advanced models excluded; own network needed in China",
    "mistral": "Strict throttling (~1 req/s); pooled monthly cap — real fill-rate far below; not for production SLA",
    "zhipu-bigmodel": "Free model family capped at 1 concurrent; invites require new-user KYC",
    "siliconflow": "Voucher settles in CNY; KYC mandatory for some models",
    "tencent-hunyuan-lite": "Concurrency per Tencent Cloud docs; lite series is rate-limited free",
    "cloudflare-workers-ai": "Neuron-billed; 10,000 free neurons/day (token count varies by model)",
    "workbuddy": "Points are the unified unit, consumed per model; base 500/mo burns in 2-3 days of heavy use; tasks & community posts earn more",
    "volcengine-doubao": "Granted per model on activation; exact amounts shown in console",
    "alibaba-bailian": "Quotas have expiry; exact amounts in console only",
    "hf-inference": "Free-account credits are tiny, mainly for trials; amounts shift",
    "gemini-cli": "Low free RPM/TPD (429 at peaks); model lineup shifts; shares pool with AI Studio",
    "qwen-code-cli": "OAuth free-pool limits per official docs; a paid DashScope key unlocks more",
    "github-copilot-free": "Limited access: completions + capped chats; enterprise accounts disabled; numbers per plans page",
    "opencode-zen": "No free tier, no signup grant; sells zero-markup rates with a vetted pool; pair with OpenRouter :free",
    "kilo-code": "Free-pool quotas/models shift; time-limited promos on the site board; enterprise Cursor deal off-roadmap",
    "qoder": "Claim 100 credits/day manually in-app, non-cumulative; free & paid individuals both; credit-to-USD undisclosed",
    "trae": "Token-billed Dollar Usage monthly grant; free tier queues first at peak; amounts per console",
}

MODELS = {
    "groq": ["gpt-oss-120b/20b", "qwen3.6/3.8-27b", "kimi-k2-instruct", "whisper-large-v3 (audio)"],
    "openrouter": ["19+ of :free-suffix text models (deepseek/qwen/llama...) + openrouter/free router"],
    "cerebras": ["Llama 4 Scout/Qwen3 + all models on trial credits"],
    "google-ai-studio": ["gemini-3.8-flash", "gemini-3.6-flash (free lineup shifts)"],
    "mistral": ["mistral-large", "mistral-medium", "codestral", "mistral-small"],
    "zhipu-bigmodel": ["glm-4-flash-250414 (free forever)", "glm-4.7-flash", "glm-4-air"],
    "siliconflow": ["200+ open-source CN models: Qwen / DeepSeek distills / GLM..."],
    "tencent-hunyuan-lite": ["hunyuan-lite (free forever)"],
    "cloudflare-workers-ai": ["Llama 3.x / Qwen2.5 / Mistral 7B / SDXL image"],
    "workbuddy": ["Kimi-K3", "GLM-5.3", "DeepSeek-V4.1-Flash", "Hy4 (limited-time free)"],
    "volcengine-doubao": ["doubao-seed full lineup (490K tokens per model)"],
    "alibaba-bailian": ["qwen series (per-model quotas)"],
    "hf-inference": ["HF routed inference, multi-backend (groq/together...)"],
    "gemini-cli": ["gemini-3.8-flash", "gemini-3.6-flash"],
    "qwen-code-cli": ["qwen3-coder series (OAuth free pool)"],
    "github-copilot-free": ["GitHub-designated limited model pool"],
    "opencode-zen": ["GLM/Kimi/Qwen vetted pool (officially benchmarked)"],
    "kilo-code": ["500+ zero-markup models; free model pool (Auto Free routing)"],
    "qoder": ["Qwen exclusive pool", "SOTA models (rotating promos)"],
    "trae": ["Claude / GPT / Gemini / DeepSeek pools"],
}
