"""Author-owned source builder. Compile resulting Bundle with cangjie-skill 2.5.0."""
from pathlib import Path
import hashlib
import json
import shutil
import yaml

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'research/qlj-security-metrics'
B=BOOK/'.cangjie/capabilities'

# slug, title, source, short quote, interpretation, synthetic example, trigger, execution, boundary
CARDS=[
('representation','真值表、ANF与位序核验','§1.1 书p1—3 / PDF11—13',
 '这个向量称为布尔函数的真值表。',
 '真值表不是一串无索引的比特。输入x按整数升序，x1为最高位，固定输入维数n。ANF是F2上平方自由多项式，掩码的置位表示参与乘积的变量。对子集做Möbius变换得到系数，再变换一次恢复原表。代数次数是最大非零单项式重量；本实现沿书p2将零函数次数记0。向量表值是输出位编码，分量用二元点积解释。',
 '合成演练：n=2，表[0,0,0,1]对应x1*x2，非零ANF掩码[3]，次数2。',
 '真值表转ANF、位序、代数次数、representation、Möbius transform；仅解释术语时先读词典。',
 '输入n,m,table；运行resources/runtime_metrics.py --input spec.json。验证长度2^n和值域后输出anf_masks、degree及输入哈希。标量可逐项评价ANF并与原表相等。向量逐非零分量输出，勿把分量次数当单变元形式次数。',
 'n≤10；向量n≤8,m≤8。布尔值、越界值、错误长度拒绝。域多项式输入需先给域模型并另转换成表；本工具不解析任意ANF字符串。'),
('walsh-nonlinearity','Walsh全谱、平衡与非线性度','§1.2—1.3 书p3—5；§4.1 书p105—106 / PDF115—116',
 '布尔函数的非线性度与其Walsh变换之间具有如下关系',
 '计算W_f(a)=Σ_x(-1)^(f(x)+a·x)，采用非归一化整数谱。由NL(f)=2^(n−1)−max|W|/2得到最近仿射距离，W(0)=0等价平衡。向量NL取全部非零输出分量的最小值。不能只检查坐标；输出掩码的线性组合可能使NL下降。与Bent卡的区别是本卡计算一般函数，不要求平坦谱。',
 '合成演练：f=x1*x2，W=[2,2,2,−2]、NL1、weight1；f=x1的NL为0。',
 'Walsh spectrum、nonlinearity、最大线性偏差、平衡性、全分量谱。',
 '运行通用计算命令；读walsh、nonlinearity、balanced。向量读取components中的全部2^m−1项并复核最小NL。完成标准为Parseval ΣW²=2^(2n)且NL与小维直接仿射距离一致。',
 '归一化Walsh值不可直接代入整数公式。高NL不自动等价APN，也不是完整系统安全结论。不能把单一坐标的NL报告成向量NL。'),
('binary-differential','二元差分表、PN与方形APN检测','§1.5 书p10—11；§2.1 书p21—24；§3.1 书p72—75 / PDF82—85',
 '对每一个非零元素a，函数Da f(x)=f(x+a)−f(x)是平衡的',
 '先明确群运算。本执行器只支持二元向量空间，输入差分用XOR。DDT(a,b)=#{x:F(x⊕a)⊕F(x)=b}；δ在a≠0上取最大。一般二元n→m PN要求n≥m且δ=2^(n−m)。二元方形APN要求δ=2。方形二元PN不可能，因为导数解成对出现；这不能否定矩形PN或标量Bent。奇特征平方映射的PN结论须使用域加减而非XOR。',
 '合成演练：GF(8)模t³+t+1的x³表[0,1,3,4,5,6,7,2]，δ2，为方形二元APN。奇特征平方原书例2.1仅作参考，程序不执行。',
 'DDT、差分均匀度、differential uniformity、PN、APN、S-box；几乎Bent另读AB卡。',
 '输入n,m≥2及完整表，运行通用命令；输出完整DDT、δ及最坏(a,b)见证、binary_pn与binary_square_apn。检查每行和2^n、a≠0各计数偶数。m=1时通用程序走标量分支，PN用Bent等价判据；不输出不存在的DDT字段。',
 'n,m≤8。APN字段仅n=m才给布尔值，非方形给null。原书一般素特征定义超出本二元执行器。未知构造参数不补猜。DDT好不保证置换，也不完成等价分类。'),
('bent-dual','Bent检测与对偶恢复','§4.1 定义4.2、定理4.1/4.5，书p106—108 / PDF116—118',
 '则其对偶函数也一定是Bent函数',
 '标量Bent要求n为正偶数且所有频率W均为±2^(n/2)。通过后，以Walsh符号恢复dual：正置0、负置1，再计算对偶之对偶检查回到原函数。Bent的零频不为0，所以不平衡。向量Bent要求所有非零分量Bent；参数门为n偶且m≤n/2。对偶只对已验证标量Bent输出。',
 '合成演练：x1*x3+x2*x4四变量函数NL6、weight6；对偶仍为自身。自对偶仅为该例结论。',
 'Bent判定、bent dual、平坦谱、向量Bent；请求生成函数转paired-bent卡。',
 '运行通用命令，读bent和可选dual_table；只在bent=true时解释对偶。对输出表重算以核验双对偶。向量读vector_bent和全部components。',
 '奇维不输出Bent对偶；零谱符号不能强作对偶。不要把AB、标量semi-bent、平衡函数当Bent。构造不是本卡职责。'),
('square-almost-bent','方形奇维Almost Bent检测','§5.1 定义5.3及SCV界讨论，书p130—132 / PDF140—142',
 '那么就称F为几乎Bent(Almost Bent)函数，简称为AB函数',
 '本书几乎Bent是向量Almost Bent。限定为方形奇数n=m时，非线性度最优值为2^(n−1)−2^((n−1)/2)，对应全部非零分量的Walsh谱落在{0,±2^((n+1)/2)}。必须遍历所有分量，而不是某一坐标三值谱。与APN分别计算；不能用APN一项冒充AB判定。一般(n,m)的SCV界不在本程序执行合同内。',
 '合成演练：GF(8)立方表的全部非零分量谱为0/±4，NL2，square_almost_bent=true。',
 '几乎Bent、Almost Bent、AB、SCV、奇数维向量最优NL；标量semi-bent只作词典区分。',
 '输入n=m奇数且m≥2的表，运行通用命令，读取square_almost_bent与全部分量谱。非方形字段null，方形偶维该受限判定返回false并在解释中说明只适用奇维合同。',
 '该实现不覆盖原书n=m+1的(2,1)特例，m=1走标量分支也不提供本字段。未实现一般SCV界计算。不得将程序合同当成本书AB定义的全部范围。'),
('resiliency','相关免疫与弹性谱检测','§6.1 定义6.1—6.2、定理6.2—6.3，书p148—150 / PDF158—160',
 '若f(x)既是m阶相关免疫函数又是平衡函数，则称f(x)是m阶弹性函数',
 '在输入独立均匀条件下，CI阶t只要求1≤wt(a)≤t的谱为零；弹性另外要求W(0)=0。本实现返回最大满足阶，0阶弹性表示仅平衡。非平衡函数resiliency_order=null，而不是误报0。常函数CI可到n，但非弹性。向量弹性逐全部非零分量检查，取最小阶；只检查坐标会漏掉常分量。',
 '合成演练：四变量奇偶和为3阶弹性。表[0,0,3,3]两个坐标均平衡，但第三个分量恒零，向量不平衡。',
 '相关免疫、correlation immunity、resiliency、弹性阶、均匀投影；构造与计数另属待审参考。',
 '运行通用命令；标量读取correlation_immunity_order、balanced、resiliency_order。要检查要求阶t时比较最大阶≥t，null判失败。向量需验证全部分量，并报告最坏分量。',
 '相关免疫不代表在有偏相关输入下仍独立。次数界只是必要条件。t=n−1边界不能机械使用常见n−t−1界。向量AI与此无关。'),
('scalar-ai','标量代数免疫度与非零零化子证书','§7.1 定义7.1、定理7.1，书p202—205 / PDF212—215',
 '使得fg=0或(f+1)g=0成立的非零布尔函数g的最小代数次数',
 'AI寻找f或f+1的非零零化子的最小次数。按d升序构造次数≤d单项式，在目标支持集上建立GF(2)齐次系统。任一侧出现非零核向量即可；零向量不能作证。较低次数两侧均满列秩，给最小性的有限消元依据。MAI指AI=ceil(n/2)，仅为该单项指标最优。常函数AI0。实现算法独立编写，不归因为原书现成代码。',
 '合成演练：f=x1*x2的AI1，g=1+x1使fg=0；n=4配对乘积Bent的AI2。',
 'algebraic immunity、AI、MAI、零化子、annihilator；请求向量AI时先辨三定义，当前不计算。',
 '输入添加ai:true；运行通用命令，读algebraic_immunity的value、annihilates、monomial_masks、witness_table。逐点核g非零、次数符合并且对应乘积全0。rank_checks逐项列degree、annihilates、rows、columns、rank、nullity；所有低于AI的次数应包含两侧满列秩记录。常函数method=constant_function_identity直接以非负次数及常数零化子证明AI0。非恒定函数n>6输出not_computed；已验证常函数直接给AI0，不将缺结果写成0。',
 '非恒定函数精确AI限n≤6；常函数在输入维数预算内直接判AI0。向量分量可逐项算标量AI，但不冒充已实现基本或图形向量AI，也不自动汇总三定义。MAI不保证快速代数攻击安全；本工具不计算FAI。'),
('paired-bent','配对乘积Bent构造及复算','§4.1 例4.1及证明，书p106—107 / PDF116—117',
 '设n=2m为任意正偶数',
 '按书中例4.1把变量分成两半，f=Σ_(i=1)^h x_i*x_(h+i)，n=2h。对第二半变量求字符和，仅一项保留，从而Walsh恒幅2^h。这是已有符号构造；小维全算用于检查实现，不代替原书证明。先生成完整表，再用Bent卡独立判定。程序位序采用x1最高位。',
 '原书数学例题4.1的n=4实例：表[0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0]，weight6、NL6。',
 '构造Bent、paired product、例4.1、生成偶数维Bent；已有表的判定用bent-dual卡。',
 '运行python resources/runtime_metrics.py --paired-bent 4 --out new-result.json；输出input完整表和result。完成标准：n正偶数、表长度正确、result.bent=true、NL=2^(n−1)−2^(n/2−1)。',
 '只实现该构造，2≤n≤10且偶数。不能声称覆盖MM/PS/Dillon全族、计数或等价类。奇数n拒绝。相邻配对是变量置换后的同构写法，不能冒充本例印刷式。')
]


