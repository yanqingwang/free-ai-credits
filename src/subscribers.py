"""Subscriber registry: issue-form opt-in, encrypted at rest.

- data/subscribers.enc is OpenSSL AES-256-CBC ciphertext of one `email` per line.
  Legacy rows were `email,freq`; the freq column is ignored and rewritten away on
  the next update (delivery is weekly-Friday for everyone, so freq is moot).
- Key lives in repo secret SUBSCRIBER_KEY; storage file stays public but opaque
  (anti-harvest), and no plaintext email is ever committed.
- Modes: --add "email" | --remove "email" | --list
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


def _decrypt() -> list[str]:
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
        email = line.split(",", 1)[0].strip().lower()   # 丢弃历史 freq 列
        if EMAIL_RE.match(email):
            out.append(email)
    return out


def _encrypt(emails: list[str]) -> None:
    text = "\n".join(emails) + "\n"
    blob = _openssl(
        ["enc", "-aes-256-cbc", "-pbkdf2", "-pass", "env:SK"], text.encode("utf-8")
    )
    with open(ENC_PATH, "wb") as f:
        f.write(blob)


def add(email: str) -> str:
    """Returns action taken for commenting back."""
    email = email.strip().lower()
    if not EMAIL_RE.match(email):
        return "invalid"
    emails = _decrypt()
    if email in emails:
        return "exists"
    emails.append(email)
    _encrypt(emails)
    return "subscribed"


def remove(email: str) -> str:
    email = email.strip().lower()
    emails = _decrypt()
    kept = [e for e in emails if e != email]
    if len(kept) == len(emails):
        return "not_found"
    _encrypt(kept)
    return "removed"


def all() -> list[str]:
    """Everyone gets the Friday digest."""
    return _decrypt()


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--add", help="email to add")
    ap.add_argument("--remove", help="email to remove")
    ap.add_argument("--list", action="store_true", help="print decrypted emails (owner ops)")
    a = ap.parse_args()
    if a.add:
        print(add(a.add))
    elif a.remove:
        print(remove(a.remove))
    elif a.list:
        for e in _decrypt():
            print(e)
