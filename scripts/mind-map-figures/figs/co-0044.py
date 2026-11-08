LABEL = '存储体：一排存储元组成一个存储字，CPU 以存储字为单位读写'
F = Fig(760, 250, '存储体：一行 = 一个存储字')
F.cells(100, 70, list('10100011'), 70, 30, {i: 'green' for i in range(8)}, size=14)
F.text(670, 85, '存储字', 12.5, 'start', ACCENT['green'], 600, valign='middle')
for r, bits in enumerate(('10100011', '00000000')):
    y = 120 + r * 56
    F.rect(90, y - 6, 580, 46, 'none', '#a1a1aa', 1.1, 8, dash='4 3' if r else None)
    for i, b in enumerate(bits):
        x = 135 + i * 70
        F.line(x - 15, y + 4, x - 15, y + 30, INK2, 1.2); F.line(x - 24, y + 30, x - 6, y + 30, INK2, 2); F.line(x - 24, y + 36, x - 6, y + 36, INK2, 2)
        if r == 0: F.text(x + 8, y + 20, b, 12, color=INK2, mono=True, valign='middle')
    F.line(70, y + 4, 668, y + 4, ACCENT['red'], 1.3)
F.text(60, 124, '选通线', 11, 'end', ACCENT['red'])
F.text(690, 150, '存储单元', 11.5, 'start', MUTED)
F.text(380, 236, '存储字长 8 bit：1 Byte = 8 bit；CPU 以一个存储字长 / 机器字长为单位进行读写', 12, color=MUTED)
