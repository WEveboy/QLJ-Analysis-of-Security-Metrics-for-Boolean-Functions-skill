"""Independent task exercise. Does not import the implementation or its tests."""
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / 'skills/qlj-security-metrics'
OUT = Path(__file__).resolve().parent
PY = sys.executable
records = []
f = [0, 0, 0, 1]
cube = [0, 1, 3, 4, 5, 6, 7, 2]
bent = [0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0]

def direct_walsh(table):
    return [sum((-1)**(v+((a & x).bit_count()%2)) for x,v in enumerate(table)) for a in range(len(table))]

def run(i, request, route, spec=None, paired=None):
    output = OUT / ('task-%02d-result.json' % i)
    command = [PY, 'resources/runtime_metrics.py']
    if spec is not None:
        inp = OUT / ('task-%02d-input.json' % i)
        inp.write_text(json.dumps(spec), encoding='utf-8')
        command += ['--input', str(inp)]
    else:
        command += ['--paired-bent', str(paired)]
    command += ['--out', str(output)]
    p = subprocess.run(command, cwd=SKILL, capture_output=True, text=True, encoding='utf-8')
    entry = dict(id=i, request=request, route=route, cwd=str(SKILL), command=command,
                 command_display=subprocess.list2cmdline(command), exit_code=p.returncode,
                 stdout=p.stdout, stderr=p.stderr, output_file=str(output),
                 status='completed' if p.returncode == 0 else 'failed')
    records.append(entry)
    if p.returncode:
        raise RuntimeError(entry)
    report = json.loads(output.read_text(encoding='utf-8'))
    return entry, report

def note(i, request, route, conclusion, status='completed_boundary_response'):
    records.append(dict(id=i, request=request, route=route, command=None, exit_code=None,
                        output_file=None, status=status, conclusion=conclusion,
                        action='No calculator command: explanation, missing-input stop, or scope refusal as applicable.'))

e,r = run(1, 'n2 [0,0,0,1] 转ANF', ['representation'], {'n':2,'m':1,'table':f})
e['conclusion'] = 'ANF=x1*x2; anf_masks=[3]; degree=2; input order ascending integer, x1 MSB.'
assert r['result']['anf_masks'] == [3]
e['independent_checks'] = {'anf_evaluates_to_input': all(((x>>1)&1)*(x&1)==v for x,v in enumerate(f))}

e,r = run(2, '同表全Walsh/NL', ['walsh-nonlinearity'], {'n':2,'m':1,'table':f})
w = direct_walsh(f)
assert r['result']['walsh'] == w
nl = min(sum(v != (((a&x).bit_count()%2)^c) for x,v in enumerate(f)) for a in range(4) for c in (0,1))
assert r['result']['nonlinearity'] == nl
e['conclusion'] = {'walsh':w, 'nonlinearity':nl, 'balanced':False}
e['independent_checks'] = {'direct_walsh':True, 'parseval':sum(v*v for v in w)==16, 'direct_affine_distance':nl}

e,r = run(3, 'n3m3 [0,1,3,4,5,6,7,2] 差分与APN', ['binary-differential'], {'n':3,'m':3,'table':cube})
d = [[sum((cube[x]^cube[x^a])==b for x in range(8)) for b in range(8)] for a in range(8)]
assert r['result']['ddt'] == d
e['conclusion'] = {k:r['result'][k] for k in ('differential_uniformity','differential_witness','binary_pn','binary_square_apn','permutation')}
e['independent_checks'] = {'direct_ddt':True,'all_row_sums_8':all(sum(row)==8 for row in d),'nonzero_rows_even':all(v%2==0 for row in d[1:] for v in row)}

e,r = run(4, 'n4m1 指定表 Bent及对偶', ['bent-dual'], {'n':4,'m':1,'table':bent})
q = r['result']; dual=q['dual_table']; wd=direct_walsh(dual)
assert q['bent'] and all(abs(v)==4 for v in direct_walsh(bent))
assert [int(v<0) for v in wd]==bent
e['conclusion'] = {'bent':True,'nonlinearity':q['nonlinearity'],'dual_table':dual,'self_dual':dual==bent}
e['independent_checks'] = {'direct_flat_spectrum':True,'dual_bent':all(abs(v)==4 for v in wd),'double_dual_returns_input':True}

e,r = run(5, '第3表测本书几乎Bent', ['square-almost-bent'], {'n':3,'m':3,'table':cube})
spectra = {str(b):direct_walsh([(b&v).bit_count()%2 for v in cube]) for b in range(1,8)}
assert all(r['result']['components'][b]['walsh']==w for b,w in spectra.items())
assert all(v in (0,4,-4) for w in spectra.values() for v in w)
e['conclusion'] = {'square_almost_bent':r['result']['square_almost_bent'],'nonlinearity':r['result']['nonlinearity'],'all_7_component_spectra':spectra,'scope':'本书向量AB；方形奇维合同，未以APN代替AB。'}
e['independent_checks'] = {'all_nonzero_components_direct_walsh':True,'all_values_zero_or_plus_minus_4':True}

parity = [x.bit_count()%2 for x in range(16)]
e,r = run(6, 'n4奇偶表CI与弹性', ['resiliency'], {'n':4,'m':1,'table':parity})
assert direct_walsh(parity)==[0]*15+[16]
e['conclusion'] = {k:r['result'][k] for k in ('balanced','correlation_immunity_order','resiliency_order')}
e['independent_checks'] = {'all_spectral_mass_at_weight_4':True,'uniform_projection_up_to_3':all(len(set(sum(parity[x] for x in range(16) if (x&mask)==a) for a in range(16) if a&mask==a))==1 for mask in range(16) if mask.bit_count()<=3)}

