# Walsh全谱、平衡与非线性度

## R — Reading

> 布尔函数的非线性度与其Walsh变换之间具有如下关系

来源QLJ2011，§1.2—1.3 书p3—5；§4.1 书p105—106 / PDF115—116。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

计算W_f(a)=Σ_x(-1)^(f(x)+a·x)，采用非归一化整数谱。由NL(f)=2^(n−1)−max|W|/2得到最近仿射距离，W(0)=0等价平衡。向量NL取全部非零输出分量的最小值。不能只检查坐标；输出掩码的线性组合可能使NL下降。与Bent卡的区别是本卡计算一般函数，不要求平坦谱。

## A1 — Application Example

合成演练：f=x1*x2，W=[2,2,2,−2]、NL1、weight1；f=x1的NL为0。

## A2 — Future Trigger

Walsh spectrum、nonlinearity、最大线性偏差、平衡性、全分量谱。

## E — Execution

先读resources/usage.md。运行通用计算命令；读walsh、nonlinearity、balanced。向量读取components中的全部2^m−1项并复核最小NL。完成标准为Parseval ΣW²=2^(2n)且NL与小维直接仿射距离一致。

## B — Boundary

归一化Walsh值不可直接代入整数公式。高NL不自动等价APN，也不是完整系统安全结论。不能把单一坐标的NL报告成向量NL。

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/runtime_metrics.py](../../resources/runtime_metrics.py)
- [resources/test_metrics.py](../../resources/test_metrics.py)
- [resources/usage.md](../../resources/usage.md)
- [resources/mm_construction.py](../../resources/mm_construction.py)
- [resources/test_mm.py](../../resources/test_mm.py)
