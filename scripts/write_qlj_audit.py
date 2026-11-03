from pathlib import Path
import json, hashlib
from build_qlj_bundle import CARDS

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'research/qlj-security-metrics'

def write(name,text):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')

def main():
    write('research/qlj-security-metrics/verified.md',
        '# 三重验证与晋级评审\n\nV1按候选记录核读页图；V2用新输入有限复算；V3为可检查的规格统一与条件防遗漏，不宣称模型能力显著提高。\n\n'+
        '| canonical ID | V1 来源 | V2 实算 | V3 收益 | 去向 |\n|---|---|---|---|---|\n'+
        '\n'.join(f'| cap.qlj.{slug} | {src} | test_metrics.py及阶段4输出 | {title}口径一致 | single路由卡 |'
                  for slug,title,src,*_ in CARDS)+
        '\n\n阶段1.6：8项均有独立意图和契约，可复用且可评测；共享表示和计算器，independent_run=false，因此全部router，无独立晋级。\n'+
        '候选池并集去重，五视角不是五个独立来源。sources为唯一原书；短引用不能代替完整条件。\n')
    gaps=[
        ('T04','§1.6—1.7 pp12—18','迹表示、RM与码桥','reference','词典/overview；未实现域模型或码计算'),
        ('T05/T14','§2.2—2.5 pp27—67','PN原像分布、构造、等价、码应用','needs_review','参数与证明未逐式复核，不进active'),
        ('T06','§3.2—3.4 pp80—100','APN族与EA/CCZ','needs_review','只检测给定表；族参数和未知等价搜索未实现'),
        ('T07','§4.3—4.5 pp112—124','MM/PS/间接构造、等价类计数','needs_review','仅例4.1构造激活'),
        ('T08','§5.2—5.4 pp133—144','一般SCV界、AB构造与等价刻画','needs_review','只激活方形奇维AB检测，保留(2,1)例外'),
        ('T10','§6.2—6.5 pp156—195','标量/向量弹性构造与计数','needs_review','参数与计数公式未逐式复核'),
        ('T11','§7.2—7.3 pp210—264','支撑/平面/交换基/对称MAI构造','needs_review','不从章标题补成构造程序'),
        ('T12','§7.4 pp265—270','基本、图形、组件三种向量AI','reference/needs_review','定义入词典；只返回分量标量AI，不实现三个向量AI'),
        ('T13','§2.4/3.4/4.5','EA/CCZ/仿射等价','reference','谱相同不能给等价证书；Bent章节仿射口径另列词典'),
    ]
    table='| 任务 | 原书位置 | 候选/主题 | 判定 | 实际去向/缺口 |\n|---|---|---|---|---|\n'+\
        '\n'.join('| '+' | '.join(row)+' |' for row in gaps)+'\n'
    write('research/qlj-security-metrics/needs-review.md','# 待审清单\n\n下列重要机制已检索定位，未达到可执行来源门。它们不是本版已交付能力。\n\n'+table)
    write('research/qlj-security-metrics/references.md','# 参考内容映射\n\n'+table+
        '\n参考最终进入skills/qlj-security-metrics/references/overview.md与glossary.md。待审条目在overview显式披露，不把其标题当公式实现。\n')
    write('research/qlj-security-metrics/coverage-audit.md','# 覆盖审计\n\n'+
        '源文件286页均已本地OCR，共327380字符（含识别空格）；框架/反例/术语作全书检索，原则关键页图核读，案例核读32页。\n'+
        '这不是286页全文逐句精读，更不是全书全部证明完成。各提取器记录实际范围。\n\n'+
        '| 任务 | 原子执行去向 |\n|---|---|\n'+
        '| T01 | representation |\n| T02 | walsh-nonlinearity |\n| T03/T05/T06 | binary-differential（仅二元） |\n'+
        '| T07 | bent-dual、paired-bent |\n| T08 | square-almost-bent（仅方形奇维） |\n| T09 | resiliency |\n| T11 | scalar-ai（仅n≤6） |\n\n'+table+
        '\n“有去向”只指无静默遗漏，不能宣称所有任务已实现。\n')
    overview=(BOOK/'BOOK_OVERVIEW.md').read_text(encoding='utf-8-sig')
    if '## 参考和待审' not in overview:
        (BOOK/'BOOK_OVERVIEW.md').write_text(overview+'\n## 参考和待审\n\n'+table+
            '\n本轮为research-draft-0.1.0，保留全书主题入口，仅激活核图及实测通过的8卡。未完成全书逐定理核验或新旧技能模型效果对照。\n',encoding='utf-8')
    write('research/qlj-security-metrics/rejected/unsupported-claims.md',
        '# 淘汰项\n\nR01：整书所有构造均已实现——不实，淘汰。\nR02：AI/δ/NL单项最优推出系统安全——来源不支持，淘汰。\n'+
        'R03：所有二元PN不存在——遗漏方形条件，改由binary-differential纠正。\nR04：标量semi-bent等于本书AB——错误归类，淘汰。\n')
    write('docs/UPLOAD_WORKFLOW.md', '''# 本仓库更新流程

1. 读取远端main最新SHA和文件树；保留远端已有文件，禁止强推覆盖。
2. 仅上传规范能力包、来源审计、人工源码、测试、范例与CI。不上传原书PDF、页图、OCR全文、缓存、凭证或构建临时目录。
3. 修改源Bundle及生成脚本后，用cangjie-skill 2.5.0编译；不得手改生成目录。
4. 运行标准库单元测试、CLI案例、cangjie格式/引用验证与实际输出评测。校验哈希不代替数学证明。
5. 原子提交后核对SHA与文件清单，等待CI；修复失败后再交付。
6. 本仓库不产Windows EXE，本次不创建EXE Release。无新增LICENSE；原著权益不转授。
''')
    write('docs/REPRODUCE.md','''# 复现与使用

Python 3.10+即可运行已编译技能，不需第三方包。使用：

```powershell
python skills/qlj-security-metrics/resources/runtime_metrics.py --input examples/gold-3.json --out gold-result.json
python skills/qlj-security-metrics/resources/runtime_metrics.py --paired-bent 4 --out bent-result.json
python -m unittest discover -s skills/qlj-security-metrics/resources -p test_metrics.py -v
```

输出路径必须尚不存在。输入字段与预算见技能resources/usage.md。
将skills/qlj-security-metrics整个目录复制到宿主技能目录；本次只按用户请求发布GitHub，不改本机已安装技能。

作者端复现需安装cangjie-skill 2.5.0及PyYAML/jsonschema：

```powershell
python scripts/build_qlj_bundle.py
python <cangjie-skill>/scripts/cangjie.py compile --bundle research/qlj-security-metrics/.cangjie/capabilities --out <新输出目录>/qlj-security-metrics --output single
python <cangjie-skill>/scripts/validate_skill_pack.py <新输出目录>/qlj-security-metrics
```

编译器不会从PDF自动生成方法论；本库的Bundle来自人工/代理提取与核验。
同一Bundle可确定性生成single产物，时间戳、运行ID等构建元数据会不同。
源文件PDF及OCR不分发；根据source-manifest.json的SHA256核对本地合法来源。
''')
    write('README.md','''# 密码函数的安全性指标分析 · 科研技能

基于李超、屈龙江、周悦《密码函数的安全性指标分析》（科学出版社，2011），按原“Boolean-vector-research-skill生成”项目的 **cangjie-skill 2.5.0 / RIA-TV++** 流程蒸馏。

**研究初稿0.1.0：1个入口、8张能力卡、Python标准库有限表计算器。** 已进行全书OCR检索、关键页图核对、五视角候选提取、三重验证、路由编译及有限输出测试。全书复杂构造与计数仍有待审项，不称全书定理库已完成。

- [技能入口](skills/qlj-security-metrics/SKILL.md)：表示/ANF、Walsh/NL、二元PN/APN、Bent对偶、方形奇维AB、弹性、标量AI、配对乘积Bent构造。
- [精华长文](research/qlj-security-metrics/DIGEST.md) · [全书骨架](research/qlj-security-metrics/BOOK_OVERVIEW.md) · [术语](research/qlj-security-metrics/GLOSSARY.md)
- [覆盖审计](research/qlj-security-metrics/coverage-audit.md) · [待审](research/qlj-security-metrics/needs-review.md) · [验证记录](research/qlj-security-metrics/test-results.md)
- [使用和复现](docs/REPRODUCE.md) · [后续上传规范](docs/UPLOAD_WORKFLOW.md)

```powershell
python skills/qlj-security-metrics/resources/runtime_metrics.py --input examples/gold-3.json
python skills/qlj-security-metrics/resources/runtime_metrics.py --paired-bent 4
```

精确AI限n≤6；标量n≤10；向量n≤8、m≤8。仅验证给定有限表，不替代系统安全评估、全族证明或最新研究查新。书中“几乎Bent”为向量AB；向量AI三定义不混用。

原书PDF、页图及全文OCR仅在本地取证，不随仓库分发。原著版权归权利人；未新增许可证。
本项目由WEveboy提出研究目标与维护；Codex协助蒸馏、工具实现和验证。
''')
    write('.gitignore','__pycache__/\n*.pyc\ntmp/\n.staging-*/\n*.pdf\n*.png\n*.jpg\n')
    write('examples/gold-3.json',json.dumps(dict(n=3,m=3,table=[0,1,3,4,5,6,7,2],ai=False),indent=2)+'\n')
    write('examples/bent-4.json',json.dumps(dict(n=4,m=1,table=[0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0],ai=True),indent=2)+'\n')
    write('examples/parity-4.json',json.dumps(dict(n=4,m=1,table=[x.bit_count()%2 for x in range(16)],ai=True),indent=2)+'\n')
    write('.github/workflows/ci.yml','''name: Skill validation
on: [push, pull_request]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.12']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m unittest discover -s skills/qlj-security-metrics/resources -p test_metrics.py -v
      - run: python scripts/check_repository.py
      - run: python skills/qlj-security-metrics/resources/runtime_metrics.py --input examples/gold-3.json --out gold-result.json
      - run: python skills/qlj-security-metrics/resources/runtime_metrics.py --paired-bent 4 --out bent-result.json
''')

if __name__=='__main__':main()
