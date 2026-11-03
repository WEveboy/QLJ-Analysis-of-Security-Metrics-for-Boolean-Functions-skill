# 术语提取候选（第5视角）

来源：李超、屈龙江、周悦《密码函数的安全性指标分析》（2011）。定位采用印刷书页，PDF页=书页+10。

检索范围：286页OCR逐页扫描定义、术语、章节标题及等价/计数锚点，未把OCR公式视为正确原文。回图核查PDF页13、14、20、21、22、24、28、31、32、62、63、82、86、132、166、189、268、275、276；其余指标核心证据结合本项目frameworks/principles/cases提取记录。该范围属于全章词汇扫描+关键定义回图，不代表全书逐定理证明复核。原文短引与重写释义分字段保存，符号采用可读转写。

全部术语为reference，不自动晋级active能力。章节的历史研究状态仅作2011年资料，不宣称今日仍开放或最优。

```yaml
- id: g01
  term: 布尔函数、向量值函数与分量
  type: term
  source_chapter: 第1章§1.1、§1.4，书pp1、8—10；第3章定义3.2，书p72
  author_definition: 原文短引：“则称f_λ(x)为F的组件函数。”
  definition_paraphrase: F₂ⁿ→F₂是布尔函数，F₂ⁿ→F₂ᵐ是(n,m)向量值函数。坐标分量为f_i，非零输出掩码v给出的v·F遍历全部非零线性组合；有限域表示下用Tr(λF(x))表达组件。
  key_distinction: 任一坐标好不推出全部非零组合好；坐标与一般组件不能混称。
  why_it_matters: 固定v并穷尽其非零值，避免向量指标只验m个坐标。
  tags:
  - term
  - Boolean
  decision: reference
- id: g02
  term: 真值表与位序
  type: term
  source_chapter: 第1章§1.1，书p1
  author_definition: 无逐字引文；下列definition_paraphrase为依原书定义的转写释义
  definition_paraphrase: 给输入向量排定顺序后，按序列出函数值。原书常用(x₁…x_n)₂递增，x₁最高位、x_n最低位。
  key_distinction: 位序是表示约定；变位序会改变掩码标签，未必改变与坐标无关的指标。
  why_it_matters: 保证表、ANF掩码和Walsh频率可互相回查。
  tags:
  - term
  - truth table
  decision: reference
- id: g03
  term: 代数正规型与Möbius变换
  type: term
  source_chapter: 第1章§1.1—1.2，书pp2—3，命题1.1、式1.5
  author_definition: 原文短引：“代数正规型系数的二进制Möbius变换，反之也成立”
  definition_paraphrase: 在F₂上每个变量指数至多1的唯一多项式表示；系数与真值表由二进制Möbius变换相互恢复。
  key_distinction: ANF加法是模2，不是整数多项式加法；零函数次数依原书约定为0。
  why_it_matters: 让次数与零化子证书基于同一表示。
  tags:
  - term
  - ANF
  decision: reference
- id: g04
  term: 代数次数与一致代数次数
  type: term
  source_chapter: 第1章§1.5，书pp10—11
  author_definition: 原文短引：“则称Deg F为F的一致代数次数。”
  definition_paraphrase: 标量次数是ANF中非零项的最大变量数；向量deg F是最大坐标次数。原书Deg F=min_(v≠0)deg(v·F)，称一致代数次数。
  key_distinction: deg的最大值与Deg的最小值是不同指标；域多项式的形式次数也不是布尔次数。
  why_it_matters: 避免高次坐标掩盖低次线性组合。
  tags:
  - term
  - deg F
  decision: reference
- id: g05
  term: 循环Walsh谱与线性Walsh谱
  type: term
  source_chapter: 第1章§1.2，书pp3—4，式1.6—1.7
  author_definition: 原文短引：“以后不另加说明的话，布尔函数的Walsh谱均是指由式(1.6)定义的循环Walsh谱”
  definition_paraphrase: 默认W_f(a)=Σ_x(−1)^(f(x)+a·x)，为原书循环Walsh谱；另以S_f(a)=Σ_x f(x)(−1)^(a·x)称线性Walsh谱。a≠0时W=−2S；a=0时W=2ⁿ−2S。
  key_distinction: 原书“循环”并非把输入索引改成模2ⁿ循环移位；两种谱在零频关系不同。
  why_it_matters: 固定非归一化整数W，防止NL公式误差2倍或误用零频。
  tags:
  - term
  - Walsh spectrum
  decision: reference
- id: g06
  term: 平衡函数
  type: term
  source_chapter: 第1章§1.1、§1.5，书pp1、9—10，定理1.1
  author_definition: 原文短引：“反过来，每一个分量函数都平衡，并不意味着向量值函数是平衡函数。”
  definition_paraphrase: 标量两值各出现2^(n−1)次；向量每个输出值的原像大小为2^(n−m)。向量平衡等价于每个非零v的v·F平衡。
  key_distinction: 向量所有坐标平衡只是必要条件；导数平衡与原函数平衡是两件事。
  why_it_matters: 把W_f(0)=0与全分量条件接通。
  tags:
  - term
  - balanced function
  decision: reference
- id: g07
  term: 非线性度
  type: term
  source_chapter: 第1章§1.3、§1.5，书pp7、11；第4章定义4.1，书p105
  author_definition: 原文短引：“向量值函数的非线性度等于其分量函数的任意非零线性组合的非线性度的最小值。”
  definition_paraphrase: 标量NL为到全体仿射函数的最小Hamming距离，等于2^(n−1)−max|W|/2；向量NL为非零组件NL的最小值。
  key_distinction: 不是代数次数，也不是只到线性齐次函数的距离。
  why_it_matters: 让最坏逼近而非平均逼近决定报告。
  tags:
  - term
  - nonlinearity
  decision: reference
- id: g08
  term: 差函数、DDT与差分均匀度
  type: term
  source_chapter: 第1章§1.5，书p11；第2章定义2.1，书p21
  author_definition: 原文短引：“则称δ_f为函数f的差分均匀度。”
  definition_paraphrase: 一般有限交换群中D_aF(x)=F(x+a)−F(x)；DDT(a,b)逐项计解数；δ取全部a≠0、全部b的最大计数。二元空间加减都为XOR。DDT名称为本工具工程记法。
  key_distinction: 整数计数δ不同于δ/|A|的概率；不能把a=0行计入最大值；群差分不能默认为整数减法。
  why_it_matters: 校验差分行和、最大值及失败见证。
  tags:
  - term
  - derivative
  decision: reference
- id: g09
  term: 完全非线性函数
  type: term
  source_chapter: 第2章定义2.2、定理2.2，书p22；第1章书p11
  author_definition: 原文短引：“简称PN函数。”
  definition_paraphrase: 从A到B且|A|≥|B|，δ=|A|/|B|时称PN，等价于每个非零导数平衡。二元n→m对应δ=2^(n−m)。
  key_distinction: 方形特征2不存在PN，不意味着二元矩形PN不存在；二元标量Bent是PN。
  why_it_matters: 参数、群结构和目标维数必须同时写明。
  tags:
  - term
  - PN
  decision: reference
- id: g10
  term: 几乎完全非线性函数
  type: term
  source_chapter: 第3章定义3.1、命题3.1，书p72
  author_definition: 原文短引：“简称APN函数。”
  definition_paraphrase: 本书在F_(pⁿ)到自身上以δ=2定义APN。特征2时非零导数方程有成对解，δ=2达到最优。
  key_distinction: 奇特征方形PN可有δ=1，所以APN在奇特征是次优；APN与AB不是同义词。
  why_it_matters: 避免将二元最优结论无条件推广到一般素特征。
  tags:
  - term
  - APN
  decision: reference
- id: g11
  term: Bent函数与Bent对偶
  type: term
  source_chapter: 第4章定义4.2、定理4.1、定理4.5，书pp106、108
  author_definition: 原文短引：“则其对偶函数也一定是Bent函数”
  definition_paraphrase: 正偶数n时，全部Walsh幅值恒为2^(n/2)，达到NL上界；W_f(a)=2^(n/2)(−1)^f*(a)定义Bent对偶。
  key_distinction: Bent不平衡；非Bent谱不能按符号强造Bent对偶；双对偶返回原函数不等于所有Bent都自对偶。
  why_it_matters: 先过平坦谱门，再输出符号对偶证书。
  tags:
  - term
  - bent
  decision: reference
- id: g12
  term: 向量Bent函数
  type: term
  source_chapter: 第5章定义5.2及定理5.1—5.3，书pp128—129
  author_definition: 无逐字引文；下列definition_paraphrase为依原书定义的转写释义
  definition_paraphrase: 每个非零输出线性组合都是Bent，等价于全部非零导数平衡；存在性必要条件是n偶且m≤n/2。
  key_distinction: 不是方形APN；不能仅检查坐标Bent便判向量Bent。
  why_it_matters: 将PN矩形条件与全分量谱连接。
  tags:
  - term
  - vectorial bent
  decision: reference
- id: g13
  term: 几乎Bent函数
  type: term
  source_chapter: 第5章定义5.3，书p132；§5.2，书pp133—135
  author_definition: 原文短引：“简称为AB函数。”
  definition_paraphrase: 本书指达到Sidelnikov-Chabaud-Vaudenay界的向量值函数，一般定义带n≤m+1。方形奇维n=m时NL=2^(n−1)−2^((n−1)/2)，等价于非零组件谱取0、±2^((n+1)/2)。
  key_distinction: 不等于标量semi-bent。只检测方形奇维是对一般定义的缩小合同。
  why_it_matters: 约束第5章术语路由，阻止把整个AB章误接标量三值谱工具。
  tags:
  - term
  - AB
  decision: reference
- id: g14
  term: 高原函数
  type: term
  source_chapter: 第3章定义3.5，书p76；第5章定义5.5，书p139
  author_definition: 原文短引：“如果它的Walsh谱取值为{0,±γ}的子集合，那么f就称为高原函数。”
  definition_paraphrase: 标量Walsh值落在{0,±γ}且非零幅值固定；向量高原要求每个非零组件高原，幅值可依组件而异。
  key_distinction: 高原不自动等于Bent或AB；Bent无零谱，AB另有维数和目标幅值。
  why_it_matters: 保持谱类包含关系而不偷换最优性。
  tags:
  - term
  - plateaued function
  decision: reference
- id: g15
  term: 相关免疫阶
  type: term
  source_chapter: 第6章定义6.1、定理6.2，书pp148—149
  author_definition: 无逐字引文；下列definition_paraphrase为依原书定义的转写释义
  definition_paraphrase: 在输入独立均匀条件下，输出与任意不超过t个输入坐标统计独立；等价于1≤wt(a)≤t时W_f(a)=0。
  key_distinction: CI不要求平衡；常函数也可具有高CI。一般输入分布不直接适用谱判据。
  why_it_matters: 把零频从相关免疫的非零低重量频率中分开。
  tags:
  - term
  - correlation immunity
  decision: reference
- id: g16
  term: 弹性函数与向量弹性
  type: term
  source_chapter: 第6章定义6.2及定理6.3，书p150；定义6.9，书p179
  author_definition: 原文短引：“如果F(x)既是t阶相关免疫的又是平衡的，则称F(x)是t阶向量弹性函数”
  definition_paraphrase: 标量为平衡且t阶CI；向量为平衡且固定任意t个输入比特后输出分布不变，记(n,m,t)。非零组件须全部t阶弹性。
  key_distinction: 弹性阶受输入坐标选择影响，不是任意仿射输入变换的不变量（书p156例6.1）；NL是另一目标。
  why_it_matters: 阻止等价变换后沿用旧弹性阶，要求重新检查。
  tags:
  - term
  - resilient
  decision: reference
- id: g17
  term: 零化子与标量代数免疫度
  type: term
  source_chapter: 第7章定义7.1、定理7.1，书p203
  author_definition: 无逐字引文；下列definition_paraphrase为依原书定义的转写释义
  definition_paraphrase: 非零布尔g满足fg=0或(f+1)g=0时，AI(f)取这两侧零化子中最小代数次数；AI≤ceil(n/2)。
  key_distinction: g不能是零函数；只找f侧会漏掉另一侧。次数高不等于AI高。
  why_it_matters: 以非零系数或完整g表作为结果证书。
  tags:
  - term
  - annihilator
  decision: reference
- id: g18
  term: 最优代数免疫度函数
  type: term
  source_chapter: 第7章定义7.2，书p204
  author_definition: 无逐字引文；下列definition_paraphrase为依原书定义的转写释义
  definition_paraphrase: AI达到ceil(n/2)的n元布尔函数称MAI。
  key_distinction: MAI只对经典双侧零化子定义最优，不自动抵抗快速代数攻击，也不自动高NL或高弹性。
  why_it_matters: 避免把单项最优写成系统安全。
  tags:
  - term
  - MAI
  decision: reference
- id: g19
  term: 向量基本代数免疫度
  type: term
  source_chapter: 第7章定义7.4，书p265
  author_definition: 原文短引：“F的基本代数免疫度AI(F)定义为”
  definition_paraphrase: 定义集合AI(S)为在S上恒零的非零n元布尔函数最小次数，基本AI(F)=min_a AI(F⁻¹(a))。
  key_distinction: 零化对象是输出纤维，不是输出坐标；空纤维允许常1作为零化子并使该最小值为0。
  why_it_matters: 计算器必须标明basic，否则无法与论文数值比较。
  tags:
  - term
  - basic vectorial AI
  decision: reference
- id: g20
  term: 向量图形代数免疫度
  type: term
  source_chapter: 第7章定义7.4，书p265
  author_definition: 原文短引：“F的图形代数免疫度AI_gr(F)定义为”
  definition_paraphrase: 在n+m变量的布尔环中取非零g(x,y)，要求对所有x有g(x,F(x))=0，最小次数为AI_gr(F)。
  key_distinction: g属于n+m变量空间，而基本AI的g属于n变量空间；两种搜索空间不同。
  why_it_matters: 图关系零化证书不能冒充标量/组件证书。
  tags:
  - term
  - graph AI
  decision: reference
- id: g21
  term: 向量组件代数免疫度
  type: term
  source_chapter: 第7章定义7.5及定理7.26，书p266
  author_definition: 原文短引：“F的组件代数免疫度AI_comp(F)定义为”
  definition_paraphrase: AI_comp(F)=min_(v≠0)AI(v·F)。原书给AI(F)≤AI_gr(F)≤AI(F)+m、AI(F)≤AI_comp(F)、AI_gr(F)≤AI_comp(F)+1。
  key_distinction: 全部坐标AI最小值仍不够；三种AI没有被定义成相等。常组件可能把AI_comp降到0。
  why_it_matters: 输出须含定义名、最坏非零掩码与零化子。
  tags:
  - term
  - component AI
  decision: reference
- id: g22
  term: 仿射等价、EA等价与CCZ等价
  type: term
  source_chapter: 第2章定义2.9—2.11，书p52；第4章§4.5，书p122
  author_definition: 无逐字引文；下列definition_paraphrase为依原书定义的转写释义
  definition_paraphrase: 第2章affine为F′=L₁∘F∘L₂，L₁、L₂为仿射置换；EA再允许加仿射L₃；CCZ为函数图之间存在可逆仿射映射。第4章Bent的“仿射等价”限定为输入仿射变换。
  key_distinction: 必须先说采用哪种等价。EA蕴含CCZ；相同不变量不替代给定变换证书。章节用语也不能自动统一。
  why_it_matters: 精确限定分类对象，防止把必要预筛当分类完成。
  tags:
  - term
  - affine
  decision: reference
- id: g23
  term: 有限域迹与绝对迹
  type: term
  source_chapter: 第1章§1.6，书p14
  author_definition: 原文短引：“当m=1时，也称为F_(2ⁿ)上的绝对迹函数。”
  definition_paraphrase: 当m|n时Tr_n^m(x)=Σ_(j=0)^(n/m−1)x^(2^(jm))，值在F_(2ᵐ)；m=1称绝对迹。选基后与二元向量表示连接。
  key_distinction: 迹依扩域/子域而定；绝对迹是标量，不可当作原有限域元素索引的等同映射。
  why_it_matters: 有限域构造报告模多项式、基和迹层次。
  tags:
  - term
  - trace
  decision: reference
- id: g24
  term: Reed–Muller码
  type: term
  source_chapter: 第1章定义1.4，书p18
  author_definition: 原文短引：“叫做r阶的二元Reed-Muller码（简称RM码）。”
  definition_paraphrase: 将所有m元次数≤r的布尔函数在全部2ᵐ输入点求值，得到二元线性码RM(r,m)，维数Σ_(i=0)^r C(m,i)。
  key_distinction: 此处码长n=2ᵐ，与函数输入维m不同。码距/到码距离与函数次数是不同量。
  why_it_matters: 明确函数真值表与码字的桥，支持零化子评价矩阵。
  tags:
  - term
  - RM(r,m)
  decision: reference
- id: g25
  term: 正交矩阵与支撑
  type: term
  source_chapter: 第6章定义6.3—6.4及定理6.8，书pp155—156
  author_definition: 原文短引：“设A是w行n列的矩阵，称A是一个(w,n,2,m)正交矩阵”
  definition_paraphrase: 支撑是f=1的输入集合，将其作为行形成特征矩阵；原书(w,n,2,t)正交矩阵要求任意t列的所有二元t模式等次数出现。
  key_distinction: 这里的“正交矩阵”是正交阵OA，不是实数线性代数QᵀQ=I。
  why_it_matters: 把CI/弹性转成组合计数检查。
  tags:
  - term
  - orthogonal array
  decision: reference
- id: g26
  term: 重量支撑与对称布尔函数
  type: term
  source_chapter: 第7章§7.3、定义7.3，书pp232、258
  author_definition: 原文短引：“f的重量支撑集定义为”
  definition_paraphrase: 对称布尔函数值仅依输入Hamming重量。WS(f)收集存在f(a)=1且wt(a)=i的重量i；对称时可用n+1个层值描述函数。
  key_distinction: 重量支撑是重量集合，不是全输入支撑，也不是每层1的数目。非对称时同一重量不能恢复全表。
  why_it_matters: 避免用压缩重量信息替代一般真值表。
  tags:
  - term
  - weight support
  decision: reference
- id: g27
  term: 构造计数与等价类计数
  type: term
  source_chapter: 第4章§4.5，书pp122—124；第6章§6.3，书pp175—179；第7章§7.2，书pp210—225
  author_definition: 无逐字引文；下列definition_paraphrase为依原书定义的转写释义
  definition_paraphrase: 构造族大小、全部函数数、某等价关系下类数、计数上下界必须分别注明。书中按不同构造和等价关系讨论它们。
  key_distinction: 给出很多构造参数不意味着产生同样多个不同函数；类数也不等于函数总数。历史“目前未知”限定为书稿时代。
  why_it_matters: 报告去重关系、是否只下界与参数条件；不引用未核清表值当现状。
  tags:
  - term
  - counting
  decision: reference
```
