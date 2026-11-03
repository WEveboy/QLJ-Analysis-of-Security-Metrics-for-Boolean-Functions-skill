# 框架/流程提取候选（cangjie-skill 2.5.0）

## 核读与来源

一手来源：李超、屈龙江、周悦《密码函数的安全性指标分析》，科学出版社，2011。下文“书p”是印刷页，“PDF”是1起始物理页，关系为PDF=书p+10。
实际逐张核读：PDF13—28、31—38、82—85、107—110，共32张页图。另对全286页中文OCR做机制关键词自动扫描，并阅读PDF29—286各页命中“构造/判定/方法/等价/定理/计数/当且仅当”的首3条上下文。此为覆盖预筛，**不是全文逐句核读**；OCR公式不足以激活新构造。全量扫描剩余段落与关键定理核验仍有缺口。
引用只保留短句，其余为重述。候选未完成V2实算前均不自称verified。

```yaml
- id: f01
  title: 真值表与ANF双向转换
  type: procedure
  source_chapter: "§1.1，书p3，命题1.1/式1.5；PDF13"
  source_quote: "布尔函数 f 可以看成其代数正规型系数的二进制 Möbius 变换，反之也成立。"
  summary: "对每个变量子集I，在F2中累加支撑包含于I的真值以得到a_I；ANF求值反向按相同包含关系累加。位序必须先固定。可用变换两次恢复原表检验实现。"
  inputs: "n、长度2^n的0/1表、明确输入位序"
  outputs: "ANF系数表、代数次数、往返一致性"
  steps: [固定输入点顺序, 对子集关系执行模2累加, 反变换逐点核对]
  missing_conditions: "用户位序未知不能猜。快速子集算法是独立工程实现，应标D。"
  tags: [representation, mobius, procedure]

- id: f02
  title: Walsh计算与非线性度交叉核验
  type: calculation
  source_chapter: "§1.2—1.3，书p3—7；PDF13—17；命题1.2、1.3"
  source_quote: "布尔函数的两种 Walsh 谱可以相互唯一确定。"
  summary: "先确认使用循环Walsh谱W而非线性谱S。由符号真值表求W，检验Parseval及W(0)=2^n−2wt(f)，再由最大绝对谱求NL。小n时枚举全部仿射函数距离作独立算法核对。"
  inputs: "固定索引的完整布尔表"
  outputs: "完整谱、重量、平衡性、NL、Parseval检查；可附最近仿射函数"
  steps: [固定谱定义, 求全部W值, 检查平方和2^(2n), 求NL并核对]
  missing_conditions: "快速Walsh变换与枚举最近仿射函数属D实现。"
  tags: [walsh, nonlinearity, validation]

- id: f03
  title: 向量性质通过全部非零组件核验
  type: framework
  source_chapter: "§1.4—1.5，书p9—12；PDF19—22；定理1.1"
  source_quote: "每个分量函数都平衡，并不意味着向量值函数是平衡函数。"
  summary: "坐标只是v·F中v为单位向量的少数情形。对所有v≠0逐个计算组件表，平衡性要求全部平衡，向量NL取全部组件NL最小值，一致代数次数取全部组件次数最小值；通常代数次数则取坐标最大值。"
  inputs: "n,m、完整输出整数表、输出坐标约定"
  outputs: "全部组件指标、最坏组件见证、通常/一致次数分别列明"
  steps: [枚举所有非零v, 建组件v·F, 核验并保留最坏见证]
  missing_conditions: "m大时指数增长，必须限制预算。不能从坐标测试冒充全组件结论。"
  tags: [vectorial, components, contract]

- id: f04
  title: 由完整差分表判定PN与APN并先过域特征门
  type: procedure
  source_chapter: "§1.5书p11；§2.1书p21—23，定义2.1—2.3及定理2.2；§3.1书p72，定义3.1/命题3.1—3.2；PDF21、31—33、82"
  source_quote: "会经常通过检验 D_a f(x) 是否为平衡函数来讨论函数 f 的完全非线性性。"
  summary: "一般有限交换群中非零a差分行全部均匀当且仅当PN。二元n→m使用XOR差分，PN目标δ=2^(n−m)；方形二元F2^n→F2^n因解成对不存在δ=1的PN，但n→m的二元PN并未被这一结论排除。方形二元APN目标δ=2；奇特征也可定义APN为δ=2，但这时只是次优。"
  inputs: "域/群模型、全表、输入输出空间；二元工具限F2^n→F2^m"
  outputs: "完整DDT或计数摘要、δ、达峰(a,b)、PN/APN及适用性"
  steps: [明确群运算与维数, 遍历a≠0及x计数差分, 逐行核验总数, 按对应类型目标判定]
  missing_conditions: "仅用XOR的二元工具不能计算奇素数域；APN标签默认只给n=m，推广须另声明。"
  tags: [differential, pn, apn, characteristic]

- id: f05
  title: 单变量有限域多项式转换与次数区分
  type: procedure
  source_chapter: "§1.6，书p12—15；PDF22—25，式1.10"
  source_quote: "f(x)=x³ 为三次单项式，但当它视为 F_(2^n) 上的函数时，按照定义，它的代数次数就是2而不是3。"
  summary: "固定不可约多项式和基后，求完整点值再转坐标ANF；约化单变量表示的非零幂次二进制重量最大值给布尔代数次数。不能把普通多项式次数直接当作布尔函数代数次数。"
  inputs: "n、不可约模多项式、基、系数与幂次、约化规则"
  outputs: "固定模型真值表、坐标ANF、代数次数及域模型"
  steps: [固定有限域模型, 求点值, 转ANF并对照二进制幂次重量]
  missing_conditions: "相对迹表示要求m|n，旋分陪集系数关系需另实现；本候选不宣称完成一般迹式自动归约。"
  tags: [finite-field, degree, trace]

- id: f06
  title: RM评价码作为函数表示的核验桥
  type: framework
  source_chapter: "§1.7，书p15—18；PDF25—28，定义1.4"
  source_quote: "次数≤r 的所有单项式所对应的码字形成线性码 RM(r,m) 的一组 F2 基。"
  summary: "将每个次数≤r的平方自由单项式按固定点序评价为一行，所得行空间即RM(r,m)。应区分码长2^m与变量数m，维数为Σ(i=0..r)binom(m,i)。可在小维数枚举码字重量验证。"
  inputs: "变量数m、阶r、点顺序"
  outputs: "评价生成矩阵、秩和维数检查"
  steps: [枚举单项式, 评价矩阵, 求F2秩并对照组合维数]
  missing_conditions: "高阶非线性度/精确最近码字求解未因此自动实现。书p19定理1.3只OCR预筛，本候选不引用其未图核的最小距离公式。"
  tags: [reed-muller, evaluation, rank]

- id: f07
  title: PN原像分布必要条件预筛
  type: calculation
  source_chapter: "§2.2，书p27—28；PDF37—38，定理2.5/式2.1"
  source_quote: "根据原像分布特征，可以发现在很多情况下，m|n 并不是 PN 函数存在的充分条件。"
  summary: "以N=|A|、M=|B|避免与维数混淆，记k_z为原像数。PN必要条件是Σk_z=N、对b≠0有Σk_z k_(z+b)=N(N−1)/M、Σk_z²=(N²+NM−N)/M。给定整数分布不满足任一条件即可否决，满足只代表未被必要条件排除。"
  inputs: "明确群B、N、M、各k_z"
  outputs: "三组必要条件检查及失败项"
  steps: [检查非负整数与总和, 逐个非零b检验移位内积, 检验平方和]
  missing_conditions: "必须保留B的群结构；相同M的不同群移位约束不等同；满足条件不证明函数存在。"
  tags: [pn, preimage, necessary-condition]

- id: f08
  title: DO型PN以线性化差分核判定
  type: procedure
  source_chapter: "§2.1，书p25—27；PDF35—37，定理2.4"
  source_quote: "差函数 D_a f(x)=f(x+a)−f(x)=L_a(x)+c_a。"
  summary: "奇特征q=p^n、deg(f)<q前提下，DO型PN等价于每个非零a的差分均为线性化置换多项式加常数。可将L_a视为Fp线性映射，以零核/满秩核验置换性。"
  inputs: "奇特征有限域模型、DO形系数或完整表"
  outputs: "各差分线性部分秩、非平凡核见证或PN结论"
  steps: [核对奇特征与DO形, 构建L_a, 检查各a零核]
  missing_conditions: "二元XOR工具不实现本候选；奇素域引擎和全族证明需另补；目前宜reference/needs_review。"
  tags: [do, pn, linearized-polynomial]

- id: f09
  title: APN差分检测与组件自相关平方和互证
  type: calculation
  source_chapter: "§3.1，书p72—75；PDF82—85；定理3.2—3.3，式3.1—3.4"
  source_quote: "利用组件函数，可以判定一个函数的 APN 性质。"
  summary: "二元方形F，对每个a≠0枚举全部λ（包括0组件），令AC_λ(a)=Σx(−1)^(λ·(F(x+a)+F(x)))。APN当且仅当每个a的Σλ AC_λ(a)²=2^(2n+1)。可与DDT≤2做不同计算路线交叉核对。"
  inputs: "n与完整n→n二元表"
  outputs: "每个非零a的平方和、APN布尔值、首个失败方向"
  steps: [算全部组件自相关, 对λ平方求和, 与目标精确整数比较并对照DDT]
  missing_conditions: "λ=0不可漏；全a核验不可只采样；复杂度需预算。"
  tags: [apn, autocorrelation, cross-validation]

- id: f10
  title: CCZ不变量预筛与证书分离
  type: framework
  source_chapter: "§3.1书p73—74；§3.4书p97—100；PDF83—84、107—110"
  source_quote: "如果能够计算出两个 APN 函数的扩展 Walsh 谱，并且发现它们的扩展 Walsh 谱不同，就可以断言这两个 APN 函数是 CCZ 不等价的。"
  summary: "先比较含重数的扩展绝对Walsh谱等必要不变量。不相同可否决等价，相同只能未定。若用户给出图空间的可逆仿射变换，逐点验证图映射才可正向确认等价；该验证实现属于D。代数次数不是CCZ不变量，不能拿它否决CCZ。"
  inputs: "两完整方形函数表；可选给定可逆图变换"
  outputs: "proven_not_equivalent / inconclusive / verified_certificate与见证"
  steps: [按同一约定求谱多重集, 比较必要不变量, 有证书时验证全图]
  missing_conditions: "不搜索未知变换，不做完整分类。PN情形EA=CCZ的定理2.17只OCR扫描，不扩展到APN。"
  tags: [ccz, invariant, certificate]

- id: f11
  title: APN与几乎Bent任务路由分离
  type: framework
  source_chapter: "§3.1书p72；第5章PDF138—155（本轮仅OCR机制预筛，未逐式图核）"
  source_quote: "在特征为2的有限域上，需要考虑差分均匀度等于2的函数。"
  summary: "APN依据差分定义检测；几乎Bent依据其专属谱定义及维数条件检测。目录和OCR显示§5.1—5.3有向量Bent、AB及编码刻画，不能仅凭APN通过便给AB标签。"
  inputs: "函数表、n,m、请求的是APN还是AB"
  outputs: "分开报告差分与AB适用性；AB未图核时标needs_review"
  steps: [先APN差分检测, 再核对第5章完整AB条件, 分开输出]
  missing_conditions: "第5章关键定理仍需页图核验，不能凭本候选激活AB计算卡。"
  tags: [apn, ab, routing, needs-review]
```

