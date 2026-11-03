# 二元差分表、PN与方形APN检测

## R — Reading

> 对每一个非零元素a，函数Da f(x)=f(x+a)−f(x)是平衡的

来源QLJ2011，§1.5 书p10—11；§2.1 书p21—24；§3.1 书p72—75 / PDF82—85。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

先明确群运算。本执行器只支持二元向量空间，输入差分用XOR。DDT(a,b)=#{x:F(x⊕a)⊕F(x)=b}；δ在a≠0上取最大。一般二元n→m PN要求n≥m且δ=2^(n−m)。二元方形APN要求δ=2。方形二元PN不可能，因为导数解成对出现；这不能否定矩形PN或标量Bent。奇特征平方映射的PN结论须使用域加减而非XOR。

## A1 — Application Example

合成演练：GF(8)模t³+t+1的x³表[0,1,3,4,5,6,7,2]，δ2，为方形二元APN。奇特征平方原书例2.1仅作参考，程序不执行。

## A2 — Future Trigger

DDT、差分均匀度、differential uniformity、PN、APN、S-box；几乎Bent另读AB卡。

## E — Execution

先读resources/usage.md。输入n,m≥2及完整表，运行通用命令；输出完整DDT、δ及最坏(a,b)见证、binary_pn与binary_square_apn。检查每行和2^n、a≠0各计数偶数。m=1时通用程序走标量分支，PN用Bent等价判据；不输出不存在的DDT字段。

## B — Boundary

n,m≤8。APN字段仅n=m才给布尔值，非方形给null。原书一般素特征定义超出本二元执行器。未知构造参数不补猜。DDT好不保证置换，也不完成等价分类。
