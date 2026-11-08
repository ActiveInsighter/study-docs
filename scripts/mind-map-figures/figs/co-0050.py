from common import instr, memcol
LABEL = '变址寻址：EA = (IX) + A，IX 可由用户改变'
F = Fig(560, 280, '变址寻址：EA = (IX) + A')
c = instr(F, 140, 80, 'OP', '', 'A', (60, 50, 60), 30)
F.box(30, 170, 60, 30, 'IX', 'violet', 13, 4, True)
F.items.append('<path d="M180 160H290L270 190H200Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.3"/>'); F.text(235, 174, 'ALU', 12, color='#7f1d1d', weight=700, valign='middle')
F.line(c[0], c[1], c[0], 158, INK2, 1.2, arrow='end'); F.poly([(60, 168), (60, 140), (205, 140), (205, 158)], INK2, 1.2, arrow='end')
memcol(F, 380, 80, ['', '', '操作数', ''], 100, 32, hl={2: 'blue'})
F.poly([(235, 192), (235, 226), (350, 226), (350, 160), (378, 160)], INK2, 1.2, arrow='end')
F.text(280, 268, 'A 不变、IX 可变：适合处理数组、编写循环程序', 12, color=MUTED)