## 全书机制扫描后新增待审入口（不激活）

- PDF54—60（书44—50）：PN幂/多项式构造；表及定理2.10—2.14参数需图核，不能从OCR抄指数。
- PDF67—78（书57—68）：PN→线性码权分布、覆盖结构、常复合码；输入码构造/长度/秩与所有假设尚未逐图核验，映射为reference。
- PDF91—106（书81—96）：Gold/Inverse/Welch/Kasami及二项/多项式APN构造；OCR识别到直接差分与置换多项式两条证明路线，具体参数待图核。
- PDF123—134（书113—124）：MM、PS、Dillon及间接Bent构造和计数。各构造的置换、子空间相交和对偶条件必须图核后独立成卡。
- PDF167—185（书157—175）：弹性函数直接/递归、级联/直和构造；多指标同时约束与参数更新不可省略。
- PDF186—205（书176—195）：弹性计数与向量弹性构造，涉及正交阵、线性码和无线性结构；当前保留参考，不用未核参数执行。
- PDF221—242（书211—232）：MAI的支撑包含、平面、交换基、有限域和其他构造。识别出“零化子存在→线性方程非零解→矩阵不满秩”的可执行机制；需与原书矩阵行列约定和f/f+1两支核对。
- PDF245—274（书235—264）：对称MAI，特别定理7.25给测试算法；Lucas条件/重量支持集合尚未图核，不给通用最优性断言。
- PDF275—280（书265—270）：向量AI三种定义及关系，不能将最小组件AI称为三种定义的共同结果。

## 建议晋级为单入口内原子能力卡

优先 f01表示、f02标量谱、f03全组件、f04差分PN/APN、f05有限域模型、f07PN原像必要条件、f09 APN平方和、f10等价预筛。f06可做RM参考或小维矩阵能力。f08依赖奇素域引擎暂不激活，f11待第5章图核。

V2建议小维演练：f01全部2元布尔表往返；f02与枚举仿射距离比较；f03取F(x)=(x1,x1)示范坐标平衡但整体不平衡；f04给n=2,m=1的x1x2为二元PN且不平衡，给GF(8) x³为方形APN；f09同表比较DDT与平方和；f10相同谱返回未定，不能宣布等价。均为合成演练，不冒充书中例题。
