# 复现与使用

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
