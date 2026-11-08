LABEL = 'CPU 访问主存地址的过程（2 路组相联映射）'
F = Fig(760, 380, 'CPU 访问主存地址')
F.text(60, 76, '有效位', 12.5, color=ACCENT['red'], weight=600); F.text(160, 76, '标记（20 位）', 12.5, color=ACCENT['blue'], weight=600); F.text(240, 76, '行号', 12.5, color=MUTED); F.text(300, 76, 'Cache', 12.5, color=INK, weight=600)
for i in range(8):
    y = 88 + i * 32
    v, tg = {2: ('1', '1…11'), 3: ('1', '0…00')}.get(i, ('0', '−'))
    F.text(60, y + 16, v, 13, color=ACCENT['red'], mono=True, valign='middle'); F.text(160, y + 16, tg, 12.5, color=ACCENT['blue'], mono=True, valign='middle')
    F.text(240, y + 16, str(i), 12, color=MUTED, mono=True, valign='middle')
    F.box(270, y, 80, 32, '64B' if i in [2, 3] else '', {2: 'green', 3: 'red'}.get(i, 'white'), 12, 0)
for g in range(4): F.brace(352, 352, 0) if False else F.vbrace(354, 90 + g * 64, 150 + g * 64, f'第 {g} 组', color=ACCENT['amber'])
F.text(310, 360, 'Cache：8 × 64B = 512 B', 12.5, color=INK2)
F.text(450, 92, 'CPU 访问主存地址', 13, 'start', INK, 700)
F.text(450, 118, '1…111[[amber:01]]001110', 13, 'start', ACCENT['blue'], mono=True)
F.text(450, 150, '① 根据主存块号的后 2 位确定 Cache 组号', 12.5, 'start', INK2)
F.text(450, 174, '② 遍历该组中的所有行：前 20 位与', 12.5, 'start', INK2)
F.text(450, 198, '\u3000 某行标记匹配且有效位 = 1，则命中，', 12.5, 'start', INK2)
F.text(450, 222, '\u3000 访问块内地址为 001110 的单元', 12.5, 'start', INK2)
F.text(450, 246, '③ 若未命中或有效位 = 0，则正常访问主存', 12.5, 'start', INK2)
