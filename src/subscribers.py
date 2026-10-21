"""Subscriber registry: issue-form opt-in, encrypted at rest.

- data/subscribers.enc is OpenSSL AES-256-CBC ciphertext of `email,freq` lines.
- Key lives in repo secret SUBSCRIBER_KEY; storage file stays public but opaque
  (anti-harvest), and no plaintext email is ever committed.
- Modes: --add "email" --freq daily|weekly | --remove "email" | --list
"""
import os
import re
import subprocess
import sys

ENC_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "subscribers.enc")
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def _key() -> str:
    key = os.environ.get("SUBSCRIBER_KEY")
    if not key:
        print("SUBSCRIBER_KEY missing", file=sys.stderr)
        sys.exit(2)
    return key


def _openssl(args: list[str], input_bytes: bytes) -> bytes:
    env = dict(os.environ, SK=_key())
    r = subprocess.run(
        ["openssl"] + args, input=input_bytes, capture_output=True, env=env, check=True
    )
    return r.stdout


def _decrypt() -> list[tuple[str, str]]:
    if not os.path.exists(ENC_PATH):
        return []
    blob = open(ENC_PATH, "rb").read()
    if not blob.strip():
        return []
    text = _openssl(
        ["enc", "-d", "-aes-256-cbc", "-pbkdf2", "-pass", "env:SK"], blob
    ).decode("utf-8")
    out = []
    for line in text.splitlines():
        line = line.strip()
        if "," in line and EMAIL_RE.match(line.split(",")[0]):
            email, freq = line.split(",", 1)
            out.append((email.lower(), freq if freq in ("daily", "weekly") else "weekly"))
    return out


def _encrypt(pairs: list[tuple[str, str]]) -> None:
    text = "\n".join(f"{e},{f}" for e, f in pairs) + "\n"
    blob = _openssl(
        ["enc", "-aes-256-cbc", "-pbkdf2", "-pass", "env:SK"], text.encode("utf-8")
    )
    with open(ENC_PATH, "wb") as f:
        f.write(blob)


def add(email: str, freq: str) -> str:
    """Returns action taken for commenting back."""
    email = email.strip().lower()
    if not EMAIL_RE.match(email):
        return "invalid"
    freq = freq if freq in ("daily", "weekly") else "weekly"
    pairs = _decrypt()
    for i, (e, f) in enumerate(pairs):
        if e == email:
            if f == freq:
                return "exists"
            pairs[i] = (email, freq)
            _encrypt(pairs)
            return f"updated:{freq}"
    pairs.append((email, freq))
    _encrypt(pairs)
    return f"subscribed:{freq}"


def remove(email: str) -> str:
    email = email.strip().lower()
    pairs = [p for p in _decrypt() if p[0] != email]
    if len(pairs) == len(_decrypt()):
        return "not_found"
    _encrypt(pairs)
    return "removed"


def sendable(today) -> list[tuple[str, str]]:
    """Subscribers due today: daily ones every day, weekly ones only Monday."""
    out = []
    for email, freq in _decrypt():
        if freq == "daily" or today.weekday() == 0:
            out.append((email, freq))
    return out


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--add", help="email to add")
    ap.add_argument("--remove", help="email to remove")
    ap.add_argument("--freq", default="weekly", choices=["daily", "weekly"])
    ap.add_argument("--list", action="store_true", help="print decrypted emails (owner ops)")
    a = ap.parse_args()
    if a.add:
        print(add(a.add, a.freq))
    elif a.remove:
        print(remove(a.remove))
    elif a.list:
        for e, f in _decrypt():
            print(f"{e},{f}")
