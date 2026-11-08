LABEL = '操作系统引导步骤：BIOS 自检 → 读 MBR → 读分区引导记录 → 加载启动管理器与内核'
F = Fig(860, 300, '操作系统的引导')
F.box(30, 120, 50, 36, 'CPU', 'blue', 12, 4)
F.box(120, 60, 60, 120, 'RAM', 'amber', 12, 0); F.box(120, 180, 60, 70, 'ROM（BIOS）\n含 ROM\n引导程序', 'blue', 9.5, 0); F.text(150, 266, '主存', 11, color=ACCENT['red'])
F.line(80, 138, 118, 210, ACCENT['red'], 1.2, arrow='end'); F.text(92, 186, '①', 12, color=ACCENT['red'])
F.text(250, 210, '磁盘', 12, 'end', INK, 700, valign='middle')
F.box(260, 190, 160, 40, '主引导记录 MBR\n（磁盘引导程序、分区表）', 'white', 10.5, 0); F.box(420, 190, 200, 40, 'C 盘', 'green', 12, 0); F.box(620, 190, 160, 40, 'D 盘', 'green', 12, 0)
F.text(560, 62, 'UNIX 文件系统（C 盘活动分区）', 11.5, color=INK2, weight=600)
F.cells(420, 72, ['引导块', '超级块', '空闲空间管理', 'i 结点区', '根目录', '…'], [0] and 0, 0) if False else None
for i, (t, w) in enumerate((('引导块（负责\n初始化 OS）', 90), ('超级块', 60), ('空闲空间管理', 90), ('i 结点区', 90), ('根目录', 60))):
    F.box(420 + sum([90, 60, 90, 90, 60][:i]), 76, w, 44, t, 'amber' if i == 0 else 'white', 10, 0)
F.line(340, 188, 182, 160, ACCENT['red'], 1.2, arrow='end'); F.text(260, 162, '② 读 MBR，执行磁盘引导程序', 10.5, color=ACCENT['red'])
F.line(465, 122, 182, 110, ACCENT['red'], 1.2, arrow='end'); F.text(320, 102, '③ 读活动分区的引导块，加载 OS', 10.5, color=ACCENT['red'])
F.text(430, 290, '① CPU 执行 ROM 中的引导程序（自检）　② 读 MBR、扫描分区表　③ 从活动分区的引导记录加载启动管理器 → 内核', 11, color=MUTED)
