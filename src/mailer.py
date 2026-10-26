"""Email delivery: render the daily digest markdown into a mobile-friendly HTML email + .md attachment.

The digest is a 13-column Markdown table, which is unreadable on a phone (horizontal
scrolling, 13px text). This module converts tables into a *responsive card layout*:

- Desktop / wide clients  → normal table (unchanged look).
- Narrow screens (phone)  → each table row reflows into a stacked "card": the row's
  first cell becomes the card title, every other cell is a label/value line.
- Clients that strip <style> (some Gmail variants) still get readable output because
  every cell carries a `data-label` attribute rendered as an inline prefix on mobile.

Only stdlib + markdown are used; no template engine.
"""
import html as _html
import os
import re
import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr, formatdate


# --- column → short mobile label (zh / en detected by header text) ------------
# Keep in sync with src/render.py HEADERS. Unknown headers fall back to the raw text.
_LABEL_ALIASES = {
    "#": "#",
    "厂商": "厂商", "Provider": "Provider",
    "国家/开源/评分": "国家", "Country/OSS/Score": "Country",
    "类型": "类型", "Type": "Type",
    "较昨日": "变化", "vs yesterday": "Change",
    "免费内容（模型）": "免费内容", "Free content (models)": "Free",
    "持续价值(USD/月)": "持续/月", "Recurring value (USD/mo)": "Recurring",
    "一次性价值(USD)": "一次性", "One-time value (USD)": "One-time",
    "注册方式": "注册", "Signup": "Signup",
    "限制条件": "限制", "Restrictions": "Limits",
    "有效期": "有效期", "Validity": "Validity",
    "官方验证": "官方源", "Official sources": "Official",
    "第三方验证": "第三方", "Third-party sources": "Third-party",
}

MOBILE_CSS = """
@media only screen and (max-width: 640px) {
  * { box-sizing: border-box !important; }
  html, body { width: 100% !important; overflow-x: hidden !important; }
  .wrap { width: 100% !important; max-width: 100% !important; padding: 10px !important; }
  table.digest, table.digest tbody, table.digest tr, table.digest td { display: block !important; width: 100% !important; max-width: 100% !important; }
  table.digest thead { display: none !important; }
  table.digest { min-width: 0 !important; }
  table.digest tr { box-sizing: border-box !important; border: 1px solid #e3e8ef; border-radius: 10px;
                    margin: 0 0 12px; padding: 10px 12px; background: #fff;
                    box-shadow: 0 1px 2px rgba(16,24,40,.06); }
  table.digest tr:first-child { margin-top: 0; }
  table.digest td { box-sizing: border-box !important; border: 0 !important; padding: 4px 0 !important;
                    font-size: 15px !important; line-height: 1.55 !important; word-break: break-word;
                    overflow-wrap: anywhere; }
  table.digest td::before { content: attr(data-label); display: block; font-size: 12px;
                            font-weight: 600; color: #667085; margin-bottom: 2px; }
  /* 序号列在手机上没意义，直接隐藏；厂商列当卡片标题 */
  table.digest td[data-label="#"] { display: none !important; }
  table.digest td[data-label="厂商"], table.digest td[data-label="Provider"] {
    font-size: 17px !important; font-weight: 700; color: #101828; padding-bottom: 6px !important;
    border-bottom: 1px dashed #e3e8ef !important; margin-bottom: 6px;
  }
  table.digest td[data-label="厂商"]::before, table.digest td[data-label="Provider"]::before { display: none; }
  /* 合计/备注行：不卡片化，按普通注释展示 */
  table.digest tr.note-row { border: 0 !important; box-shadow: none !important; background: #f8fafc !important;
                             padding: 8px 10px !important; border-radius: 6px; }
  table.digest tr.note-row td { font-size: 13px !important; color: #475467 !important; }
  table.digest tr.note-row td::before { display: none; }
  h1 { font-size: 20px !important; }
  h2 { font-size: 17px !important; }
}
"""

BASE_CSS = """
* { box-sizing: border-box; }
.table-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
table.digest { border-collapse: collapse; width: 100%; min-width: 880px; }
table.digest th { background: #f8fafc; color: #344054; font-weight: 600; text-align: left;
                  border: 1px solid #e3e8ef; padding: 7px 8px; font-size: 12px; white-space: nowrap; }
table.digest td { border: 1px solid #e3e8ef; padding: 7px 8px; font-size: 12.5px;
                  vertical-align: top; word-break: normal; overflow-wrap: break-word; }
table.digest tr:nth-child(even) td { background: #fcfcfd; }
a { color: #2563eb; text-decoration: none; }
h1 { font-size: 24px; margin: 0 0 6px; }
h2 { font-size: 19px; margin: 24px 0 10px; padding-top: 4px; }
hr { border: 0; border-top: 1px solid #e3e8ef; margin: 20px 0; }
code { background: #f2f4f7; padding: 1px 4px; border-radius: 4px; font-size: 12px; }
"""


