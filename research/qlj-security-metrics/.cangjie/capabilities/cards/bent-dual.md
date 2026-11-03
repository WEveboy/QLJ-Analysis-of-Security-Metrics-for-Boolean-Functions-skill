# Bent检测与对偶恢复

## R — Reading

> 则其对偶函数也一定是Bent函数

来源QLJ2011，§4.1 定义4.2、定理4.1/4.5，书p106—108 / PDF116—118。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

标量Bent要求n为正偶数且所有频率W均为±2^(n/2)。通过后，以Walsh符号恢复dual：正置0、负置1，再计算对偶之对偶检查回到原函数。Bent的零频不为0，所以不平衡。向量Bent要求所有非零分量Bent；参数门为n偶且m≤n/2。对偶只对已验证标量Bent输出。

## A1 — Application Example

合成演练：x1*x3+x2*x4四变量函数NL6、weight6；对偶仍为自身。自对偶仅为该例结论。

## A2 — Future Trigger

Bent判定、bent dual、平坦谱、向量Bent；请求生成函数转paired-bent卡。

## E — Execution

先读resources/usage.md。运行通用命令，读bent和可选dual_table；只在bent=true时解释对偶。对输出表重算以核验双对偶。向量读vector_bent和全部components。

## B — Boundary

奇维不输出Bent对偶；零谱符号不能强作对偶。不要把AB、标量semi-bent、平衡函数当Bent。构造不是本卡职责。
