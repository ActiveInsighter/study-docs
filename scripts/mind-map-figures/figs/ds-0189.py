from common import record
LABEL = '邻接多重表（无向图）：每条边只用一个边结点'
F = Fig(860, 360, '邻接多重表（无向图）')
N = {'V1': (60, 110), 'V2': (190, 90), 'V3': (110, 200), 'V4': (210, 200)}
F.graph(N, [('V1','V3'), ('V1','V4'), ('V2','V3'), ('V3','V4')], r=20, directed=False, size=13)
F.text(130, 262, '边：(V1,V3) (V1,V4) (V2,V3) (V3,V4)', 12, color=MUTED, mono=True)
F.text(300, 74, '顶点：data | firstedge　　边结点：ivex | ilink | jvex | jlink', 12.5, 'start', MUTED)
for i, v in enumerate(['V1', 'V2', 'V3', 'V4']):
    y = 100 + i * 56
    F.text(296, y + 13, str(i), 12, 'end', MUTED, mono=True, valign='middle')
    record(F, 304, y, [v, '●'], 46, 26, {0: 'blue'}, size=12)
E = {'e1': (480, 100, ['0', '●', '2', '●']), 'e2': (680, 100, ['0', '^', '3', '●']), 'e3': (480, 212, ['1', '^', '2', '●']), 'e4': (680, 268, ['2', '^', '3', '^'])}
C = {}
for k, (x, y, f) in E.items():
    C[k] = record(F, x, y, f, 36, 26, {0: 'amber', 2: 'amber'}, size=12)
def link(p, e, col):
    x, y = E[e][0], E[e][1]
    F.poly([p, ((p[0] + x) / 2, p[1]), ((p[0] + x) / 2, y + 13), (x - 2, y + 13)], ACCENT[col], 1.3)
link((373, 113), 'e1', 'blue'); link((373, 169), 'e3', 'blue'); link((373, 225), 'e1', 'blue'); link((373, 281), 'e2', 'blue')
F.line(C['e1'][1][0], 113, 678, 113, ACCENT['green'], 1.3, arrow='end')
F.poly([C['e1'][3], (C['e1'][3][0], 190), (500, 190), (500, 210)], ACCENT['violet'], 1.3)
F.poly([C['e3'][3], (C['e3'][3][0], 254), (700, 254), (700, 266)], ACCENT['violet'], 1.3)
F.poly([C['e2'][3], (C['e2'][3][0], 150), (770, 150), (770, 266)], ACCENT['violet'], 1.3)
F.legend(300, 340, [('blue', 'firstedge'), ('green', 'ilink：同 ivex 的下一条边'), ('violet', 'jlink：同 jvex 的下一条边')])
