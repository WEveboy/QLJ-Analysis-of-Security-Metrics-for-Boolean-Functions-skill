# 案例提取与可复算演练

## 核读范围与口径

已逐张查看PDF页13—28（书p3—18）、31—38（书p21—28）、82—85（书p72—75）、115—118（书p105—108）。这些页以定义、定理和证明为主，发现如下原书演算示例。没有检索全书全部例题，不宣称案例全量覆盖。PDF页码均从1计数，正文书页+10=PDF页。

以下先列原书证据，再单列本次合成演练。原书中的数学例题属于worked_example，不是作者个人经历。所有短引文均直接核页图；公式转写使用自定纯文本记法，须结合章节上下文。

## A. 原书案例池

```yaml
- id: c01
  title: 平方映射的PN性质取决于域特征
  type: case
  example_kind: worked_example
  source_chapter: 第2章2.1，例2.1，书p23，PDF33
  source_quote: "设f(x)=x²：F_q→F_q，q=pⁿ，证明当p=2时，f(x)不是PN函数；当p>2时，f(x)是PN函数。"
  summary: |
    a≠0时，特征2给出D_a f(x)=a²，是常映射；奇特征给出D_a f(x)=2ax+a²，是域上的仿射置换。
    将导数是否平衡作为PN判据，不能漏掉定义域、值域为同一有限域以及a≠0的条件。
  bound_to: [PN导数平衡判据, 域特征检查, T05]
  outcome: 特征2非PN，奇特征PN；原书给出上述符号证明。
  tags: [case, pn, finite-field, characteristic]
- id: c02
  title: 偶数维配对乘积Bent函数
  type: case
  example_kind: worked_example
  source_chapter: 第4章4.1，例4.1及其证明，书pp106—107，PDF116—117
  source_quote: "设n=2m为任意正偶数，令f(x₁,x₂,…,x_n)=x₁x_(m+1)+x₂x_(m+2)+…+x_mx_(2m)，则f(x)是一个n元Bent函数。"
  summary: |
    将输入分成两组X₁、X₂，写f=X₁·X₂。
    对每个频率(W₁,W₂)先对X₂求和，仅X₁=W₂贡献，Walsh值为±2^m。
    这是完整的符号构造与平坦谱证明，不需要借样本外推。
  bound_to: [Bent构造, Walsh平坦谱判定, T07]
  outcome: 所有正偶数维均存在该构造，|W_f|恒为2^(n/2)。
  tags: [case, bent, construction, walsh]
- id: c03
  title: 三次单项式与函数代数次数不同
  type: case
  example_kind: worked_example
  source_chapter: 第1章1.6，书p14，PDF24
  source_quote: "如F(x)=x³为三次单项式，但当它视为F_(2ⁿ)上的函数时，按照定义，它的代数次数就是2而不是3。"
  summary: |
    该句演示单变元形式次数与布尔函数ANF次数的区别，依据前一页的指数二进制重量规则。
    精确使用须保持单变元表示的约化范围；n=1时x³作为函数约化为x，不能不加条件照抄该例。
  bound_to: [域多项式表示转ANF, 指数二进制重量, T01, T04]
  outcome: 对n≥2的x³（指数3处在原书约化范围内）代数次数为2；n=1不满足直接套用条件。
  tags: [case, algebraic-degree, representation, boundary]
- id: c04
  title: 特征2非零向量可以自正交
  type: case
  example_kind: worked_example
  source_chapter: 第1章1.7，定义1.3后，书p17，PDF27
  source_quote: "例如在F₂ⁿ中，对于v=(1,1)，(v,v)=1·1+1·1=0。"
  summary: |
    示例说明有限域内积不是正定实内积，不能用(v,v)=0推出v=0。
    原书用它衔接线性码对偶与自正交性概念，不是一个密码函数构造。
  bound_to: [有限域内积, 线性码对偶, T04]
  outcome: v非零而内积为0。
  tags: [case, finite-field, orthogonality, linear-code]
```

## B. 本次合成演练（不计作原书案例证据）

