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


def md_to_wechat(md_text: str) -> str:
    """将 Markdown 文本转换为公众号兼容的 HTML。"""
    lines = md_text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # 由后续 Task 逐个实现处理逻辑
        i += 1
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
