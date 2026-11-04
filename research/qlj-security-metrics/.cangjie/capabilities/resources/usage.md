# 执行合同
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
