# Maiorana–McFarland Bent构造与谱证书

## R — Reading

> 其中π是F₂^(n/2)上的置换，g是任意n/2元布尔函数，·表示F₂^(n/2)中向量的内积。（上下标规范排写）

来源QLJ2011，§4.3 定义4.5、式(4.9)、定理4.9，书p113 / PDF123。引文为核图短摘；公式在I中规范转写。

## I — Interpretation

设n=2h，x和y均为h位向量，f(x,y)=x·π(y)+g(y)。π必须是整个半维空间的置换，g任意。对x求字符和，只在π(y)=a时非零，因此W_f(a,b)=2^h(-1)^(b·π^(-1)(a)+g(π^(-1)(a)))。本卡把原书符号证明变成给定有限实例的证书：保存逆置换、预测谱，再与计算器全谱比较。配对乘积是π为恒等且g=0的特例。

## A1 — Application Example

合成演练：h=2，π=[2,0,3,1]，g=[0,1,1,0]，构造16项表；全谱幅值4，NL6。穷举h=2的24个置换与16个g共384例均经直接字符和核验。

## A2 — Future Trigger

Maiorana–McFarland、M-M、MM Bent、任意半维置换构造Bent；固定配对乘积使用paired-bent卡，已有表判断用bent-dual卡。

## E — Execution

先读resources/usage.md。运行python resources/mm_construction.py --input mm.json --out new-mm-result.json。输入h、长度2^h的整数置换pi与同长度0/1表g。坐标z=(x<<h)|y，前h位为x。输出function完整表、analysis、inverse_pi及predicted_walsh；matched必须为true。完成后可将function另存JSON交通用计算器复算。

## B — Boundary

限定1≤h≤5，n≤10；重复或越界pi、布尔值冒充整数、错误g长度均拒绝。非置换π不满足本构造定理，拒绝不能被解释为所有变体函数都非Bent。并未实现Dillon/PS/间接构造或计数分类。
