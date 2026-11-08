LABEL = '对称矩阵与三角矩阵的压缩存储'
F = Fig(700, 330, '对称矩阵 / 三角矩阵的压缩存储')
def mat(x, y, M, tones):
    for r, row in enumerate(M):
        for c, v in enumerate(row):
            F.text(x + c * 40, y + r * 36, v, 15, color=TONES[tones(r, c)][2] if tones(r, c) else INK2, mono=True, weight=600 if tones(r, c) else 400, valign='middle')
    F.path(f'M{x - 18} {y - 18} q-8 0 -8 8 V{y + 82} q0 8 8 8', INK2, 1.4); F.path(f'M{x + 98} {y - 18} q8 0 8 8 V{y + 82} q0 8 -8 8', INK2, 1.4)
mat(70, 90, [['1', '2', '3'], ['2', '4', '5'], ['3', '5', '6']], lambda r, c: 'blue' if c >= r else None)
F.line(200, 126, 240, 126, LINE, 1.5, arrow='end')
F.cells(250, 110, list('123456'), 40, 32, {i: 'blue' for i in range(6)}, size=14)
F.text(500, 132, '对称矩阵：只存上（或下）三角', 12.5, 'start', INK2)
mat(70, 216, [['1', '2', '3'], ['c', '4', '5'], ['c', 'c', '6']], lambda r, c: 'blue' if c >= r else 'amber')
F.line(200, 252, 240, 252, LINE, 1.5, arrow='end')
F.cells(250, 236, list('123456') + ['c'], 40, 32, {**{i: 'blue' for i in range(6)}, 6: 'amber'}, size=14)
F.text(540, 258, '三角矩阵：最后多存\n一个常量 c', 12.5, 'start', INK2, lh=1.4)
