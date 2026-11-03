# 密码函数的安全性指标分析 · 科研技能

基于李超、屈龙江、周悦《密码函数的安全性指标分析》（科学出版社，2011），按原“Boolean-vector-research-skill生成”项目的 **cangjie-skill 2.5.0 / RIA-TV++** 流程蒸馏。

**研究初稿0.1.0：1个入口、8张能力卡、Python标准库有限表计算器。** 已进行全书OCR检索、关键页图核对、五视角候选提取、三重验证、路由编译及有限输出测试。全书复杂构造与计数仍有待审项，不称全书定理库已完成。

- [技能入口](skills/qlj-security-metrics/SKILL.md)：表示/ANF、Walsh/NL、二元PN/APN、Bent对偶、方形奇维AB、弹性、标量AI、配对乘积Bent构造。
- [精华长文](research/qlj-security-metrics/DIGEST.md) · [全书骨架](research/qlj-security-metrics/BOOK_OVERVIEW.md) · [术语](research/qlj-security-metrics/GLOSSARY.md)
- [覆盖审计](research/qlj-security-metrics/coverage-audit.md) · [待审](research/qlj-security-metrics/needs-review.md) · [验证记录](research/qlj-security-metrics/test-results.md)
- [使用和复现](docs/REPRODUCE.md) · [后续上传规范](docs/UPLOAD_WORKFLOW.md)

```powershell
python skills/qlj-security-metrics/resources/runtime_metrics.py --input examples/gold-3.json
python skills/qlj-security-metrics/resources/runtime_metrics.py --paired-bent 4
```

精确AI限n≤6；标量n≤10；向量n≤8、m≤8。仅验证给定有限表，不替代系统安全评估、全族证明或最新研究查新。书中“几乎Bent”为向量AB；向量AI三定义不混用。

原书PDF、页图及全文OCR仅在本地取证，不随仓库分发。原著版权归权利人；未新增许可证。
本项目由WEveboy提出研究目标与维护；Codex协助蒸馏、工具实现和验证。
