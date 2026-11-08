from common import instr, memcol
LABEL = '基址寻址：EA = (BR) + A，可用专用基址寄存器或通用寄存器'
F = Fig(800, 300, '基址寻址：EA = (BR) + A')
for k, x in enumerate((20, 410)):
    c = instr(F, x + 60, 80, 'OP', '', 'A' if k == 0 else 'R₀ | A', (50, 40, 60 if k == 0 else 80), 28)
    F.items.append(f'<path d="M{x + 120} 170H{x + 210}L{x + 194} 194H{x + 136}Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.3"/>'); F.text(x + 165, 181, 'ALU', 11.5, color='#7f1d1d', weight=700, valign='middle')
    F.line(c[0] if k == 0 else x + 210, c[1], x + 180, 168, INK2, 1.2, arrow='end')
    if k == 0:
        F.box(x, 150, 50, 26, 'BR', 'violet', 12, 4, True); F.poly([(x + 25, 176), (x + 25, 190), (x + 100, 190), (x + 100, 160), (x + 140, 160), (x + 140, 168)], INK2, 1.2, arrow='end')
        F.text(x + 150, 270, '(a) 专用基址寄存器 BR', 12.5, color=INK2)
    else:
        memcol(F, x, 140, ['', '基址', '⋮'], 70, 24, title='通用寄存器', labels={0: 'R₀'})
        F.poly([(x + 150, 108), (x + 150, 124), (x - 10, 124), (x - 10, 152), (x - 2, 152)], INK2, 1.2, arrow='end')
        F.poly([(x + 70, 176), (x + 140, 176), (x + 140, 168)], INK2, 1.2, arrow='end')
        F.text(x + 150, 270, '(b) 通用寄存器 R₀ 作基址寄存器', 12.5, color=INK2)
    memcol(F, x + 260, 90, ['', '', '操作数', ''], 90, 30, hl={2: 'blue'})
    F.poly([(x + 165, 196), (x + 165, 225), (x + 230, 225), (x + 230, 165), (x + 258, 165)], INK2, 1.2, arrow='end')
F.text(400, 294, 'BR 由操作系统管理，A 可变：便于多道程序的浮动（编制浮动程序）', 12, color=MUTED)
