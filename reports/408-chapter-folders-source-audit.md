# 408 章节目录与原始导图复核

本次把 402 个独立小节放入所属的 26 个章节目录，4 个学科目录下仅保留学科首页与章节目录。每章以 `index.mdx` 作为总览，`meta.json` 明确列出小节数字顺序，章节默认收起。上下页导航在章内按总览、1、2、…、10排序，章节总览可以返回学科首页，小节可以返回章节总览。

例如：

```text
computer-networks/
  index.mdx
  02-physical-layer/
    index.mdx
    meta.json
    02-1-role-interface.mdx
    02-2-communication-modes.mdx
    02-3-symbol-rate.mdx
```

章节总览的原网址保持不变。402 个旧小节网址通过精确 301 跳转至新的章节内地址；同时覆盖带/不带尾斜杠及 Markdown 下载地址，共 1,206 条静态规则，低于 Cloudflare 的 2,000 条上限。原有 RSC 内部重写保持独立，无跳转链、循环或通配覆盖。对应表见 [legacy-routes.json](../lib/mind-map/legacy-routes.json)。

## 原始来源与内容核对

原始文件来自用户指定的 [Drive 408 文件夹](https://drive.google.com/drive/folders/1ZYpJh3nauAHnw8YQt07YRGidpWh9n5RD)：数据结构、计算机网络、操作系统及“推荐”计算机组成原理 XMind，共4份。使用新版 `content.json`；包内 `content.xml` 是旧版兼容警告页，不能用它判断实际导图内容。

- 4 份归档均通过 ZIP CRC 检查；共遍历 9,592 个主题节点，911 处主题图片引用均能找到包内资源。
- 逐章把176个非 END 的主要分支对应到网站的真实小节，包含数据结构源文件中合在同一画布的第二、三章。对应关系、源文件 SHA-256 和 Drive 文件 ID 见 [408-source-audit.json](./408-source-audit.json)。
- 核对范围为主要知识分支、图片依赖及代表性计算，不把重写后的小节宣称为全部叶节点逐字复制；已纠正的原文概念错误继续保持纠正。
- 源 XMind 存在5处过期内部主题链接，涉及内存管理、磁盘调度、ARP及RIP。这些 XMind ID 未作为网页依赖；当前对应站内地址均有效，并补充 I/O 软件层次到磁盘调度、NAT到ARP的关联链接。
- 独立重算6组正文实例：UDP反码校验和、CRC余数、FIFO的Belady反例、三对角矩阵压缩与逆映射、银行家安全序列、多体交叉存储时间。实际数值与正文一致；计算回归见 `tests/408-content-calculations.test.ts`。

## SVG 与站内依赖

- 共612张SVG；497个不同文件在正文中出现513次；其余115张是已记录重绘替代关系的源图，继续保留。
- 全量检查 SVG XML、正值 viewBox、重复ID、`href`/`url(#...)`引用、CSS外部导入及外部资源依赖，未发现缺失依赖。
- 所有正文图片均存在；逐图迁移记录已改为新的章节内文件路径，原始章节位置保留为来源证据。
- [依赖检查结果](./408-asset-dependency-audit.json) 可用 `python3 scripts/audit-408-mind-map-assets.py` 重验，已加入部署前检查。
- 检查真实 Fumadocs 页面树：每个学科仅有一个总览页和章节文件夹，全部小节在所属章节之内；所有导图继续保持双侧布局配置，解析后图片引用完整保留。

完整构建和部署使用现有 GitHub Actions 工作流，未在本地执行完整网站构建。发布后检查新旧网址、小节跳转、章节侧栏、双侧布局和图片放大，再发送完成通知。
