---
name: qlj-security-metrics
description: |
  基于李超、屈龙江、周悦《密码函数的安全性指标分析》的科研能力：真值表与ANF、Walsh非线性度、二元差分PN/APN、Bent及对偶、方形奇维AB、相关免疫与弹性、标量AI、配对乘积Bent。用于有限候选复算和条件核对；不执行全族分类或密码系统安全证明。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.qlj-security-metrics
  cangjie.capability-count: 8
  cangjie.entrypoint-count: 1
---
# 密码函数的安全性指标分析 — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 通用代码工程、任意书籍自动蒸馏、无来源的新颖性和系统安全证明。

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 先读resources/usage.md与所需能力卡；输入必须有维数、完整表及位序。
2. 区分B原书事实、D独立实现/合成演练、H未证研究方向；不把有限验证称为全族证明。
3. 向量性质检查全部非零分量；几乎Bent指向量AB；PN/APN保留域特征和维数条件。
4. 本版是限定范围研究初稿：全书OCR检索与关键页核图完成，待审构造见overview，未逐一定理核验。
5. runtime为Python标准库；精确AI限n≤6。not_computed与失败不同，null与0不同。
6. 参考来源为2011年专著；有关今天的最优记录与开放问题必须另外核查。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 真值表、ANF与位序核验；真值表转ANF、位序、代数次数、representation、Möbius transform；仅解释术语时先读词典。 | references/capabilities/representation.md | — |
| Walsh全谱、平衡与非线性度；Walsh spectrum、nonlinearity、最大线性偏差、平衡性、全分量谱。 | references/capabilities/walsh-nonlinearity.md | references/capabilities/representation.md |
| 二元差分表、PN与方形APN检测；DDT、差分均匀度、differential uniformity、PN、APN、S-box；几乎Bent另读AB卡。 | references/capabilities/binary-differential.md | references/capabilities/representation.md |
| Bent检测与对偶恢复；Bent判定、bent dual、平坦谱、向量Bent；请求生成函数转paired-bent卡。 | references/capabilities/bent-dual.md | references/capabilities/representation.md、references/capabilities/walsh-nonlinearity.md |
| 方形奇维Almost Bent检测；几乎Bent、Almost Bent、AB、SCV、奇数维向量最优NL；标量semi-bent只作词典区分。 | references/capabilities/square-almost-bent.md | references/capabilities/representation.md、references/capabilities/walsh-nonlinearity.md |
| 相关免疫与弹性谱检测；相关免疫、correlation immunity、resiliency、弹性阶、均匀投影；构造与计数另属待审参考。 | references/capabilities/resiliency.md | references/capabilities/representation.md、references/capabilities/walsh-nonlinearity.md |
| 标量代数免疫度与非零零化子证书；algebraic immunity、AI、MAI、零化子、annihilator；请求向量AI时先辨三定义，当前不计算。 | references/capabilities/scalar-ai.md | references/capabilities/representation.md |
| 配对乘积Bent构造及复算；构造Bent、paired product、例4.1、生成偶数维Bent；已有表的判定用bent-dual卡。 | references/capabilities/paired-bent.md | references/capabilities/representation.md、references/capabilities/bent-dual.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 关键域模型或输入规格不足时先补信息；超出预算明确未算。
- 未核参数构造不进入已证明方法；向量AI先区分三定义，当前只保留参考。
