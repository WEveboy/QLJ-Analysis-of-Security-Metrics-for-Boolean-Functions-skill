# 反例、失败模式与适用边界候选

提取器：cangjie-skill 2.5.0 / counter-example-extractor。2026-11-03。

取材范围：对本地 OCR 的全部 286 个逐页文件作去空格关键词检索（反例、不成立、不能、不一定、不等价、快速代数、未必、不存在、相同、反之），回查关键命中的原始页图。OCR 检索不等于全书证明精读。页图核读 PDF 19、33、64、82、110、143、145、151、174、214、215、216；正文书页 = PDF 页 − 10。下列引号均由页图核对；规则说明与合成实验另行标记。

```yaml
- id: ce01
  title: 坐标性质好不能替代整个向量函数的性质
  type: counter-example
  source_chapter: 第1章1.5，书p9 / PDF19
  source_quote: "一组安全性指标良好的布尔函数……所构成的向量值函数……的安全性能未必很好。"
  failure_mode: 只测坐标函数，漏掉坐标之间的线性组合或输出分布。
  mechanism: 向量Walsh变换涉及全部输出掩码v；单独坐标仅覆盖单位掩码。
  warning_signs: [只给坐标非线性度, 只检验每位平衡就宣布向量平衡]
  bound_to: [vector-metrics, resiliency]
  synthetic_example: "合成演练：F(x1,x2)=(x1,x1)，表[0,0,3,3]。两个坐标都平衡，但掩码11分量恒0，输出01与10从不出现。直接枚举即可核查；非原书例题。"
  tags: [vector, components, boundary]

- id: ce02
  title: 二元方形PN不可能不能扩大成所有二元n到m映射均无PN
  type: counter-example
  source_chapter: 第2章2.1，例2.1及其后，书p23 / PDF33；第3章3.1，书p72 / PDF82
  source_quote: "注意到当p=2时，如果x0是方程f(x+a)-f(x)=b的一个根，那么x0+a也是它的一个根，因此Daf(x)不可能是置换。"
  failure_mode: 丢失F_(p^n)到自身这一方形域条件；或直接把奇特征构造搬到二元域。
  mechanism: 特征2的非零差分解成对，方形PN要求每个差分恰有1个解，矛盾；非方形二元PN目标计数可为2^(n-m)，不构成同一矛盾。
  warning_signs: [声称所有二元PN不存在, 未写域特征就使用平方映射PN]
  bound_to: [pn, differential-uniformity, bent]
  source_example: "例2.1：f(x)=x²在p=2时差分恒a²；p>2时差分2ax+a²是置换。这里讨论方形有限域映射。"
  tags: [pn, characteristic, dimensions]

- id: ce03
  title: APN是差分最优的说法必须带域特征
  type: counter-example
  source_chapter: 第3章3.1，定义3.1后，书p72 / PDF82
  source_quote: "对特征为奇数的有限域来说，PN函数是差分均匀度最优的函数，APN函数是差分均匀度次优的函数。"
  failure_mode: 将二元方形APN最优直接写成一般素特征上APN最优。
  mechanism: APN定义为差分均匀度2；奇特征方形域可存在均匀度1的PN。
  warning_signs: [只写APN最优不写p, 把δ2当任意空间的统一下界]
  bound_to: [apn, pn]
  tags: [apn, finite-field, bound]

- id: ce04
  title: 差分均匀度或扩展Walsh谱相同不能充当CCZ等价证书
  type: counter-example
  source_chapter: 第3章3.4，书p100 / PDF110
  source_quote: "两个APN函数显然具有相同的差分均匀度，因此差分均匀度不能用来判定APN函数之间的CCZ不等价性。"
  failure_mode: 从共同δ或共同谱推出CCZ等价，甚至宣布完成分类。
  mechanism: 原书给的是不变量不同可以否定等价的单向筛选；不变量相同仅表示该筛选未区分。
  warning_signs: [指标相同所以等价, 未给图仿射变换或定理就归类]
  bound_to: [equivalence, vector-metrics]
  source_rule: "同页明确：扩展Walsh谱不同可断言CCZ不等价。相同不能据此反推，是该单向判据的逻辑边界。"
  tags: [ccz, invariant, certificate]

- id: ce05
  title: 代数次数不是一般CCZ等价不变量
  type: counter-example
  source_chapter: 第2章2.4，书p54 / PDF64，定理2.16后
  source_quote: "注意到逆函数与原函数是CCZ等价的，而逆函数的代数次数跟原函数的代数次数未必相等，因此，代数次数不是CCZ等价不变量。"
  failure_mode: 因函数次数不同就宣告CCZ不等价；或将EA和CCZ一般地当成相同概念。
  mechanism: 置换图交换输入与输出即得逆函数图，是CCZ图变换，但可改变次数。
  warning_signs: [用次数作CCZ必要不变量, 将特定PN结论推广到所有APN]
  bound_to: [equivalence]
  source_qualification: "同页说明一般函数EA等价蕴含CCZ等价，反向未必；PN特定类上的重合是额外定理。"
  tags: [ccz, ea, degree]

- id: ce06
  title: APN不能无条件反推AB；几乎Bent也不能误作标量semi-bent
  type: counter-example
  source_chapter: 第5章5.2，书p133 / PDF143，定理5.5—5.7
  source_quote: "一般情况下，定理5.6的逆命题不成立，即AB函数一定是APN函数，但APN函数未必是几乎Bent函数。"
  failure_mode: 只算δ2便报告AB；或将本书几乎Bent识别为任意标量半Bent。
  mechanism: AB还要求相应三值Walsh谱；奇数维二次函数的APN与AB等价需额外二次条件。
  warning_signs: [δ2所以AB, 把某一个组件半Bent等同向量AB, 省略奇数或二次前提]
  bound_to: [almost-bent, apn, scalar-spectrum]
  source_qualification: "定理5.5明确排除(n,m)=(2,1)后才推出n=m且n为奇数。标准奇数方形AB检测不覆盖该例外，不能无例外声称整书AB只可能奇数方形。"
  tags: [ab, apn, spectrum]

- id: ce07
  title: 高非线性度、代数次数与弹性阶仍不能保证高AI
  type: counter-example
  source_chapter: 第6章6.2，例6.2后，书p164 / PDF174
  source_quote: "然而，后来人们指出该布尔函数的代数免疫度非常低，从而LILI-128不能抵抗代数攻击。"
  failure_mode: 用若干传统指标达到界替代代数免疫度检查。
  mechanism: 该页讨论(10,3,6,480)函数，在固定弹性阶下次数与非线性度达到相应界，但低次零化关系是另一种约束。
  warning_signs: [几个指标最优所以系统安全, 无零化子检查]
  bound_to: [resiliency, algebraic-immunity]
  source_status: "原书历史案例转述；本次未独立复现LILI-128攻击，不将它冒充本轮攻击实验。"
  tags: [resiliency, ai, historical-case]

- id: ce08
  title: MAI并不等于抵抗快速代数攻击
  type: counter-example
  source_chapter: 第7章7.1，定义7.2后，书p204 / PDF214
  source_quote: "反过来，具有高的代数免疫度并不能保证密码算法对代数攻击的免疫性。"
  failure_mode: 只输出AI=ceil(n/2)便宣称函数或密码系统免疫全部代数攻击。
  mechanism: 快速代数攻击寻找低次非零g与适当次数的非零h，使fg=h；这比仅找fg=0的经典AI问题更广。
  warning_signs: [MAI所以安全, 把零化子算法称为完整快速代数攻击评估]
  bound_to: [algebraic-immunity]
  source_qualification: "原书同页明确通常要求h不为0，h=0退化为普通代数攻击；本次仅保留边界，不宣称完成快速代数免疫度算法。"
  tags: [mai, fast-algebraic-attack, scope]

- id: ce09
  title: 平衡不保证高代数免疫度
  type: counter-example
  source_chapter: 第7章7.1，书p205 / PDF215
  source_quote: "但是反之不然，平衡的布尔函数不一定代数免疫度好，例如，非常数仿射函数为平衡函数，但其代数免疫度仅为1。"
  failure_mode: 将高AI必要的重量条件或接近平衡倒推为高AI充分条件。
  mechanism: 非常数仿射函数本身或补函数提供一次零化关系，而重量仍完全平衡。
  warning_signs: [只根据重量估AI, 将必要条件当充分条件]
  bound_to: [algebraic-immunity, balance]
  tags: [balance, ai, necessity]

- id: ce10
  title: 代数免疫度不满足通常形式的次可加性
  type: counter-example
  source_chapter: 第7章7.1，书p206 / PDF216，引理7.2前
  source_quote: "有些文献中使用如下性质：设f1,f2∈Bn，则AI(f1+f2)≤AI(f1)+AI(f2)。这一结论是不正确的。"
  failure_mode: 在组合构造或证明里把AI当作范数，直接使用三角不等式。
  mechanism: "原书构造n≥5的MAI函数f，令f1=(1+x1)f、f2=x1f，则两者AI都为1，但AI(f1+f2)=ceil(n/2)>2。"
  warning_signs: [根据两个子函数AI之和给组合AI上界, 未检零化子便相加]
  bound_to: [algebraic-immunity, construction]
  synthetic_example: "本轮具体化合成演练，非原书具体例题：n=5，f(x)=1[wt(x)≥3]；用独立GF(2)矩阵秩实现逐次d=0,1,2,3检查双侧零化子。实测AI(f)=3，AI((1+x1)f)=1，AI(x1f)=1，并逐点核验f=f1+f2。"
  computed_table: [0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1]
  computation_convention: "整数升序真值表，x1为最高位；穷举次数不超过d的全部单项式作为列，在f=0与f=1支撑上分别计算GF(2)秩；首次列不满秩的d即AI。未导入项目runtime_metrics。"
  tags: [ai, counterexample, subadditivity]
```

## 核查与交付建议

- ce01—ce10均有页图依据，短引文不超过150汉字；ce02与ce03共享页图但限制的误用不同。
- 合成反例只用来验证规则与边界，不能当作原书亲历、原书具体例题或一般族证明。
- ce04的“相同不能反推”是从原书单向不变量判据所得的逻辑限制，未假称原书给出某对同谱不等价函数。
- 未检索到的材料不等于不存在；本次未完成所有构造、脚注及参考文献的逐条证明审计，也未做2011年后文献查新。
- 必须在编译后的AI能力卡保留ce08、ce09、ce10；在AB能力卡保留ce06；在PN/APN与等价卡分别保留ce02—ce05。
