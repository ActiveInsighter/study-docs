LABEL = 'CPU 访问主存地址的过程（直接映射）'
F = Fig(760, 380, 'CPU 访问主存地址')
F.text(60, 76, '有效位', 12.5, color=ACCENT['red'], weight=600); F.text(160, 76, '标记（19 位）', 12.5, color=ACCENT['blue'], weight=600); F.text(240, 76, '行号', 12.5, color=MUTED); F.text(300, 76, 'Cache', 12.5, color=INK, weight=600)
for i in range(8):
    y = 88 + i * 32
    v, tg = {0: ('1', '0…01')}.get(i, ('0', '−'))
    F.text(60, y + 16, v, 13, color=ACCENT['red'], mono=True, valign='middle'); F.text(160, y + 16, tg, 12.5, color=ACCENT['blue'], mono=True, valign='middle')
    F.text(240, y + 16, str(i), 12, color=MUTED, mono=True, valign='middle')
    F.box(270, y, 80, 32, '64B' if i in [0] else '', {0: 'red'}.get(i, 'white'), 12, 0)
F.text(310, 360, 'Cache：8 × 64B = 512 B', 12.5, color=INK2)
F.text(450, 92, 'CPU 访问主存地址', 13, 'start', INK, 700)
F.text(450, 118, '0…01[[amber:000]]001110', 13, 'start', ACCENT['blue'], mono=True)
F.text(450, 150, '① 根据主存块号的后 3 位确定 Cache 行', 12.5, 'start', INK2)
F.text(450, 174, '② 若主存块号的前 19 位与该行标记', 12.5, 'start', INK2)
F.text(450, 198, '\u3000 匹配且有效位 = 1，则 Cache 命中，', 12.5, 'start', INK2)
F.text(450, 222, '\u3000 访问块内地址为 001110 的单元', 12.5, 'start', INK2)
F.text(450, 246, '③ 若未命中或有效位 = 0，则正常访问主存', 12.5, 'start', INK2)
