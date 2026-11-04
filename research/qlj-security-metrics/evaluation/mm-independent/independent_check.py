from pathlib import Path
import itertools,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
TOOL=ROOT/'skills/qlj-security-metrics/resources/mm_construction.py'
def calc(pi,g):
 size=len(pi);h=(size-1).bit_length();t=[((x&pi[y]).bit_count()%2)^g[y] for x in range(size) for y in range(size)]
 w=[sum((-1)**(v+((z&a).bit_count()%2)) for z,v in enumerate(t)) for a in range(len(t))]
 return t,w
cases=[('permutation-nonlinear-g',[2,0,3,1],[0,1,1,0]),('reverse-and-constant',[3,2,1,0],[1,1,1,1]),('invalid-repeated-pi',[0,0,2,3],[0,0,0,0])]
records=[]
for name,pi,g in cases:
 t,w=calc(pi,g); inp=OUT/(name+'-input.json');result=OUT/(name+'-result.json');inp.write_text(json.dumps(dict(h=2,pi=pi,g=g)),encoding='utf-8')
 cmd=[sys.executable,str(TOOL),'--input',str(inp),'--out',str(result)]
 run=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8'); valid=len(set(pi))==4
 if valid:
  assert run.returncode==0,run.stderr
  actual=json.loads(result.read_text(encoding='utf-8'))
  assert actual['function']['table']==t
  assert actual['analysis']['result']['walsh']==w
  assert actual['certificate']['predicted_walsh']==w
  assert set(map(abs,w))=={4}
 else:
  assert run.returncode==2 and not result.exists()
  assert set(map(abs,w))!={4}
 records.append(dict(name=name,pi=pi,g=g,independent_table=t,independent_walsh=w,independent_nonlinearity=8-max(map(abs,w))//2,exit_code=run.returncode,stderr=run.stderr,expected_contract_valid=valid))
for pi in itertools.permutations(range(4)):
 for g in itertools.product(range(2),repeat=4):
  t,w=calc(pi,g); assert set(map(abs,w))=={4}
summary=dict(python=sys.version,cases=records,independent_exhaustive_h2_cases=384,independent_exhaustive_status='PASS',source='QLJ2011 book p113 / PDF123',scope='direct character sums; no runtime module imported')
(OUT/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS 384 independent h2 examples; 2 valid CLI, 1 invalid CLI')