下列输入是蒸馏时设计的有限实例。2026-11-03使用Python3标准库直接枚举运行，所有数值为实际输出。未调用项目原有计算器，适合作为后续工具的独立预期值；数值核验不替代原书的全参数证明。

### s01 平方映射的有限实例（绑定c01）

群运算为模素数p加减，表按x=0,…,p−1；行按a=1,…,p−1，列按b=0,…,p−1。DDT[a,b]=#{x:f(x+a)−f(x)=b}。

| p | f(x)=x²表 | 所有非零a的DDT行 | δ |
|---|---|---|---|
| 2 | [0,1] | [0,2] | 2 |
| 3 | [0,1,1] | 每行为[1,1,1] | 1 |
| 5 | [0,1,4,4,1] | 每行为[1,1,1,1,1] | 1 |
| 7 | [0,1,4,2,2,4,1] | 每行为七个1 | 1 |

这里p=2仅为F₂→F₂；不能据此说所有二元矩形映射不存在PN（例如二元标量Bent是矩形PN）。

### s02 四变量配对乘积Bent（绑定c02）

x=(x₁x₂x₃x₄)₂升序，x₁最高位。f=x₁x₃+x₂x₄，所有加法在F₂。

- table = [0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0]
- W = [4,4,4,4,4,-4,4,-4,4,4,-4,-4,4,-4,-4,4]
- weight=6，degree=2，NL=6，所有非零导数平衡（可由Bent性质或另行枚举）。
- ANF非零掩码=[5,10]（整数位集合即二进制低位为x₄，对应x₂x₄和x₁x₃）。
- 本实例dual=f，double_dual=f；自对偶只是该实例结论，不是所有Bent都自对偶。

### s03 GF(8)立方映射（绑定c03及APN定义）

GF(8)=F₂[t]/(t³+t+1)，元素整数x的第i位是t^i系数；加法XOR，乘法按模多项式0b1011约化。F=x³表为[0,1,3,4,5,6,7,2]。

- 非零输入差分a=1,…,7各自的导数像均有4个元素，每个非零DDT计数为2，δ=2。
- 全部非零输出掩码v=1,…,7的分量deg(v·F)均为2。
- 各分量Walsh值均在{−4,0,4}，NL(F)=2。
- 本段是用书p72定义3.1/命题3.1—3.2与书p11向量NL公式进行的合成检测，不声称书pp72—75给出该立方构造。

### s04 奇偶校验的弹性阶（绑定书p7谱判据）

f=x₁+x₂+x₃，表=[0,1,1,0,1,0,0,1]；W=[0,0,0,0,0,0,0,8]。所有wt(a)≤2的谱为0，故为2阶弹性；a=7（wt=3）谱非零，所以不能称3阶弹性。该例线性且NL=0，体现单项指标不能代表全面安全。

### s05 二变量AND的表示与谱（绑定书p3式1.5—1.6、p7的NL公式）

f=x₁x₂，table=[0,0,0,1]，Möbius ANF=[0,0,0,1]，W=[2,2,2,−2]，NL=1。它是最小偶数维Bent但不平衡。

## C. 本次实际运行的核心枚举方法

计算使用如下定义（可以直接独立复算上述结果）；GF(8)乘法先移位异或并以11约化。

```python
parity = lambda x: x.bit_count() % 2

def walsh(table):
    return [sum((-1)**(table[x] ^ parity(a & x))
                for x in range(len(table)))
            for a in range(len(table))]

def anf(table):
    result = table[:]
    for bit in range(len(table).bit_length()-1):
        for x in range(len(table)):
            if (x >> bit) & 1:
                result[x] ^= result[x ^ (1 << bit)]
    return result

def gf8_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11
    return result
```

## D. 缺口和可用性结论

- c01/c02是完整原书worked_example，可直接支持A1；有限数值s01/s02已复算。
- c03需要将指数约化条件写入能力卡，尤其不能对n=1照抄“次数2”。该边界是本次核查，不冒称作者在该段明确警告。
- c04是参考型例证，不晋级独立密码函数能力。
- 其他所查页没有发现明确编号的数值例题；没有将定理、证明和合成演练冒充书中实例。
- 未核查第二章其余应用例题及后五章全部例题；应在覆盖审计登记此缺口。