CARDS.append((
'mm-bent','Maiorana–McFarland Bent构造与谱证书','§4.3 定义4.5、式(4.9)、定理4.9，书p113 / PDF123',
'其中π是F₂^(n/2)上的置换，g是任意n/2元布尔函数，·表示F₂^(n/2)中向量的内积。（上下标规范排写）',
'设n=2h，x和y均为h位向量，f(x,y)=x·π(y)+g(y)。π必须是整个半维空间的置换，g任意。对x求字符和，只在π(y)=a时非零，因此W_f(a,b)=2^h(-1)^(b·π^(-1)(a)+g(π^(-1)(a)))。本卡把原书符号证明变成给定有限实例的证书：保存逆置换、预测谱，再与计算器全谱比较。配对乘积是π为恒等且g=0的特例。',
'合成演练：h=2，π=[2,0,3,1]，g=[0,1,1,0]，构造16项表；全谱幅值4，NL6。穷举h=2的24个置换与16个g共384例均经直接字符和核验。',
'Maiorana–McFarland、M-M、MM Bent、任意半维置换构造Bent；固定配对乘积使用paired-bent卡，已有表判断用bent-dual卡。',
'运行python resources/mm_construction.py --input mm.json --out new-mm-result.json。输入h、长度2^h的整数置换pi与同长度0/1表g。坐标z=(x<<h)|y，前h位为x。输出function完整表、analysis、inverse_pi及predicted_walsh；matched必须为true。完成后可将function另存JSON交通用计算器复算。',
'限定1≤h≤5，n≤10；重复或越界pi、布尔值冒充整数、错误g长度均拒绝。非置换π不满足本构造定理，拒绝不能被解释为所有变体函数都非Bent。并未实现Dillon/PS/间接构造或计数分类。'))

