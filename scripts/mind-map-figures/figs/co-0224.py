LABEL = '主存块号 % 4 决定在 Cache 中的组号'
F = Fig(620, 624, '主存块号 % 4 = 组号')
pal = ['green', 'blue', 'amber', 'violet', 'red', 'teal', 'gray', 'light']
tone = lambda b: pal[b % 4] if 4 == 8 else ['amber', 'blue', 'green', 'red'][b % 4]
F.text(120, 80, 'Cache', 13, color=INK, weight=700)
F.rect(70, 90, 100, 8 * 30 + 16, 'none', INK2, 1.3, 10)
for i in range(8):
    y = 98 + i * 30
    F.box(80, y, 80, 30, '64B' if i == 0 else '', tone(i if 4 == 8 else i // 2), 11.5, 0)
    F.text(60, y + 15, str(i), 12, 'end', MUTED, mono=True, valign='middle')
for g in range(4): F.vbrace(172, 100 + g * 60, 156 + g * 60, str(g), color=ACCENT['amber'])
F.text(206, 80, '组号', 12, color=ACCENT['amber'])
F.text(50, 80, '行号', 12, 'end', MUTED)
F.text(340, 60, '内存', 13, color=INK, weight=700); F.text(270, 60, '块号', 12, color=MUTED)
blocks = list(range(11)) + [None] + [988, 989, 990, None]
y = 70
for b in blocks:
    h = 60 if b is None else 28
    F.box(300, y, 90, h, '…' if b is None else ('64B' if b in (0, 4, 8, 988) and 4 == 4 or b in (0, 8) and 4 == 8 else ''), 'white' if b is None else tone(b), 11.5, 0)
    if b is not None:
        F.text(280, y + 14, str(b), 12, 'end', MUTED, mono=True, valign='middle'); F.text(410, y + 14, f'{b} % 4 = {b % 4}', 12.5, 'start', ACCENT['red'], mono=True, valign='middle')
    y += h
F.text(345, y + 22, '直接映射：每个主存块只能放到唯一的一行' if 4 == 8 else '组间直接映射、组内全相联（2 路组相联）', 12, color=MUTED)
