LABEL = '孩子表示法：顺序存储结点，链式存储每个结点的孩子'
F = Fig(700, 450, '孩子表示法（顺序 + 链式）')
rows = [['下标', 'data', 'firstChild']] + [[str(i), d, ''] for i, d in enumerate('RABCDEFGHK')]
F.table(30, 64, rows, [56, 60, 90], 34, mono_cols=(0,), size=14)
kids = {0: [1, 2, 3], 1: [4, 5], 3: [6], 6: [7, 8, 9]}
for i in range(10):
    y = 64 + 34 * (i + 1) + 17
    if i in kids:
        F.circle(30 + 116 + 45, y, 3, '', 'dark', sw=0)
        x = 260
        F.line(191, y, x - 2, y, INK2, 1.3, arrow='end')
        for j, c in enumerate(kids[i]):
            F.rect(x, y - 13, 32, 26, 'blue', ACCENT['blue'], 1.3, 0)
            F.text(x + 16, y, str(c), 13, color=TONES['blue'][2], mono=True, valign='middle')
            F.rect(x + 32, y - 13, 14, 26, '#f4f4f5', ACCENT['blue'], 1.3, 0)
            if j < len(kids[i]) - 1:
                F.circle(x + 39, y, 2.6, '', 'dark', sw=0)
                F.line(x + 39, y, x + 72, y, INK2, 1.3, arrow='end')
            else:
                F.text(x + 39, y, '∧', 11, color=LINE, valign='middle')
            x += 74
    else:
        F.text(191, y, '∧', 12, color=LINE, valign='middle')
F.text(560, 110, '对应的树', 13, color=MUTED)
F.tree(470, 150, ('R', [('A', ['D', 'E']), 'B', ('C', [('F', ['G', 'H', 'K'])])]), unit=30, levelh=56, r=13, size=12)
F.text(560, 390, '孩子链表中存的是孩子的下标', 12.5, color=MUTED)
