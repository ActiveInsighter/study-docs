from common import instr, memcol
LABEL = '寄存器间接寻址：EA = (Ri)，寄存器中存操作数地址'
F = Fig(560, 330, '寄存器间接寻址：EA = (Rᵢ)')
c = instr(F, 30, 80, 'OP', '', 'Rᵢ', (60, 50, 50), 30)
memcol(F, 200, 130, ['⋮', '⋮', 'EA', '⋮'], 90, 32, title='寄存器', hl={2: 'amber'}, labels={0: 'R₀', 2: 'Rᵢ', 3: 'Rₙ'})
F.poly([c, (c[0], 120), (60, 120), (60, 210), (170, 210)], INK2, 1.3, arrow='end')
memcol(F, 400, 100, ['', '', '', '操作数', ''], 100, 32, hl={3: 'blue'})
F.line(292, 210, 398, 212, INK2, 1.3, arrow='end')
F.text(280, 316, '只需一次访存（寄存器中的地址可扩大寻址范围）', 12, color=MUTED)
