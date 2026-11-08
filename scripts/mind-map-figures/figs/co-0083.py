LABEL = 'CPU 访问主存地址的过程（全相联映射）'
F = Fig(760, 380, 'CPU 访问主存地址')
F.text(60, 76, '有效位', 12.5, color=ACCENT['red'], weight=600); F.text(160, 76, '标记（22 位）', 12.5, color=ACCENT['blue'], weight=600); F.text(240, 76, '行号', 12.5, color=MUTED); F.text(300, 76, 'Cache', 12.5, color=INK, weight=600)
for i in range(8):
    y = 88 + i * 32
    v, tg = {1: ('1', '1…1101'), 3: ('1', '0…0000')}.get(i, ('0', '−'))
    F.text(60, y + 16, v, 13, color=ACCENT['red'], mono=True, valign='middle'); F.text(160, y + 16, tg, 12.5, color=ACCENT['blue'], mono=True, valign='middle')
    F.text(240, y + 16, str(i), 12, color=MUTED, mono=True, valign='middle')
    F.box(270, y, 80, 32, '64B' if i in [1, 3] else '', {1: 'violet', 3: 'green'}.get(i, 'white'), 12, 0)
F.text(310, 360, 'Cache：8 × 64B = 512 B', 12.5, color=INK2)
F.text(450, 92, 'CPU 访问主存地址', 13, 'start', INK, 700)
F.text(450, 118, '1…1101 001110', 13, 'start', ACCENT['blue'], mono=True)
F.text(450, 150, '① 主存地址的前 22 位与 Cache 中', 12.5, 'start', INK2)
F.text(450, 174, '\u3000 所有行的标记比较', 12.5, 'start', INK2)
F.text(450, 198, '② 若标记匹配且有效位 = 1，则 Cache', 12.5, 'start', INK2)
F.text(450, 222, '\u3000 命中，访问块内地址为 001110 的单元', 12.5, 'start', INK2)
F.text(450, 246, '③ 若未命中或有效位 = 0，则正常访问主存', 12.5, 'start', INK2)
