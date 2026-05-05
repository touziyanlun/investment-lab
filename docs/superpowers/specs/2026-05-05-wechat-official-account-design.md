# 微信公众号搭建 — 设计规格

> **日期**：2026-05-05
> **状态**：设计已确认，待实现
> **关联项目**：investment-lab

---

## 一、目标

为「投资严论」搭建微信公众号，将 investment-lab 的 Markdown 研报完整搬运发布。

## 二、约束与决策

| 维度 | 决策 |
|------|------|
| 账号类型 | 个人订阅号（需用户自行注册，无 API 发布权限） |
| 品牌 | 与 touziyanlun.github.io 同名同品牌「投资严论」 |
| 内容策略 | 完整搬运，一篇研报对应一篇公众号文章 |
| 发布方式 | 手动（本地生成 HTML → 复制到公众号后台 → 发布） |

## 三、技术方案

### 核心工具：Python 转换脚本

位置：`scripts/wechat_publish.py`

输入：`research/<研报>.md`
输出：`research/<研报>.wechat.html`

功能：
- Markdown → 公众号兼容 HTML（内联样式，无外部 CSS）
- 表格自适应（公众号表格列多时加横向滚动）
- 代码块适配（等宽字体、浅灰底色）
- 图片处理（本地图片提示上传，网络图片保留）
- 加粗/斜体/标题层级保留
- 免责声明尾部自动追加
- 支持指定输出路径和仅预览（dry-run）

### 辅助工具：Markdown Here 浏览器插件

用途：快速将 Markdown 粘贴到公众号编辑器中转换，适用于临时内容和预览。

## 四、项目结构

```
investment-lab/
├── scripts/
│   └── wechat_publish.py     # 转换脚本
├── research/
│   └── *.md                  # 源文件
│   └── *.wechat.html         # 生成文件（不入库）
└── .gitignore                # 新增 *.wechat.html
```

## 五、使用流程

```
python scripts/wechat_publish.py research/某研报.md
→ 生成 .wechat.html
→ 浏览器打开 → 全选复制
→ 粘贴到 mp.weixin.qq.com 编辑器
→ 调整封面图、摘要
→ 发布
```

## 六、非功能需求

- Python 脚本零外部依赖（仅用标准库）
- 支持 `--dry-run` 预览模式
- 生成 HTML 可直接在浏览器查看效果
- .wechat.html 加入 .gitignore

## 七、不在范围内

- 不自动创建/注册公众号（需用户自行操作）
- 不通过 API 自动发布（订阅号无此权限）
- 不做公众号后台管理（菜单、自动回复等）
- 不做粉丝互动功能
- 不做第三方编辑器集成
