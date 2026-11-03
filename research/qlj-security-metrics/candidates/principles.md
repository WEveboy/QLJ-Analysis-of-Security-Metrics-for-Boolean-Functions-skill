# 原则与计算规则提取

来源：李超、屈龙江、周悦《密码函数的安全性指标分析》，科学出版社，2011。以下书页均指印刷页，PDF页=书页+10。

本记录基于指定关键页的逐页图像核读：PDF115—118、138—142、158—163、210—217、275—278，共27页；不冒充全书逐公式核验。OCR仅用于其余章节检索，OCR中的上下标、集合符号、求和界不直接作为执行依据。候选不是最终 verified 判定。

```yaml
- id: p01
  title: 标量非线性度的全谱计算
  type: calculation
  source_chapter: 第4章4.1，定义4.1，式4.1—4.3，书p105—106 / PDF115—116
  source_quote: "布尔函数的非线性度与其Walsh变换之间具有如下关系"
  inputs: n以及完整布尔真值表，必须记录索引的位序
  formula: "W_f(a)=sum_x (-1)^(f(x)+a·x); NL(f)=2^(n-1)-max_a|W_f(a)|/2"
  units: 精确整数计数；非归一化Walsh变换
  output: 全谱、最大幅值及取得点、NL
  summary: 计算全部频率的Walsh值，再用最大绝对值计算距全部仿射函数的最小Hamming距离；不能只检查零频或一个线性函数。
  missing_conditions: 实现需明确输入位序和点积；这是工程合同，不应冒充原书固定的软件格式
  tags: [nonlinearity, walsh, calculation]

- id: p02
  title: Bent的平坦谱判据及偶数维门
  type: calculation
  source_chapter: 第4章4.1，定义4.2、定理4.1，书p106 / PDF116
  source_quote: "若f(x)是一个n元Bent函数，那么n一定是正偶数"
  inputs: n以及完整布尔真值表
  formula: "n为正偶数且对全部a有W_f(a)∈{−2^(n/2),2^(n/2)}；等价于NL=2^(n-1)−2^(n/2−1)"
  units: 非归一化整数Walsh谱
  output: is_bent，失败频率和对应谱值；n为奇数直接说明不适用Bent定义
  summary: 最大幅值达到下界时由Parseval得到全部幅值相同。Bent无需平衡；实际上W_f(0)非零。
  missing_conditions: 无；应区分奇数维其他最优谱类
  tags: [bent, spectrum, parity]

- id: p03
  title: 已验证Bent函数的对偶恢复
  type: calculation
  source_chapter: 第4章4.1，定理4.5前定义及定理4.5，书p108 / PDF118
  source_quote: "则其对偶函数也一定是Bent函数"
  inputs: 已通过p02判据的真值表和全部Walsh谱
  formula: "W_f(a)=2^(n/2)(−1)^(dual_f(a))；正号置0，负号置1"
  units: 布尔输出
  output: 对偶真值表，独立再变换检查dual(dual(f))=f
  summary: 仅在幅值平坦且非零的Bent谱上按符号定义对偶。二次回算是实现自检，不能用一次符号映射冒充已核验。
  missing_conditions: 非Bent时不可强行由零谱或不等幅谱构造Bent对偶
  tags: [bent, dual, certificate]

- id: p04
  title: 向量非线性度必须覆盖全部非零分量
  type: calculation
  source_chapter: 第5章5.1，定义5.1，书p128 / PDF138
  source_quote: "F的非线性度定义为"
  inputs: n、m、完整F: F2^n→F2^m映射表
  formula: "NL(F)=min_(v≠0) NL(v·F)=2^(n−1)−max_(v≠0,u)|sum_x(−1)^(v·F(x)+u·x)|/2"
  units: 精确整数Hamming距离
  output: 全部分量非线性度、最坏分量v和最坏频率u
  summary: 除m个坐标外，还要计算全部非零线性组合。坐标都具有高NL不保证向量NL同样高。
  missing_conditions: 输出编码与分量点积必须明确
  tags: [vectorial, components, nonlinearity]

- id: p05
  title: 向量Bent的分量判据与参数门
  type: rule
  source_chapter: 第5章5.1，定义5.2、定理5.1—5.3，书p128—129 / PDF138—139
  source_quote: "那么2|n，并且m≤n/2"
  inputs: n、m、完整映射F
  formula: "每个非零v的v·F均为Bent；必要条件n偶且m≤n/2"
  units: 布尔判定
  output: 参数门结果和全部非零分量的Bent状态；不满足时给反证条件或失败分量
  summary: 二元向量Bent可由每个非零导数的平衡性刻画。这里平衡导数指每个输出值出现同样次数，并非方形APN的二对一要求。
  missing_conditions: 不将方形二元PN函数存在性与一般(n,m)Bent存在性混为一谈
  tags: [vectorial-bent, pn, dimension]

- id: p06
  title: 几乎Bent（AB）术语及达到SCV界的检验
  type: calculation
  source_chapter: 第5章5.1，定理5.4及定义5.3，书p130—132 / PDF140—142
  source_quote: "那么就称F为几乎Bent(Almost Bent)函数，简称为AB函数"
  inputs: n、m、完整映射表；一般定义要求n≤m+1
  formula: "SCV=2^(n−1)−sqrt(3·2^n−2−2(2^n−1)(2^(n−1)−1)/(2^m−1))/2；NL(F)达到此界"
  units: 最好用整数平方判定避免浮点误判
  output: 参数是否适用、NL(F)、界值及是否达到
  summary: 本书“几乎Bent”是向量Almost Bent，不是标量semi-bent。方形n=m时界化为2^(n−1)−2^((n−1)/2)，实际检测应明确奇数n。书中也讨论n=m+1，其存在性仅留下(2,1)特例。
  missing_conditions: 一般(n,m)SCV界必须保留n≤m+1；若只实现方形奇维AB，应明确缩小执行合同，不把全部第5章宣布实现
  tags: [almost-bent, ab, scv, terminology]

- id: p07
  title: 相关免疫与弹性的不同频率范围
  type: calculation
  source_chapter: 第6章6.1，定义6.1—6.2、定理6.2—6.3，书p148—150 / PDF158—160
  source_quote: "若f(x)既是m阶相关免疫函数又是平衡函数，则称f(x)是m阶弹性函数"
  inputs: n、真值表、要求阶数t（为避免混淆，用t替代本节原书的m）
  formula: "CI阶≥t iff W_f(a)=0 for 1≤wt(a)≤t；弹性阶≥t iff W_f(a)=0 for 0≤wt(a)≤t"
  units: 精确零谱判定
  output: CI最大阶数，平衡性，弹性最大阶数或不满足平衡，以及最小重量失败频率
  summary: CI不要求平衡，弹性在CI基础上额外要求W_f(0)=0。常函数可以有最高阶CI但不是平衡弹性函数。
  missing_conditions: 原书概率定义假定输入独立且均匀；不能推广到任意输入分布而不重新论证
  tags: [correlation-immunity, resilience, walsh]

- id: p08
  title: Siegenthaler次数约束的参数区间
  type: rule
  source_chapter: 第6章6.1，定理6.4及推论6.1，书p150—151 / PDF160—161
  source_quote: "若f(x)是m(1≤m<n−1)阶弹性函数，则deg f≤n−m−1"
  inputs: n、已验证的CI/弹性阶t、ANF次数
  formula: "弹性：1≤t<n−1时deg f≤n−t−1；CI：1≤t≤n−1时deg f≤n−t；n−1阶弹性为全变量奇偶和加常数"
  units: 整数次数
  output: 前提适用性和必要条件通过/违反
  summary: 次数界仅是必要条件，不能反推CI或弹性。边界t=n−1必须单列，不能机械使用n−t−1而把奇偶函数错误排除。
  missing_conditions: 已核原书给出的具体区间；不要省略下限或例外
  tags: [siegenthaler, degree-bound, resilience]

- id: p09
  title: Sarkar非线性度必要上界
  type: rule
  source_chapter: 第6章6.1，定理6.6，书p153 / PDF163
  source_quote: "这个上界被称为Sarkar界"
  inputs: 已验证阶数t、n、NL
  formula: "CI且t≤n−1：NL≤2^(n−1)−2^t；弹性且t≤n−2：NL≤2^(n−1)−2^(t+1)"
  units: 整数距离
  output: 必要上界、与实算NL的比较
  summary: 上界只在相应阶数前提下使用；不能把上界本身当成任何参数下可达到的构造。该页进一步讨论的达到条件应按实际应用再核。
  missing_conditions: 当前不提供全参数可达性证明或构造程序
  tags: [sarkar, upper-bound, nonlinearity]

- id: p10
  title: 标量代数免疫度必须搜索两侧非零零化子
  type: calculation
  source_chapter: 第7章7.1，定义7.1，书p202—203 / PDF212—213；线性方程组说明书p205 / PDF215
  source_quote: "使得fg=0或(f+1)g=0成立的非零布尔函数g的最小代数次数"
  inputs: 完整布尔真值表、n、精确搜索预算
  formula: "AI(f)=min{deg g: g≠0且fg=0或(f+1)g=0}"
  units: 整数次数
  output: 最小次数、哪一侧的非零零化子、ANF系数、逐点乘积核验和低次数不存在证据
  summary: 对每个次数d枚举次数≤d的单项式，建立在f=1支持集上为零的齐次GF(2)线性系统，再对f+1重复。最早出现的非零解给AI；零向量永远不能作为零化子见证。矩阵消元是由定义与p205说明得到的实现方式。
  missing_conditions: 常函数直接按定义得到AI0；预算不足只给已发现上界或未算，不输出假精确AI
  tags: [algebraic-immunity, annihilator, gf2]

- id: p11
  title: MAI上界及其不能替代快速代数免疫
  type: rule
  source_chapter: 第7章7.1，定理7.1、定义7.2，书p203—204 / PDF213—214
  source_quote: "具有高的代数免疫度并不能保证密码算法对代数攻击的免疫性"
  inputs: n、已验证AI值及是否常函数
  formula: "AI(f)≤ceil(n/2)；MAI iff AI(f)=ceil(n/2)"
  units: 整数次数
  output: 相对该指标的最优性，明确快速代数攻击仍需其他条件
  summary: 原书定理还给出deg f上界，常函数须按零函数次数约定单独处理。达到MAI表示单项指标最优，不表示完整算法安全；快速代数攻击考察fg=h的低次/适当次数关系，不能用不存在低次零化子替代。
  missing_conditions: 不把本轮AI计算程序标为已经实现快速代数免疫度算法
  tags: [mai, fast-algebraic-attack, limit]

- id: p12
  title: 高AI的重量必要条件
  type: rule
  source_chapter: 第7章7.1，定理7.2，书p204—205 / PDF214—215
  source_quote: "平衡的布尔函数不一定代数免疫度高"
  inputs: n、Hamming重量和已知AI下界AI>d
  formula: "sum_(i=0)^d C(n,i) ≤ wt(f) ≤ sum_(i=0)^(n−d−1) C(n,i)"
  units: 整数重量
  output: 必要条件检验；奇数n且MAI时必须平衡
  summary: 由零化子齐次系统无非零解得到支持集规模下界，两侧联用。满足重量区间不能反推AI；非恒定仿射函数平衡而AI=1是书中所给反向警告。
  missing_conditions: 仅必要条件，不得用此条件替代零化子搜索
  tags: [ai, weight, necessary-condition]

- id: p13
  title: 不能使用AI的伪次可加性
  type: rule
  source_chapter: 第7章7.1，书p206 / PDF216
  source_quote: "这一结论是不正确的"
  inputs: 函数f1、f2或对其AI的推导
  formula: "禁止推定AI(f1+f2)≤AI(f1)+AI(f2)；可使用已核引理7.1：若deg f2=r，则AI(f1)−r≤AI(f1+f2)≤AI(f1)+r"
  units: 次数
  output: 错误推理定位及合法替代界的前提
  summary: 原书取n≥5、AI(f)=ceil(n/2)，令f1=(1+x1)f、f2=x1f，两者AI为1而和为f，直接否定次可加式。
  missing_conditions: 不把这个已给出的符号反例宣称为本轮新发现
  tags: [counter-example, ai, invalid-rule]

- id: p14
  title: 向量基本AI、图形AI和组件AI的定义分离
  type: calculation
  source_chapter: 第7章7.4.1，定义7.4—7.5，书p265—266 / PDF275—276
  source_quote: "下面给出向量值函数代数免疫度的三个定义"
  inputs: n、m、完整映射表和明确指标名称
  formula: "AI(F)=min_a AI(F^(-1)(a))；AI_gr(F)=min{deg g:0≠g∈B_(n+m),g在gr(F)上为0}；AI_comp(F)=min_(v≠0) AI(v·F)"
  units: 最小非零零化子的代数次数
  output: 使用的定义、最小侧/分量/纤维、见证多项式所处变量空间
  summary: 集合AI(S)是非零布尔多项式在S上恒零的最小次数。基本AI按输出纤维取最小；图形AI使用n+m个变量；组件AI按非零输出线性组合取标量AI。它们不同，不能用组件最小值命名为无修饰“向量AI”。空纤维按集合定义允许非零常数1，因此给基本AI0；必须记录是否存在空纤维。
  missing_conditions: 全部三种定义实现需不同算法；只实现组件AI时必须标AI_comp，图形AI和基本AI单列not_computed
  tags: [vectorial-ai, graph-ai, component-ai]

- id: p15
  title: 向量三种AI的关系界与参数化上界
  type: rule
  source_chapter: 第7章7.4.1，定理7.26—7.27，书p266—267 / PDF276—277
  source_quote: "下面定理刻画了上面三种代数免疫度之间的联系"
  inputs: n≥m≥1、指标定义和已算数值
  formula: "AI(F)≤AI_gr(F)≤AI(F)+m；AI(F)≤AI_comp(F)；AI_gr(F)≤AI_comp(F)+1；基本AI上界d为sum_(i=0)^d C(n,i)>2^(n−m)的最小正整数；图形AI上界D为sum_(i=0)^D C(n+m,i)>2^n的最小正整数；AI_comp≤ceil(n/2)"
  units: 次数，组合数精确整数
  output: 使用条件和界检验，不以界值代替精确AI
  summary: 这些是不同指标间的关系。定理7.28给基本AI可达性，但不推出图形AI或组件AI在全部参数下可达；书p268对后两项仍作当时研究状态说明。
  missing_conditions: 本轮未独立核验所有关系界的全部退化情形；作为带出处的参考规则保留，部署前需明确非满射和常分量约定
  tags: [vectorial-ai, bounds, reference]

- id: p16
  title: 向量最优AI构造的参数与未读结尾
  type: procedure
  source_chapter: 第7章7.4.2，式7.15—7.16，书p268 / PDF278
  source_quote: "一类具有最优代数免疫度的向量值函数"
  inputs: 有限域F_(2^n)、本原元α、n、m、s以及完整构造定理
  formula: 本页将域按α指数的连续区间分成2^m个纤维，再以纤维标签定义F
  units: 有限域函数
  output: 候选构造及所缺后续条件
  summary: 本页只能核到构造开头与部分性质，后续性质仍在下一页，不能据此编译为已完成构造能力。
  missing_conditions: PDF279及后续完整定理、线性无关条件、AI最优证明与域模型实现需补读；应转needs_review
  tags: [construction, vectorial-ai, needs-review]
```

## 提取边界与可激活建议

第一批可以形成原子卡：全谱NL、Bent/对偶、向量全分量NL、方形奇维AB、CI/弹性、标量AI双侧零化子。原书每项都有完整定义或判据，仍需V2实际新输入复算及V3任务增益判断。向量AI三定义可先作为规格判别和参考卡，若运行时仅算AI_comp，应写清另外两项未计算。复杂弹性构造/计数、一般AB构造以及向量MAI构造不能从关键页视为已经全面实现。

本文件中的短引文均从页图核读。公式按原书数学内容整理为可读文本，并对实现位序、矩阵与预算的补充单独说明；不将工程补充归为作者原话。
