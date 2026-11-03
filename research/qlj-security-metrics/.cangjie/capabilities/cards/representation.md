# 真值表、ANF与位序核验

## R — Reading

> 这个向量称为布尔函数的真值表。

来源QLJ2011，§1.1 书p1—3 / PDF11—13。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

真值表不是一串无索引的比特。输入x按整数升序，x1为最高位，固定输入维数n。ANF是F2上平方自由多项式，掩码的置位表示参与乘积的变量。对子集做Möbius变换得到系数，再变换一次恢复原表。代数次数是最大非零单项式重量；本实现沿书p2将零函数次数记0。向量表值是输出位编码，分量用二元点积解释。

## A1 — Application Example

合成演练：n=2，表[0,0,0,1]对应x1*x2，非零ANF掩码[3]，次数2。

## A2 — Future Trigger

真值表转ANF、位序、代数次数、representation、Möbius transform；仅解释术语时先读词典。

## E — Execution

先读resources/usage.md。输入n,m,table；运行resources/runtime_metrics.py --input spec.json。验证长度2^n和值域后输出anf_masks、degree及输入哈希。标量可逐项评价ANF并与原表相等。向量逐非零分量输出，勿把分量次数当单变元形式次数。

## B — Boundary

n≤10；向量n≤8,m≤8。布尔值、越界值、错误长度拒绝。域多项式输入需先给域模型并另转换成表；本工具不解析任意ANF字符串。
