LABEL = '微地址形成部件：根据 IR 中的 OP 给出该指令微程序的入口地址'
F = Fig(460, 260, '微地址形成部件')
F.box(60, 60, 80, 44, 'OP', 'blue', 16, 0, True); F.box(140, 60, 220, 44, '', 'blue', rx=0); F.text(380, 82, 'IR', 15, 'start', INK, 700, valign='middle')
F.line(100, 106, 100, 136, INK2, 1.6, arrow='end')
F.box(80, 138, 240, 60, '微地址形成部件', 'amber', 16, 6)
F.line(200, 200, 200, 236, INK2, 1.6, arrow='end'); F.text(210, 226, '微程序入口地址 → CMAR', 12, 'start', INK2)
