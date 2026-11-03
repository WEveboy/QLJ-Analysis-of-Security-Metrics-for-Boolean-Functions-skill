# 方形奇维Almost Bent检测

## R — Reading

> 那么就称F为几乎Bent(Almost Bent)函数，简称为AB函数

来源QLJ2011，§5.1 定义5.3及SCV界讨论，书p130—132 / PDF140—142。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

本书几乎Bent是向量Almost Bent。限定为方形奇数n=m时，非线性度最优值为2^(n−1)−2^((n−1)/2)，对应全部非零分量的Walsh谱落在{0,±2^((n+1)/2)}。必须遍历所有分量，而不是某一坐标三值谱。与APN分别计算；不能用APN一项冒充AB判定。一般(n,m)的SCV界不在本程序执行合同内。

## A1 — Application Example

合成演练：GF(8)立方表的全部非零分量谱为0/±4，NL2，square_almost_bent=true。

## A2 — Future Trigger

几乎Bent、Almost Bent、AB、SCV、奇数维向量最优NL；标量semi-bent只作词典区分。

## E — Execution

先读resources/usage.md。输入n=m奇数且m≥2的表，运行通用命令，读取square_almost_bent与全部分量谱。非方形字段null，方形偶维该受限判定返回false并在解释中说明只适用奇维合同。

## B — Boundary

该实现不覆盖原书n=m+1的(2,1)特例，m=1走标量分支也不提供本字段。未实现一般SCV界计算。不得将程序合同当成本书AB定义的全部范围。
