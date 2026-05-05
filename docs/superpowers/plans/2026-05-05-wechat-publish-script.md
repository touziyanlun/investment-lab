# 微信公众号转换脚本 — 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 创建零依赖 Python 脚本，将 investment-lab 的 Markdown 研报转换为公众号兼容的 HTML。

**Architecture:** 单个 `scripts/wechat_publish.py`，标准库正则逐行解析 Markdown → 内联样式 HTML。处理表格、代码块、标题、加粗、分隔线、列表和引用块。输出自包含 `.wechat.html` 文件。

**Tech Stack:** Python 3.9+ 标准库（`re`, `sys`, `pathlib`, `argparse`, `html`）

---

## 文件结构

```
investment-lab/
├── scripts/
│   └── wechat_publish.py     # 新建：转换脚本
└── .gitignore                # 修改：排除 *.wechat.html
```

---

### Task 1: 创建脚本骨架和参数解析

**Files:**
- Create: `scripts/wechat_publish.py`

- [ ] **Step 1: 创建脚本骨架**

```python
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

    # 包裹完整 HTML 页面
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
```

- [ ] **Step 2: 验证脚本可运行**

```bash
python scripts/wechat_publish.py --help
```

期望：显示帮助信息，无报错。

- [ ] **Step 3: 提交**

```bash
git add scripts/wechat_publish.py
git commit -m "feat: 创建 wechat_publish.py 脚本骨架，含参数解析和 HTML 模板"
```

---

### Task 2: 实现 Markdown 核心解析 — 标题、加粗、分隔线

**Files:**
- Modify: `scripts/wechat_publish.py` — 完善 `md_to_wechat()` 函数

- [ ] **Step 1: 实现逐行解析引擎**

用状态机处理三种模式：普通段落、表格、代码块。替换 `md_to_wechat()` 函数：

```python
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

    return "\n".join(result)
```

- [ ] **Step 2: 实现内联格式化**

```python
def _inline_format(text: str) -> str:
    """处理 Markdown 内联格式：加粗、斜体、行内代码、链接、emoji 短代码。"""
    # 转义 HTML 但保留我们即将注入的标签
    text = escape(text)

    # 加粗 **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)

    # 斜体 *text*（不误匹配 ** 中的内容）
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)

    # 行内代码 `text`
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)

    # 链接 [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

    # 图片 ![alt](url) — 公众号需要手动上传图片，这里保留为占位标记
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<span style="color:#888;">[图片：\1 — 请手动上传]</span>', text)

    # Emoji 短代码 :smile: → 保留原样（微信支持常见 emoji）
    # 无需处理

    return text
```

- [ ] **Step 3: 用简单 Markdown 测试**

```bash
python -c "
md = '''# 标题测试
这是一段**加粗**和*斜体*的文字。
## 二级标题
- 列表项1
- 列表项2
1. 第一
2. 第二
'''
from scripts.wechat_publish import md_to_wechat
print(md_to_wechat(md))
"
```

期望：正确输出标题、加粗、斜体、列表的 HTML。

- [ ] **Step 4: 提交**

```bash
git add scripts/wechat_publish.py
git commit -m "feat: 实现 Markdown 核心解析 — 标题/加粗/列表/引用块/代码块"
```

---

### Task 3: 实现表格解析

**Files:**
- Modify: `scripts/wechat_publish.py` — 新增 `_parse_table()` 函数

- [ ] **Step 1: 实现表格解析函数**

```python
def _parse_table(lines: list, start: int) -> str:
    """解析 Markdown 表格，返回公众号兼容的 HTML table。

    公众号表格需要内联样式（border/cellpadding），
    且对列数不一致的行做补齐处理。
    """
    table_lines = []
    i = start
    while i < len(lines) and "|" in lines[i]:
        table_lines.append(lines[i])
        i += 1

    # 至少需要表头 + 分隔行
    if len(table_lines) < 2:
        return "<p>" + escape(" | ".join(t.strip("|").split("|"))) + "</p>"

    header_line = table_lines[0]
    separator = table_lines[1]

    # 确认是有效的表格分隔行
    if not re.match(r"^[\|\s\-:]+$", separator.strip()):
        return "<p>" + escape(" | ".join(t.strip("|").split("|"))) + "</p>"

    # 解析对齐方式
    alignments = []
    for cell in separator.strip("|").split("|"):
        cell = cell.strip()
        if cell.startswith(":") and cell.endswith(":"):
            alignments.append("center")
        elif cell.endswith(":"):
            alignments.append("right")
        else:
            alignments.append("left")

    # 解析表头
    headers = [c.strip() for c in header_line.strip("|").split("|")]

    # 确保对齐数量匹配
    while len(alignments) < len(headers):
        alignments.append("left")

    # 构建 thead
    th_cells = "".join(
        f'<th style="text-align:{alignments[j] if j < len(alignments) else "left"};">{_inline_format(h)}</th>'
        for j, h in enumerate(headers)
    )
    thead = f"<thead><tr>{th_cells}</tr></thead>"

    # 构建 tbody
    tbody_rows = []
    for row_line in table_lines[2:]:
        cells = [c.strip() for c in row_line.strip("|").split("|")]
        # 补全列数
        while len(cells) < len(headers):
            cells.append("")
        td_cells = "".join(
            f'<td style="text-align:{alignments[j] if j < len(alignments) else "left"};">{_inline_format(cells[j])}</td>'
            for j in range(len(headers))
        )
        tbody_rows.append(f"<tr>{td_cells}</tr>")
    tbody = f"<tbody>{"".join(tbody_rows)}</tbody>"

    return f'<table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;width:100%;">{thead}{tbody}</table>'
```

