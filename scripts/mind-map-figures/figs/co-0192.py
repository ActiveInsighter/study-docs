from common import instr, memcol
LABEL = '相对寻址：EA = (PC) + A，A 为补码偏移量'
F = Fig(620, 300, '相对寻址：EA = (PC) + A')
c = instr(F, 160, 80, 'OP', '', 'A', (60, 50, 60), 30)
F.cells(40, 120, ['1002'], 60, 26, {0: 'violet'}, size=12); F.text(32, 133, 'PC', 12.5, 'end', INK, valign='middle')
F.text(70, 166, '取指后 PC 已自增\n（指向下一条指令）', 11.5, 'middle', MUTED, lh=1.4)
F.items.append('<path d="M180 210H280L262 236H198Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.3"/>'); F.text(230, 222, 'ALU', 12, color='#7f1d1d', weight=700, valign='middle')
F.poly([(70, 146), (70, 196), (200, 196), (200, 208)], INK2, 1.2, arrow='end'); F.line(c[0], c[1], c[0], 208, INK2, 1.2, arrow='end')
memcol(F, 380, 90, ['OP A', '⋮', '操作数', ''], 110, 32, hl={2: 'blue'}, labels={0: '1000'})
F.poly([(230, 238), (230, 266), (340, 266), (340, 170), (378, 170)], INK2, 1.2, arrow='end')
F.vbrace(494, 90, 168, '相对距离 A')
F.text(310, 292, '便于程序浮动，常用于转移指令；A 可正可负', 12, color=MUTED)
