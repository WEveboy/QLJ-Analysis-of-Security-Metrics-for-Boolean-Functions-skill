# 三重验证与晋级评审

V1按候选记录核读页图；V2用新输入有限复算；V3为可检查的规格统一与条件防遗漏，不宣称模型能力显著提高。

| canonical ID | V1 来源 | V2 实算 | V3 收益 | 去向 |
|---|---|---|---|---|
| cap.qlj.representation | §1.1 书p1—3 / PDF11—13 | test_metrics.py及阶段4输出 | 真值表、ANF与位序核验口径一致 | single路由卡 |
| cap.qlj.walsh-nonlinearity | §1.2—1.3 书p3—5；§4.1 书p105—106 / PDF115—116 | test_metrics.py及阶段4输出 | Walsh全谱、平衡与非线性度口径一致 | single路由卡 |
| cap.qlj.binary-differential | §1.5 书p10—11；§2.1 书p21—24；§3.1 书p72—75 / PDF82—85 | test_metrics.py及阶段4输出 | 二元差分表、PN与方形APN检测口径一致 | single路由卡 |
| cap.qlj.bent-dual | §4.1 定义4.2、定理4.1/4.5，书p106—108 / PDF116—118 | test_metrics.py及阶段4输出 | Bent检测与对偶恢复口径一致 | single路由卡 |
| cap.qlj.square-almost-bent | §5.1 定义5.3及SCV界讨论，书p130—132 / PDF140—142 | test_metrics.py及阶段4输出 | 方形奇维Almost Bent检测口径一致 | single路由卡 |
| cap.qlj.resiliency | §6.1 定义6.1—6.2、定理6.2—6.3，书p148—150 / PDF158—160 | test_metrics.py及阶段4输出 | 相关免疫与弹性谱检测口径一致 | single路由卡 |
| cap.qlj.scalar-ai | §7.1 定义7.1、定理7.1，书p202—205 / PDF212—215 | test_metrics.py及阶段4输出 | 标量代数免疫度与非零零化子证书口径一致 | single路由卡 |
| cap.qlj.paired-bent | §4.1 例4.1及证明，书p106—107 / PDF116—117 | test_metrics.py及阶段4输出 | 配对乘积Bent构造及复算口径一致 | single路由卡 |

阶段1.6：8项均有独立意图和契约，可复用且可评测；共享表示和计算器，independent_run=false，因此全部router，无独立晋级。
候选池并集去重，五视角不是五个独立来源。sources为唯一原书；短引用不能代替完整条件。
