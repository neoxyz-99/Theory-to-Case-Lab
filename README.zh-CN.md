# Theory-to-Case Lab：理论解释案例实验室

[English](README.md) · [MIT License](LICENSE) · [参与贡献](CONTRIBUTING.md)

这是一个面向人文社会科学的中英双语 Agent Skill，用于重构理论、梳理学界接受史，并说明理论如何真正解释具体案例。

默认输出两份互相链接的 Markdown 笔记：

1. 聚焦原著的**文献解读**；
2. 聚焦外部研究的**学界评价与理论应用**。

当用户提供具体研究案例时，增加可选的第三份**理论解释案例实验室**，逐步重构机制或解释路径，列出证据、对手解释、反证与适用边界。

## 创新点

代表性的学术 Agent 项目主要聚焦检索、文献综述、论文批评或大规模理论综合，例如 [Literature Review Skills](https://github.com/xingtaxueshu/literature-review-skills)、[LitReviewSkill](https://github.com/Zsun79/LitReviewSkill) 和 [Asta Theorizer](https://github.com/allenai/asta-theorizer)。本项目与它们在检索、综合和引用管理等基础层面存在重合，差异化重点是把原著重构、学界接受、符合认识论的案例解释和论文分析连成一条完整工作流。

- **低噪声证据分层**：阅读提示完整解释 `[P]` 原著、`[S]` 外部研究、`[A]` 分析者重构，以及例外性的混合标记 `[P/A]`、`[S/A]`；正文只在来源可能混淆处标注，不再逐段重复。
- **双文件认识论架构**：原著观点与后来的解释、批评、修正和应用分别处理。
- **机制优先**：把概念贴到案例上不等于完成解释。
- **多元解释形式**：因果、解释性、批判性、谱系性和规范性理论采用不同路径。
- **对手解释和边界**：应用必须处理反事实或替代阅读、反证以及适用范围。
- **分析型可视化**：图形用于显示结构、过程、争论或层次；每张图先说明用途、编码、证据类别和推论边界。
- **中英双语研究工作流**：保留原文概念，兼容 Obsidian 双向链接和已确认的 Zotero URI。

以上定位来自有目的的代表性比较，不宣称穷尽所有相关项目，也不使用“全球首创”之类无法核实的表述。

## 输出结构

| 使用情形 | 中文文件 | 英文文件 |
|---|---|---|
| 上传理论文献 | `作者_短标题_文献解读.md` + `作者_短标题_学界评价与理论应用.md` | `Author_Short_Title_Reading_Note.md` + `Author_Short_Title_Scholarly_Reception_and_Applications.md` |
| 同时提供案例 | 增加 `作者_短标题_理论解释案例实验室.md` | 增加 `Author_Short_Title_Theory_to_Case_Lab.md` |

第二份笔记必须报告检索日期、数据库或工具、查询范围、纳入逻辑和访问限制。外部研究不足时，如实记录，不补造共识、评价或引文。

## 两类解释路径

因果或机制性理论：

```text
结果差异 → 理论位置 → 资源与约束 → 作用机制
→ 选择空间变化 → 结果与分配后果
```

解释性、批判性、谱系性或规范性理论：

```text
文本/实践 → 概念定位 → 解释性操作
→ 被揭示的意义或权力关系 → 替代阅读 → 适用边界
```

本 Skill 不会把解释性理论强行改写成因果理论。

## 可视化规范

每张图之前先说明：

- 为什么文字或表格不足；
- 节点和箭头分别表示什么；
- 图示依据 `[P]`、`[S]` 还是 `[A]`；
- 这张图不能证明什么。

默认使用 Markdown 表格和 Mermaid。两份默认笔记分别最多两张图，Case Lab 最多三张图。只有用户明确要求探索可调条件或不同情景时，才生成互动可视化。

阅读提示必须说明全部简单与组合标记；斜线只表示“来源材料＋分析”，不是新的来源类别。默认把来源陈述与分析拆开，只有无法自然拆分的短综合才使用组合标记。强调样式具有固定含义：**粗体**表示核心命题或机制，<mark>高亮</mark>表示可直接服务于研究写作的发现，<u>下划线</u>表示边界或常见误读，*斜体*表示措辞敏感的原文术语。格式不能代替证据来源。

## 安装

可以通过 Skill Installer 从本仓库安装，或手动复制：

```bash
git clone https://github.com/neoxyz-99/Theory-to-Case-Lab.git
cp -R Theory-to-Case-Lab/skills/analyze-theory "$CODEX_HOME/skills/analyze-theory"
```

若未设置 `CODEX_HOME`，Codex 通常使用 `~/.codex`。

其他兼容 Agent Skills 的工具可以将 `skills/analyze-theory` 复制到其 Skills 目录。PDF、OCR、学术搜索和 Zotero 能力取决于宿主工具。

## 使用示例

```text
请使用 $analyze-theory 分析这篇理论文献，生成中文双文件，
保留原文概念，并区分原著、学界研究和你的分析。
```

```text
请使用 $analyze-theory 将这个理论用于我的案例，
生成 Theory-to-Case Lab，并比较一个有竞争力的替代解释。
```

## 验证

双文件：

```bash
python skills/analyze-theory/scripts/validate_theory_dossier.py \
  --reading path/to/文献解读.md \
  --reception path/to/学界评价与理论应用.md
```

三文件：

```bash
python skills/analyze-theory/scripts/validate_theory_dossier.py \
  --reading path/to/文献解读.md \
  --reception path/to/学界评价与理论应用.md \
  --case-lab path/to/理论解释案例实验室.md
```

运行项目测试：

```bash
python -m unittest discover -s tests -v
```

验证器负责检查结构和证据纪律，但不能代替对原始文献的学术核实。

## 隐私、版权与局限

- 仓库不包含用户上传的文献、私人笔记、Zotero 资料或研究档案。
- 没有再分发权利时，不得提交文献全文。
- `examples/` 全部是明确标记的合成示例，不能作为学术资料引用。
- 学界评价默认是有目的的代表性综述，不自动构成系统综述或文献计量研究。
- Zotero URI 只有在确认后才生成，不猜测 item key。
- 图中的位置、距离和箭头本身不构成证据。

## 引用

参见 [CITATION.cff](CITATION.cff)。推荐引用：`Theory-to-Case Lab, version 1.0.0, neoxyz-99, 2026`。
