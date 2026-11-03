# 相关免疫与弹性谱检测

## R — Reading

> 若f(x)既是m阶相关免疫函数又是平衡函数，则称f(x)是m阶弹性函数

来源QLJ2011，§6.1 定义6.1—6.2、定理6.2—6.3，书p148—150 / PDF158—160。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

在输入独立均匀条件下，CI阶t只要求1≤wt(a)≤t的谱为零；弹性另外要求W(0)=0。本实现返回最大满足阶，0阶弹性表示仅平衡。非平衡函数resiliency_order=null，而不是误报0。常函数CI可到n，但非弹性。向量弹性逐全部非零分量检查，取最小阶；只检查坐标会漏掉常分量。

## A1 — Application Example

合成演练：四变量奇偶和为3阶弹性。表[0,0,3,3]两个坐标均平衡，但第三个分量恒零，向量不平衡。

## A2 — Future Trigger

相关免疫、correlation immunity、resiliency、弹性阶、均匀投影；构造与计数另属待审参考。

## E — Execution

先读resources/usage.md。运行通用命令；标量读取correlation_immunity_order、balanced、resiliency_order。要检查要求阶t时比较最大阶≥t，null判失败。向量需验证全部分量，并报告最坏分量。

## B — Boundary

相关免疫不代表在有偏相关输入下仍独立。次数界只是必要条件。t=n−1边界不能机械使用常见n−t−1界。向量AI与此无关。
