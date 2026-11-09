from common import instr, memcol
LABEL = '直接寻址：EA = A，一次访存取得操作数'
F = Fig(560, 252, '直接寻址：EA = A')
c = instr(F, 30, 90, 'LDA', '', 'A', (80, 70, 70), 36)
F.poly([c, (c[0], 160), (300, 160)], INK2, 1.3, arrow='end'); F.text(306, 160, 'A', 13, 'start', INK, mono=True, valign='middle')
memcol(F, 330, 120, ['', '操作数', ''], 100, 30)
F.box(470, 120, 60, 32, 'ACC', 'amber', 13, 4, True); F.poly([(432, 165), (500, 165), (500, 154)], INK2, 1.2, arrow='end')
F.text(280, 240, '只需一次访存；寻址范围受 A 的位数限制', 12, color=MUTED)
