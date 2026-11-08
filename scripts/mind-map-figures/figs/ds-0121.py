LABEL = '并查集用双亲表示法存储：用一个数组 S[] 表示集合关系'
F = Fig(760, 330, '双亲表示法：一个数组 S[] 即可表示“集合”')
def up(nodes, par, t):
    for c, p in par.items():
        F.line(*nodes[c], *nodes[p], ACCENT[t], 1.4, arrow='end', gap=16, gap2=18)
    for k, (x, y) in nodes.items():
        F.circle(x, y, 16, k, t, 13)
N1 = {'A': (150, 76), 'B': (150, 124), 'E': (110, 170), 'F': (190, 170), 'K': (80, 216), 'L': (140, 216)}
up(N1, {'B': 'A', 'E': 'B', 'F': 'B', 'K': 'E', 'L': 'E'}, 'green')
N2 = {'C': (300, 96), 'G': (300, 170)}
up(N2, {'G': 'C'}, 'violet')
N3 = {'D': (470, 80), 'H': (420, 136), 'I': (470, 136), 'J': (520, 136), 'M': (420, 196)}
up(N3, {'H': 'D', 'I': 'D', 'J': 'D', 'M': 'H'}, 'amber')
els = list('ABCDEFGHIJKLM'); S = ['-1', '0', '-1', '-1', '1', '1', '2', '3', '3', '3', '4', '4', '7']
tone = {**{k: 'green' for k in 'ABEFKL'}, **{k: 'violet' for k in 'CG'}, **{k: 'amber' for k in 'DHIJM'}}
F.text(84, 266, '元素', 12.5, 'end', INK2, valign='middle')
F.cells(96, 254, els, 44, 24, {i: tone[e] for i, e in enumerate(els)}, size=12, mono=False)
F.text(84, 292, 'S[]', 12.5, 'end', INK2, valign='middle', mono=True)
F.cells(96, 280, S, 44, 26, size=12, index=0)
F.text(620, 120, 'S[i] = 双亲下标\n根结点 S[i] = −1', 13, 'start', INK2, lh=1.6)
