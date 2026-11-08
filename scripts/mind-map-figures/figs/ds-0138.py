LABEL = '生成树：包含全部顶点的极小连通子图'
F = Fig(560, 260, '生成子图 + 极小连通子图 = 生成树')
N = {'1': (120, 80), '2': (60, 190), '3': (180, 190)}
F.graph(N, [('1','2'), ('2','3'), ('1','3')], r=20, directed=False)
F.text(120, 240, '连通图 G', 13, color=INK2)
F.line(240, 140, 300, 140, LINE, 1.6, arrow='end')
for k, drop in enumerate((('1','3'), ('2','3'), ('1','2'))):
    ox = 330 + k * 0
for k, keep in enumerate(([('1','2'), ('2','3')],)):
    M = {a: (x + 280, y) for a, (x, y) in N.items()}
    F.graph(M, keep, r=20, directed=False, tones={k2: 'blue' for k2 in M})
F.text(400, 240, '一棵生成树：3 个顶点、2 条边', 13, color=INK2)
F.text(510, 80, 'n 个顶点\nn − 1 条边', 12.5, 'end', MUTED)