def main():
    for d in ('cards','resources','book'):(B/d).mkdir(parents=True,exist_ok=True)
    for name in ('runtime_metrics.py','test_metrics.py','mm_construction.py','test_mm.py'):
        shutil.copyfile(BOOK/name,B/'resources'/name)
    usage='''# 执行合同
Python 3.10+，仅标准库。所有相对命令以技能根目录为工作目录。

python resources/runtime_metrics.py --input spec.json --out new-result.json
python resources/runtime_metrics.py --paired-bent 4 --out new-bent.json
python -m unittest discover -s resources -p "test_*.py" -v
python resources/mm_construction.py --input mm.json --out new-mm-result.json
M-M输入：h（1至5）、pi（全置换表）、g（布尔表），n=2h；z=(x<<h)|y。

输入JSON：{"n":3,"m":3,"table":[0,1,3,4,5,6,7,2],"ai":false}。
table长度2^n，元素严格整数，x1为最高位。m省略时为1。
标量n≤10；向量n≤8,m≤8；非恒定函数精确AI n≤6，常函数直接AI0。超AI预算单项not_computed；其他越限拒绝。
成功退出0，输入/文件错误退出2；输出采用新建模式，已有文件拒绝覆盖。
结果带完整输入、输入SHA256、维数、口径和exhaustive_finite_table级别；哈希不是签名认证。
结果可重跑逐字段比较；需要原始stdout、退出码、环境时由调用者保存。
不搜索未知等价，不作全参数最优性/系统安全结论，不把2011年开放问题当作今天状态。
'''
    (B/'resources/usage.md').write_text(usage,encoding='utf-8')
    caps=[]
    for slug,title,src,quote,interpret,example,trigger,execution,boundary in CARDS:
        text=f'# {title}\n\n## R — Reading\n\n> {quote}\n\n来源QLJ2011，{src}。引文为核图短摘；公式在I中规范转写。\n\n## I — Interpretation\n\n{interpret}\n\n## A1 — Application Example\n\n{example}\n\n## A2 — Future Trigger\n\n{trigger}\n\n## E — Execution\n\n先读resources/usage.md。{execution}\n\n## B — Boundary\n\n{boundary}\n'
        (B/'cards'/f'{slug}.md').write_text(text,encoding='utf-8')
        related=[] if slug=='representation' else ['cap.qlj.representation']
        if slug in ('bent-dual','square-almost-bent','resiliency'):related+=['cap.qlj.walsh-nonlinearity']
        if slug in ('paired-bent','mm-bent'):related+=['cap.qlj.bent-dual']
        caps.append(dict(capability_id='cap.qlj.'+slug,revision=1,status='active',slug=slug,title=title,
            importance='high',importance_rationale='T01—T11科研任务：统一定义、穷举计算及失败边界，降低条件遗漏。',
            one_liner=interpret.split('。')[0]+'。',intents=[title,trigger],keywords=[slug,title],also_read=related,
            card=f'cards/{slug}.md',frontmatter=dict(description=trigger,tags=['boolean-functions','qlj']),
            source_evidence=[dict(source_id='QLJ2011',version_id='2011-first-edition',location=src)],
            resources=['resources/runtime_metrics.py','resources/test_metrics.py','resources/usage.md','resources/mm_construction.py','resources/test_mm.py'],
            promotion=dict(destination='router',gate=dict(independent_intent=True,independent_contract=True,
                independent_run=False,independent_reuse=True,independent_eval=True),
                notes='共用输入规格与同一计算器，保持single-first，避免重复发现入口。')))
    desc='基于李超、屈龙江、周悦《密码函数的安全性指标分析》的科研能力：真值表与ANF、Walsh非线性度、二元差分PN/APN、Bent及对偶、方形奇维AB、相关免疫与弹性、标量AI、配对乘积与M-M Bent构造。用于有限候选复算和条件核对；不执行全族分类或密码系统安全证明。'
    entry=dict(name='qlj-security-metrics',description=desc,core_principles=[
        '先读resources/usage.md与所需能力卡；输入必须有维数、完整表及位序。',
        '区分B原书事实、D独立实现/合成演练、H未证研究方向；不把有限验证称为全族证明。',
        '向量性质检查全部非零分量；几乎Bent指向量AB；PN/APN保留域特征和维数条件。',
        '本版是限定范围研究初稿：全书OCR检索与关键页核图完成，待审构造见overview，未逐一定理核验。',
        'runtime为Python标准库；非恒定函数精确AI限n≤6；常函数直接AI0。not_computed与失败不同，null与0不同。',
        '参考来源为2011年专著；有关今天的最优记录与开放问题必须另外核查。'],
        out_of_scope=['通用代码工程、任意书籍自动蒸馏、无来源的新颖性和系统安全证明。'],
        stop_conditions=['关键域模型或输入规格不足时先补信息；超出预算明确未算。','未核参数构造不进入已证明方法；向量AI先区分三定义，当前只保留参考。'])
    bundle=dict(schema_version=1,bundle_id='bundle.qlj-security-metrics',book=dict(title='密码函数的安全性指标分析',
        author='李超、屈龙江、周悦',source_pack='qlj-security-metrics-2011',baseline_tag='research-draft-0.2.1'),
        entry=entry,router_entry=dict(name='qlj-security-metrics-router',description=desc),promotion_budget=2,capabilities=caps)
    (B/'verified.yaml').write_text(yaml.safe_dump(bundle,allow_unicode=True,sort_keys=False),encoding='utf-8')
    shutil.copyfile(BOOK/'BOOK_OVERVIEW.md',B/'book/overview.md')
    if (BOOK/'GLOSSARY.md').exists():shutil.copyfile(BOOK/'GLOSSARY.md',B/'book/glossary.md')
    print('Bundle:',len(caps),'capabilities')

if __name__=='__main__':main()