- [ ] **Step 2: 用研报测试表格解析**

```bash
python -c "
from pathlib import Path
from scripts.wechat_publish import md_to_wechat

md = Path('research/moutai-600519-deep-dive-2026-05.md').read_text()
html = md_to_wechat(md)
# 确认表格被正确转换为 HTML table
assert '<table' in html
assert '<thead>' in html
assert '</table>' in html
print('OK: 表格解析通过')
"
```

- [ ] **Step 3: 提交**

```bash
git add scripts/wechat_publish.py
git commit -m "feat: 实现 Markdown 表格 → 公众号 HTML table 解析"
```

---

### Task 4: 前端页码（frontmatter）跳过 + Emoji 星标处理

**Files:**
- Modify: `scripts/wechat_publish.py`

- [ ] **Step 1: 处理研报中使用的特殊符号**

研报中使用 `⭐` emoji 和 `🔴🟡🟢` 信号灯标记来表示评级，需要保留。Emoji 已经是 Unicode，无需额外处理。确认 `_inline_format` 中的 escape 不破坏 emoji。

```python
# 在 _inline_format 函数开头增加 emoji 保留逻辑
# escape() 不转义 Unicode emoji，无需额外处理
# 验证：Python 的 html.escape 只转义 & < > " '，不处理中文和 emoji
```

- [ ] **Step 2: 测试 emoji 保留**

```bash
python -c "
from scripts.wechat_publish import _inline_format
result = _inline_format('护城河 ⭐⭐⭐⭐⭐ 极高')
assert '⭐⭐⭐⭐⭐' in result
print('OK: emoji保留通过')
"
```

- [ ] **Step 3: 提交**

```bash
git add scripts/wechat_publish.py
git commit -m "feat: 确认 emoji 和特殊字符在转换中正确保留"
```

---

### Task 5: 完整端到端测试 + .gitignore 更新

**Files:**
- Modify: `.gitignore`
- Test: `scripts/wechat_publish.py` 全流程

- [ ] **Step 1: 更新 .gitignore**

```bash
echo "" >> .gitignore
echo "# WeChat publish output" >> .gitignore
echo "*.wechat.html" >> .gitignore
```

- [ ] **Step 2: 用多份研报端到端测试**

```bash
# 测试三份不同类型的研报
python scripts/wechat_publish.py research/hygon-688041-deep-dive-2026-05.md --dry-run > /tmp/test1.html
python scripts/wechat_publish.py research/moutai-600519-deep-dive-2026-05.md --dry-run > /tmp/test2.html
python scripts/wechat_publish.py research/alibaba-baba-deep-dive-2026-05.md --dry-run > /tmp/test3.html

# 验证均为有效 HTML 且包含关键内容
for f in /tmp/test1.html /tmp/test2.html /tmp/test3.html; do
    test -s "$f" && echo "OK: $f 非空"
    grep -q '<table' "$f" && echo "  + 表格已渲染"
    grep -q '<h1>' "$f" && echo "  + 标题已渲染"
    grep -q '</html>' "$f" && echo "  + 完整HTML结构"
done
```

- [ ] **Step 3: 测试输出文件模式**

```bash
python scripts/wechat_publish.py research/montage-688008-deep-dive-2026-05.md
ls -la research/montage-688008-deep-dive-2026-05.wechat.html

# 清理测试输出
rm research/montage-688008-deep-dive-2026-05.wechat.html
```

- [ ] **Step 4: 提交**

```bash
git add scripts/wechat_publish.py .gitignore
git commit -m "feat: 更新 .gitignore 排除 .wechat.html，完成端到端测试"
```
