#!/usr/bin/env python3
"""将 Markdown 研报转换为微信公众号兼容的 HTML 格式。

用法：
    python scripts/wechat_publish.py research/某研报.md
    python scripts/wechat_publish.py research/某研报.md --dry-run   # 仅打印不写文件
    python scripts/wechat_publish.py research/某研报.md -o output.html
"""

import re
import sys
from pathlib import Path
from html import escape


def _inline_format(text: str) -> str:
    """处理 Markdown 内联格式：加粗、斜体、行内代码、链接。"""
    # 转义 HTML 但保留我们将注入的标签
    text = escape(text)

    # 加粗 **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)

    # 斜体 *text*（不误匹配 ** 中的内容）
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)

    # 行内代码 `text`
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)

    # 图片 ![alt](url) — 公众号需手动上传，留占位标记（必须在链接之前处理）
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<span style="color:#888;">[图片：\1 — 请手动上传]</span>', text)

    # 链接 [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

    return text


def _parse_table(lines: list, start: int) -> str:
    """解析 Markdown 表格，返回公众号兼容的 HTML table。"""
    table_lines = []
    i = start
    while i < len(lines) and "|" in lines[i]:
        table_lines.append(lines[i])
        i += 1

    if len(table_lines) < 2:
        return "<p>" + escape(" | ".join(t.strip("|").split("|"))) + "</p>"

    header_line = table_lines[0]
    separator = table_lines[1]

    if not re.match(r"^[\|\s\-:]+$", separator.strip()):
        return "<p>" + escape(" | ".join(t.strip("|").split("|"))) + "</p>"

    alignments = []
    for cell in separator.strip("|").split("|"):
        cell = cell.strip()
        if cell.startswith(":") and cell.endswith(":"):
            alignments.append("center")
        elif cell.endswith(":"):
            alignments.append("right")
        else:
            alignments.append("left")

    headers = [c.strip() for c in header_line.strip("|").split("|")]
    while len(alignments) < len(headers):
        alignments.append("left")

    th_cells = "".join(
        f'<th style="text-align:{alignments[j] if j < len(alignments) else "left"};">{_inline_format(h)}</th>'
        for j, h in enumerate(headers)
    )
    thead = f"<thead><tr>{th_cells}</tr></thead>"

    tbody_rows = []
    for row_line in table_lines[2:]:
        cells = [c.strip() for c in row_line.strip("|").split("|")]
        while len(cells) < len(headers):
            cells.append("")
        td_cells = "".join(
            f'<td style="text-align:{alignments[j] if j < len(alignments) else "left"};">{_inline_format(cells[j])}</td>'
            for j in range(len(headers))
        )
        tbody_rows.append(f"<tr>{td_cells}</tr>")
    tbody = f"<tbody>{''.join(tbody_rows)}</tbody>"

    return f'<table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;width:100%;">{thead}{tbody}</table>'


