# 配对乘积Bent构造及复算

## R — Reading

> 设n=2m为任意正偶数

来源QLJ2011，§4.1 例4.1及证明，书p106—107 / PDF116—117。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

按书中例4.1把变量分成两半，f=Σ_(i=1)^h x_i*x_(h+i)，n=2h。对第二半变量求字符和，仅一项保留，从而Walsh恒幅2^h。这是已有符号构造；小维全算用于检查实现，不代替原书证明。先生成完整表，再用Bent卡独立判定。程序位序采用x1最高位。

## A1 — Application Example

原书数学例题4.1的n=4实例：表[0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0]，weight6、NL6。

## A2 — Future Trigger

构造Bent、paired product、例4.1、生成偶数维Bent；已有表的判定用bent-dual卡。

## E — Execution

先读resources/usage.md。运行python resources/runtime_metrics.py --paired-bent 4 --out new-result.json；输出input完整表和result。完成标准：n正偶数、表长度正确、result.bent=true、NL=2^(n−1)−2^(n/2−1)。

## B — Boundary

只实现该构造，2≤n≤10且偶数。不能声称覆盖MM/PS/Dillon全族、计数或等价类。奇数n拒绝。相邻配对是变量置换后的同构写法，不能冒充本例印刷式。
