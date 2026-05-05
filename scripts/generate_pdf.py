"""
将 Markdown 研究报告转换为美观的 PDF
使用 pandoc → HTML → weasyprint 流程
"""
import subprocess
import sys
import os
from weasyprint import HTML, CSS

def md_to_pdf(md_path, pdf_path=None):
    """将 Markdown 文件转换为 PDF"""
    if pdf_path is None:
        pdf_path = md_path.replace('.md', '.pdf')

    # 第一步：pandoc 转 HTML（带目录和独立模式）
    html_path = '/tmp/macro_temp.html'
    subprocess.run([
        'pandoc', md_path,
        '--metadata', 'title=投资严论 · 宏观深度',
        '--standalone',
        '--toc', '--toc-depth=2',
        '-o', html_path
    ], check=True)

    # 第二步：weasyprint 转 PDF，注入中文字体和精美样式
    css = CSS(string='''
        @page {
            size: A4;
            margin: 2.2cm 2.5cm 2.2cm 2.5cm;
            @bottom-center {
                content: counter(page);
                font-family: "Droid Sans Fallback", sans-serif;
                font-size: 9pt;
                color: #888;
            }
        }
        @page :first {
            @bottom-center {
                content: none;
            }
        }

        body {
            font-family: "Droid Sans Fallback", "Noto Sans CJK SC", sans-serif;
            font-size: 10.5pt;
            line-height: 1.75;
            color: #1a1a1a;
        }

        /* 标题样式 */
        h1 {
            font-size: 22pt;
            font-weight: 700;
            color: #1a237e;
            border-bottom: 2.5px solid #1a237e;
            padding-bottom: 8px;
            margin-top: 36pt;
            margin-bottom: 18pt;
            page-break-before: always;
        }
        h1:first-of-type {
            page-break-before: avoid;
            font-size: 26pt;
            text-align: center;
            border-bottom: none;
            margin-top: 60pt;
        }
        h2 {
            font-size: 15pt;
            font-weight: 600;
            color: #283593;
            margin-top: 28pt;
            margin-bottom: 12pt;
            padding-bottom: 4px;
            border-bottom: 1px solid #c5cae9;
        }
        h3 {
            font-size: 12pt;
            font-weight: 600;
            color: #3949ab;
            margin-top: 20pt;
            margin-bottom: 8pt;
        }

        /* 引用块 */
        blockquote {
            background: #f5f5f5;
            border-left: 4px solid #1a237e;
            margin: 16pt 0;
            padding: 10pt 16pt;
            font-size: 10pt;
            color: #555;
        }
        blockquote p {
            margin: 4pt 0;
        }

        /* 表格 */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 14pt 0;
            font-size: 9.5pt;
        }
        th {
            background-color: #1a237e;
            color: white;
            padding: 7pt 10pt;
            text-align: left;
            font-weight: 600;
        }
        td {
            padding: 6pt 10pt;
            border-bottom: 1px solid #e0e0e0;
        }
        tr:nth-child(even) td {
            background-color: #f5f5f5;
        }

        /* 代码块 */
        pre, code {
            font-family: "DejaVu Sans Mono", monospace;
            font-size: 8.5pt;
        }
        pre {
            background: #263238;
            color: #eeffff;
            padding: 12pt;
            border-radius: 4pt;
            overflow-x: auto;
            line-height: 1.5;
        }
        code {
            background: #e8eaf6;
            padding: 1pt 4pt;
            border-radius: 2pt;
        }
        pre code {
            background: none;
            padding: 0;
            color: inherit;
        }

        /* 分隔线 */
        hr {
            border: none;
            border-top: 1px dashed #c5cae9;
            margin: 24pt 0;
        }

        /* 强调 */
        strong {
            color: #1a237e;
        }

        /* 段落 */
        p {
            margin: 6pt 0;
            text-align: justify;
        }

        /* 列表 */
        ul, ol {
            padding-left: 20pt;
        }
        li {
            margin: 2pt 0;
        }

        /* 目录 */
        nav#TOC {
            page-break-after: always;
        }
        nav#TOC ul {
            list-style: none;
            padding-left: 0;
        }
        nav#TOC > ul > li > a {
            font-weight: 600;
            color: #1a237e;
            font-size: 11pt;
        }
        nav#TOC a {
            color: #3949ab;
            text-decoration: none;
            line-height: 1.6;
        }
    ''')

    HTML(filename=html_path).write_pdf(pdf_path, stylesheets=[css])
    print(f"PDF 已生成: {pdf_path}")
    return pdf_path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python generate_pdf.py <markdown文件路径> [输出pdf路径]")
        sys.exit(1)

    md_path = sys.argv[1]
    pdf_path = sys.argv[2] if len(sys.argv) > 2 else None
    md_to_pdf(md_path, pdf_path)