def md_to_wechat(md_text: str) -> str:
    """将 Markdown 文本转换为公众号兼容的 HTML。"""
    lines = md_text.split("\n")
    result = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # 跳过 frontmatter (--- 包裹的 YAML)
        if i == 0 and stripped == "---":
            i += 1
            while i < n and lines[i].strip() != "---":
                i += 1
            i += 1  # 跳过闭合的 ---
            continue

        # 空行
        if not stripped:
            result.append("<br>")
            i += 1
            continue

        # 代码块
        if stripped.startswith("```"):
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(escape(lines[i]))
                i += 1
            i += 1  # 跳过闭合 ```
            code_text = "\n".join(code_lines)
            result.append(f"<pre><code>{code_text}</code></pre>")
            continue

        # 表格（最少需要下一行做分隔符判断）
        if "|" in stripped and i + 1 < n and re.match(r"^[\|\s\-:]+$", lines[i + 1].strip()):
            table_html = _parse_table(lines, i)
            result.append(table_html)
            while i < n and "|" in lines[i]:
                i += 1
            continue

        # 标题 H1
        if re.match(r"^# (.+)", stripped):
            text = _inline_format(re.match(r"^# (.+)", stripped).group(1))
            result.append(f"<h1>{text}</h1>")
            i += 1
            continue

        # 标题 H2
        if re.match(r"^## (.+)", stripped):
            text = _inline_format(re.match(r"^## (.+)", stripped).group(1))
            result.append(f"<h2>{text}</h2>")
            i += 1
            continue

        # 标题 H3
        if re.match(r"^### (.+)", stripped):
            text = _inline_format(re.match(r"^### (.+)", stripped).group(1))
            result.append(f"<h3>{text}</h3>")
            i += 1
            continue

        # 分隔线
        if stripped == "---":
            result.append("<hr>")
            i += 1
            continue

        # 引用块
        if stripped.startswith(">"):
            text = _inline_format(stripped[1:].strip())
            result.append(f"<blockquote><p>{text}</p></blockquote>")
            i += 1
            continue

        # 无序列表
        if re.match(r"^- (.+)", stripped):
            result.append("<ul>")
            while i < n and re.match(r"^- (.+)", lines[i].strip()):
                text = _inline_format(re.match(r"^- (.+)", lines[i].strip()).group(1))
                result.append(f"<li>{text}</li>")
                i += 1
            result.append("</ul>")
            continue

        # 有序列表
        if re.match(r"^\d+\. (.+)", stripped):
            result.append("<ol>")
            while i < n and re.match(r"^\d+\. (.+)", lines[i].strip()):
                text = _inline_format(re.match(r"^\d+\. (.+)", lines[i].strip()).group(1))
                result.append(f"<li>{text}</li>")
                i += 1
            result.append("</ol>")
            continue

        # 普通段落
        text = _inline_format(stripped)
        result.append(f"<p>{text}</p>")
        i += 1

    # 追加免责声明
    result.append("<hr>")
    result.append(
        '<p style="font-size:12px;color:#999;">免责声明：本报告仅供信息参考，'
        "不构成投资建议。投资有风险，入市需谨慎。"
        '更多深度研究请访问 <a href="https://touziyanlun.github.io/investment-lab/">touziyanlun.github.io/investment-lab</a></p>'
    )

    return "\n".join(result)


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="将 Markdown 研报转换为微信公众号兼容 HTML"
    )
    parser.add_argument("input", help="输入的 Markdown 文件路径")
    parser.add_argument("-o", "--output", default=None, help="输出文件路径（默认：同目录下 .wechat.html）")
    parser.add_argument("--dry-run", action="store_true", help="仅打印 HTML 到终端，不写文件")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"错误：文件不存在 — {args.input}", file=sys.stderr)
        sys.exit(1)

    md_text = input_path.read_text(encoding="utf-8")
    html_body = md_to_wechat(md_text)

    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(input_path.stem)}</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.8; color: #333; max-width: 680px; margin: 0 auto; padding: 16px; font-size: 15px; }}
h1 {{ font-size: 22px; font-weight: 700; margin: 24px 0 12px; color: #1a1a1a; }}
h2 {{ font-size: 19px; font-weight: 700; margin: 20px 0 10px; color: #2c2c2c; }}
h3 {{ font-size: 16px; font-weight: 700; margin: 16px 0 8px; color: #2c2c2c; }}
p {{ margin: 8px 0; }}
blockquote {{ border-left: 3px solid #ccc; padding: 8px 16px; margin: 12px 0; color: #666; background: #f9f9f9; }}
pre {{ background: #f5f5f5; padding: 12px; overflow-x: auto; font-size: 13px; border-radius: 4px; }}
code {{ font-family: "SF Mono", "Menlo", "Monaco", "Courier New", monospace; font-size: 13px; background: #f0f0f0; padding: 1px 4px; border-radius: 2px; }}
pre code {{ background: none; padding: 0; }}
strong {{ color: #1a1a1a; }}
em {{ font-style: italic; }}
table {{ border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 14px; display: block; overflow-x: auto; }}
th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
th {{ background: #f0f0f0; font-weight: 600; }}
hr {{ border: none; border-top: 1px solid #eee; margin: 24px 0; }}
ol, ul {{ padding-left: 24px; margin: 8px 0; }}
li {{ margin: 4px 0; }}
a {{ color: #576b95; text-decoration: none; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

    if args.dry_run:
        print(full_html)
    else:
        output_path = Path(args.output) if args.output else input_path.with_suffix(".wechat.html")
        output_path.write_text(full_html, encoding="utf-8")
        print(f"已生成：{output_path}")


if __name__ == "__main__":
    main()
