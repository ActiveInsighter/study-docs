from common import instr, memcol
LABEL = '寄存器寻址：EA = Ri，操作数在寄存器中'
F = Fig(460, 330, '寄存器寻址：EA = Rᵢ')
c = instr(F, 40, 80, 'OP', '', 'Rᵢ', (70, 60, 60), 34)
memcol(F, 240, 140, ['⋮', '⋮', '操作数', '⋮'], 110, 34, title='寄存器', hl={2: 'blue'}, labels={0: 'R₀', 2: 'Rᵢ', 3: 'Rₙ'})
F.poly([c, (c[0], 126), (80, 126), (80, 225), (212, 225)], INK2, 1.3, arrow='end')
F.text(230, 310, '不访存，速度快；但寄存器数目有限', 12, color=MUTED)
