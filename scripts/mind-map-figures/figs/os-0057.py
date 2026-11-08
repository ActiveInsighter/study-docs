LABEL = '位示图法：每一位对应一个盘块，0 空闲 1 已分配'
F = Fig(700, 270, '位示图法')
bits = ['1100011110011100', '0011111000011101', '1110000111110001']
F.text(60, 70, '位号', 12, 'start', ACCENT['red'], 600); F.text(30, 94, '字号', 12, 'start', ACCENT['red'], 600)
for j in range(16): F.text(96 + j * 36, 92, str(j + 1), 11, color=INK2, mono=True)
for i, row in enumerate(bits + ['', '…', '']):
    y = 100 + i * 22
    F.text(70, y + 11, ['1', '2', '3', '4', '…', '16'][i], 11, 'end', INK2, mono=True, valign='middle')
    for j in range(16):
        v = row[j] if j < len(row) else ''
        F.box(78 + j * 36, y, 36, 22, v, 'blue' if v == '1' else 'white', 11, 0, True)
F.text(500, 60, '考点：字号、位号 ⇄ 盘块号的互推', 12, 'middle', ACCENT['blue'], 600)
