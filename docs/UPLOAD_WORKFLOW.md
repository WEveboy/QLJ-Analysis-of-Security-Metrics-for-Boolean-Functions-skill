# 本仓库更新流程

1. 读取远端main最新SHA和文件树；保留远端已有文件，禁止强推覆盖。
2. 仅上传规范能力包、来源审计、人工源码、测试、范例与CI。不上传原书PDF、页图、OCR全文、缓存、凭证或构建临时目录。
3. 修改源Bundle及生成脚本后，用cangjie-skill 2.5.0编译；不得手改生成目录。
4. 运行标准库单元测试、CLI案例、cangjie格式/引用验证与实际输出评测。校验哈希不代替数学证明。
5. 原子提交后核对SHA与文件清单，等待CI；修复失败后再交付。
6. 本仓库不产Windows EXE，本次不创建EXE Release。无新增LICENSE；原著权益不转授。

后续操作以本技能独立仓库目录为根，避免在同工作区程序目录生成同名README或CI。发布前用validate_release.py生成日志；CI附带两版Python的validation.json下载资产。
