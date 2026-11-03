# 标量代数免疫度与非零零化子证书

## R — Reading

> 使得fg=0或(f+1)g=0成立的非零布尔函数g的最小代数次数

来源QLJ2011，§7.1 定义7.1、定理7.1，书p202—205 / PDF212—215。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

AI寻找f或f+1的非零零化子的最小次数。按d升序构造次数≤d单项式，在目标支持集上建立GF(2)齐次系统。任一侧出现非零核向量即可；零向量不能作证。较低次数两侧均满列秩，给最小性的有限消元依据。MAI指AI=ceil(n/2)，仅为该单项指标最优。常函数AI0。实现算法独立编写，不归因为原书现成代码。

## A1 — Application Example

合成演练：f=x1*x2的AI1，g=1+x1使fg=0；n=4配对乘积Bent的AI2。

## A2 — Future Trigger

algebraic immunity、AI、MAI、零化子、annihilator；请求向量AI时先辨三定义，当前不计算。

## E — Execution

先读resources/usage.md。输入添加ai:true；运行通用命令，读algebraic_immunity的value、annihilates、monomial_masks、witness_table。逐点核g非零、次数符合并且对应乘积全0。n>6输出not_computed，不将缺结果写成0。

## B — Boundary

精确AI限n≤6。向量分量可逐项算标量AI，但不冒充已实现基本或图形向量AI，也不自动汇总三定义。MAI不保证快速代数攻击安全；本工具不计算FAI。
