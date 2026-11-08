LABEL = '主存由 RAM 和 ROM 组成，ROM 中存放 BIOS（含自举程序）'
F = Fig(460, 410, 'RAM 与 ROM')
F.box(30, 160, 80, 60, 'CPU', 'amber', 15, 6)
F.box(180, 60, 140, 220, 'RAM', 'amber', 17, 0); F.box(180, 280, 140, 100, 'ROM（BIOS）\n包含 ROM 引导\n程序，即自举程序', 'blue', 12, 0)
F.text(340, 150, '内存条', 14, 'start', ACCENT['red'], 700); F.text(170, 330, '低\n地\n址', 13, 'end', ACCENT['red'], 700, lh=1.2, valign='middle')
F.text(110, 270, '主板', 14, 'middle', ACCENT['red'], 700); F.line(178, 300, 124, 278, ACCENT['red'], 1.2, arrow='end')
F.text(250, 396, '主存', 13, color=ACCENT['red'], weight=700)
