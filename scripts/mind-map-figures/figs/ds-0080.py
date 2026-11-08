LABEL = '双亲表示法：每个结点记录双亲在数组中的下标'
F = Fig(640, 420, '双亲表示法')
rows = [['下标', 'data', 'parent']] + [[str(i), d, p] for i, (d, p) in enumerate(zip('RABCDEFGHK', ['-1', '0', '0', '0', '1', '1', '3', '6', '6', '6']))]
F.table(30, 64, rows, [56, 70, 76], 32, mono_cols=(0, 2), size=14, tones={(1, 2): 'red'})
P = {'R': (440, 110), 'A': (350, 190), 'B': (440, 190), 'C': (530, 190), 'D': (310, 270), 'E': (390, 270), 'F': (530, 270), 'G': (470, 350), 'H': (530, 350), 'K': (590, 350)}
par = {'A': 'R', 'B': 'R', 'C': 'R', 'D': 'A', 'E': 'A', 'F': 'C', 'G': 'F', 'H': 'F', 'K': 'F'}
for c, p in par.items():
    F.line(*P[c], *P[p], ACCENT['blue'], 1.4, arrow='end', gap=17, gap2=19)
for k, (x, y) in P.items():
    F.box(x - 17, y - 17, 34, 34, k, 'blue' if k == 'R' else 'white', 15, 6)
F.text(450, 404, '指针由孩子指向双亲；根的 parent = −1', 12.5, color=MUTED)