def _label_for(header: str) -> str:
    key = header.strip()
    return _LABEL_ALIASES.get(key, key)


def _annotate_tables(html: str) -> str:
    """Add data-label to every <td> based on its column header, and class="digest" to tables."""

    def fix_table(m: re.Match) -> str:
        table_html = m.group(0)
        # collect header labels in order
        head = re.search(r"<thead>(.*?)</thead>", table_html, re.S)
        labels = []
        if head:
            labels = [_label_for(_strip_tags(c)) for c in re.findall(r"<th[^>]*>(.*?)</th>", head.group(1), re.S)]

        row_idx = [0]

        def fix_row(rm: re.Match) -> str:
            row = rm.group(0)
            idx = row_idx[0]
            row_idx[0] += 1
            cells = re.findall(r"<td[^>]*>.*?</td>", row, re.S)
            # 合计/备注行 = 宽表里只有第一个单元格有内容、其余全空（report 把 `> Totals ...` 塞进表格）。
            # 窄表（<5 列）不当备注行，避免误判正常小表。
            if len(cells) >= 5:
                rest_empty = all(not _strip_tags(c).strip() for c in cells[1:])
                if rest_empty:
                    inner = re.sub(r"^<td[^>]*>", "<td>", cells[0])
                    return f'<tr class="note-row">{inner}</tr>'
            out = row
            for i, cell in enumerate(cells):
                if "data-label=" in cell:
                    continue
                label = labels[i] if i < len(labels) else ""
                if not label:
                    continue
                new_cell = cell.replace("<td", f'<td data-label="{_html.escape(label, quote=True)}"', 1)
                out = out.replace(cell, new_cell, 1)
            return out

        # only annotate body rows (inside tbody or after thead)
        body = re.search(r"<tbody>(.*?)</tbody>", table_html, re.S)
        if body:
            new_body = re.sub(r"<tr>.*?</tr>", fix_row, body.group(1), flags=re.S)
            table_html = table_html.replace(body.group(0), f"<tbody>{new_body}</tbody>", 1)
        table_html = table_html.replace("<table>", '<table class="digest">', 1)
        return table_html

    return re.sub(r"<table>.*?</table>", fix_table, html, flags=re.S)


def _strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def md_to_html(md_text: str) -> str:
    import markdown
    html = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    # SVG 多数邮箱客户端会被拦截，邮件正文里剥掉
    html = re.sub(r"<svg.*?</svg>", "", html, flags=re.S)
    # 表格 → 响应式卡片（手机自适应）
    html = _annotate_tables(html)
    # 桌面端宽表用横向滚动容器包一层（窄屏下容器展开为卡片，无影响）
    html = re.sub(r'(<table class="digest">.*?</table>)', r'<div class="table-scroll">\1</div>', html, flags=re.S)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="format-detection" content="telephone=no">
<title>Free AI Credits Daily</title>
<style>
{BASE_CSS}
{MOBILE_CSS}
</style>
</head>
<body style="margin:0;padding:0;background:#f6f7f9;">
<div class="wrap" style="font-family:-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;
     max-width:1040px;margin:0 auto;padding:16px;color:#222;line-height:1.6;background:#fff;">
{html}
<hr>
<small style="color:#667085;">本邮件由 free-ai-credits 流水线每日自动发送（仅供参考快照，以各厂商控制台为准）</small>
</div>
</body>
</html>"""


def enabled() -> bool:
    return bool(os.environ.get("SMTP_USER")) and bool(os.environ.get("SMTP_PASS"))


def send(subject: str, md_text: str, attach_path: str | None = None, to: str | None = None) -> None:
    host = os.environ.get("SMTP_HOST") or "smtp.qq.com"
    port = int(os.environ.get("SMTP_PORT") or 465)
    user = os.environ["SMTP_USER"]
    pwd = os.environ["SMTP_PASS"]
    from_addr = os.environ.get("MAIL_FROM", user)
    to_addrs = ([to] if to else [x.strip() for x in os.environ.get("MAIL_TO", user).split(",") if x.strip()])

    msg = MIMEMultipart("mixed")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = formataddr((str(Header("Free AI Credits Bot · 免费额度日报", "utf-8")), from_addr))
    msg["To"] = ", ".join(to_addrs)
    msg["Date"] = formatdate()

    msg.attach(MIMEText(md_to_html(md_text), "html", "utf-8"))

    if attach_path and os.path.exists(attach_path):
        with open(attach_path, "rb") as f:
            att = MIMEApplication(f.read())
        att.add_header("Content-Disposition", "attachment",
                       filename=("utf-8", "", os.path.basename(attach_path)))
        msg.attach(att)
    ctx = ssl.create_default_context()
    if port == 465:
        server = smtplib.SMTP_SSL(host, port, context=ctx, timeout=30)
    else:
        server = smtplib.SMTP(host, port, timeout=30)
        server.starttls(context=ctx)
    try:
        server.login(user, pwd)
        server.sendmail(from_addr, to_addrs, msg.as_string())
    finally:
        server.quit()
