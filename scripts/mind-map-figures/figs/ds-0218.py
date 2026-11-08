LABEL = '无向图 G 及其三个连通分量'
F = Fig(860, 340, '连通分量 = 极大连通子图')
def G(ox, oy, parts, tones=None):
    P = {'A': (0, 0), 'B': (220, 0), 'C': (0, 150), 'D': (110, 110), 'E': (220, 150), 'I': (70, 36), 'J': (150, 36), 'F': (110, 190), 'G': (50, 260), 'H': (170, 260)}
    E = [('A','B'), ('A','C'), ('B','E'), ('C','D'), ('D','E'), ('I','J'), ('F','G'), ('F','H'), ('G','H')]
    for part, (dx, dy), t in parts:
        N = {k: (ox + P[k][0] * 0.8 + dx, oy + P[k][1] * 0.8 + dy) for k in part}
        F.graph(N, [e for e in E if e[0] in part and e[1] in part], r=14, directed=False, size=12, tones={k: t for k in N})
G(40, 70, [('ABCDEIJFGH', (0, 0), 'white')])
F.text(130, 330, '(a) 无向图 G', 13, color=INK2)
G(320, 70, [('ABCDE', (0, 0), 'blue'), ('FGH', (190, -88), 'green'), ('IJ', (330, 60), 'amber')])
F.text(600, 330, '(b) G 的三个连通分量', 13, color=INK2)
F.line(270, 150, 300, 150, LINE, 1.6, arrow='end')
