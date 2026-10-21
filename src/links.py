"""Link sanity: verify provider website/docs respond (single GET, short timeout)."""
import urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"


def check(url: str, timeout: int = 6) -> int | None:
    """Returns HTTP status code, or None if unreachable."""
    if not url or not url.startswith("http"):
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            r.read(2048)  # 只读一点，避免大页面拖时间
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None