e,r = run(7, 'n2 [0,0,0,1] 精确AI与零化子', ['scalar-ai'], {'n':2,'m':1,'table':f,'ai':True})
q = r['result']['algebraic_immunity']; g=q['witness_table']
target=f if q['annihilates']=='f' else [1-v for v in f]
assert any(g) and not any(a*b for a,b in zip(target,g)) and q['value']==1
e['conclusion'] = q
e['independent_checks'] = {'nonzero_witness':True,'annihilator_product_zero':True,'degree_0_impossible_both_sides':any(f) and not all(f),'reported_monomials_evaluate_to_witness':all(sum((x&mask)==mask for mask in q['monomial_masks'])%2==g[x] for x in range(4))}

e,r = run(8, '构造6变量例4.1型Bent', ['paired-bent','bent-dual'], paired=6)
q=r['result']; t=r['input']['table']
assert len(t)==64 and all(abs(v)==8 for v in direct_walsh(t)) and q['nonlinearity']==28
assert t==[((x>>3)&(x&7)).bit_count()%2 for x in range(64)]
e['conclusion'] = {'formula':'x1*x4 + x2*x5 + x3*x6 (F2)','bent':q['bent'],'nonlinearity':q['nonlinearity'],'weight':q['weight'],'table':t,'classification':'B:原书例4.1配对乘积；D:本次有限表生成与独立复算。'}
e['independent_checks'] = {'table_matches_formula':True,'direct_flat_spectrum':True,'required_NL_28':True}

e,r = run(9, 'n7全零表请求精确AI', ['scalar-ai'], {'n':7,'m':1,'table':[0]*128,'ai':True})
e['conclusion'] = {'runtime_AI':r['result']['algebraic_immunity'],'action':'依工具合同停止精确AI计算；not_computed不是0。另据定义，零函数可由非零常数1零化，数学上AI=0；此为解析结论，非工具计算结果。'}
assert r['result']['algebraic_immunity']['status']=='not_computed'

e,r = run(10, 'n2m2 [0,0,3,3] 坐标均平衡可否称向量弹性', ['resiliency'], {'n':2,'m':2,'table':[0,0,3,3]})
q=r['result']; assert q['components']['1']['balanced'] and q['components']['2']['balanced'] and not q['components']['3']['balanced']
e['conclusion'] = {'vector_resiliency_order':q['resiliency_order'],'answer':'不能。掩码3对应两个坐标之和，恒零，不平衡；故非向量弹性。','component3':q['components']['3']}
e['independent_checks'] = {'component3_is_constant_zero':all(((3&v).bit_count()%2)==0 for v in [0,0,3,3])}

note(11,'未给维数/域模型判断x^3是否APN',['binary-differential'],'输入不足：请求域特征、n与映射域/陪域；如要生成完整表还需模多项式及基/编码。当前不能给无条件APN结论或运行表工具。', 'needs_input')
note(12,'解释本书三种向量AI',['scalar-ai','glossary §§19–21'],{'basic':'AI(F)=min_a AI(F^{-1}(a)); AI(S)为在纤维S上恒零的非零n元布尔函数最小次数；空纤维允许常1、值0。','graph':'AI_gr(F)=min deg g(x,y)，g为非零n+m元布尔函数，且g(x,F(x))恒为0。','component':'AI_comp(F)=min_{v!=0} AI(v·F)，此处AI为双侧标量AI；必须遍历全部非零组合，不能只算坐标。','boundary':'三个搜索对象不同，不能将分量AI报告冒充基本AI/图形AI；本工具仅提供逐分量标量AI。','source':'本地词典，定义7.4/7.5及定理7.26，书pp265–266；未独立核原页。'})
note(13,'帮我修React布局是否调用技能',['not_applicable'],'不调用本密码函数技能；进入普通React工程排查，需要相关组件/样式/页面上下文。')
note(14,'证明新S-box整个加密系统安全',['out_of_scope'],'不接受以有限S-box指标证明整个加密系统安全。需明确定义系统构造、攻击模型、安全目标与假设，再转交对应密码学证明/分析工作；若另给完整S-box表可单独复算本技能覆盖的指标，结果不等价系统安全证明。')

payload = {'evaluation':'independent real-task exercise, no tests or expected-answer files read',
           'environment':{'python':PY,'version':platform.python_version()},
           'bit_order_assumption':'依技能默认：整数递增索引，x1最高位；所有请求显式声明该约定。',
           'records':records,
           'summary':{'requests_handled':14,'calculator_tasks_completed':10,'calculator_command_failures':0,'missing_input_stops':1,'explanations_or_scope_responses':3,'independent_assertions_passed':True},
           'findings':[{'severity':'limitation','detail':'n=7零函数可立即解析得AI=0，但精确AI工具机械按n>6返回not_computed。严格遵守预算时应区分解析结论与工具结果；不是数值错误。'},
                       {'severity':'minor_usability','detail':'AI卡说低次数满列秩为最小性依据，但输出未列逐度秩数据；本次AI=1通过两侧无常数零化子独立核最小性。'},
                       {'severity':'coverage_boundary','detail':'三种向量AI在词典可解释，运行器不算basic/graph；输入不全与系统安全请求均正确判停。'}]}
(OUT/'blind-outputs.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
print(json.dumps(payload['summary'],ensure_ascii=False))
