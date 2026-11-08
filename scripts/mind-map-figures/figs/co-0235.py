from common import instr, memcol
LABEL = '隐含寻址：另一个操作数隐含在 ACC 中'
F = Fig(620, 280, '隐含寻址')
c = instr(F, 30, 80, 'ADD', '', 'A')
F.poly([c, (c[0], 124), (250, 124)], INK2, 1.3, arrow='end'); F.text(256, 124, 'A', 13, 'start', INK, mono=True, valign='middle')
memcol(F, 280, 100, ['操作数', ''], 90)
F.box(450, 70, 60, 30, 'ACC', 'amber', 13, 4, True)
F.items.append('<path d="M410 170H510L492 196H428Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.3"/>'); F.text(460, 182, 'ALU', 12, color='#7f1d1d', weight=700, valign='middle')
F.poly([(325, 100), (325, 80), (430, 80), (430, 168)], INK2, 1.2, arrow='end'); F.line(480, 102, 480, 168, INK2, 1.2, arrow='end')
F.box(430, 216, 60, 28, '暂存', 'white', 12, 4); F.line(460, 198, 460, 214, INK2, 1.2, arrow='end')
F.poly([(460, 246), (460, 262), (560, 262), (560, 56), (480, 56), (480, 68)], INK2, 1.2, arrow='end')
F.text(30, 160, '另一个操作数隐含在 ACC 中', 12.5, 'start', INK2)
F.text(30, 186, 'EA = A，另一操作数 = (ACC)', 12.5, 'start', ACCENT['blue'], mono=True)
