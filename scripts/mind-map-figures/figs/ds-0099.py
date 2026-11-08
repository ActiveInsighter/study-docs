LABEL = '无向完全图与有向完全图'
F = Fig(620, 280, '完全图')
import math
for k, (cx, d, cap) in enumerate(((150, False, '无向完全图：n(n−1)/2 条边'), (460, True, '有向完全图：n(n−1) 条弧'))):
    N = {str(i): (cx + 80 * math.cos(math.pi / 2 * i - math.pi / 2), 145 + 80 * math.sin(math.pi / 2 * i - math.pi / 2)) for i in range(4)}
    E = []
    for i in range(4):
        for j in range(i + 1, 4):
            if d:
                E += [(str(i), str(j), '', {'shift': 5}), (str(j), str(i), '', {'shift': 5})]
            else:
                E.append((str(i), str(j)))
    F.graph(N, E, r=16, directed=d, labels={k: '' for k in N})
    F.text(cx, 264, cap, 13, color=INK2)
