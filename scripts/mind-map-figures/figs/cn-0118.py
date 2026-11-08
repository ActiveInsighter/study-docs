LABEL = '数据报方式：各分组独立选路，可能乱序到达，逐跳确认'
F = Fig(700, 300, '数据报方式')
N = {'A': (180, 150), 'C': (260, 80), 'E': (440, 80), 'D': (350, 150), 'F': (260, 220), 'G': (440, 220), 'B': (540, 150)}
for a, b in (('A', 'C'), ('A', 'D'), ('A', 'F'), ('C', 'E'), ('C', 'D'), ('D', 'E'), ('D', 'G'), ('F', 'D'), ('F', 'G'), ('E', 'B'), ('D', 'B'), ('G', 'B')): F.line(*N[a], *N[b], INK2, 1.1)
for k, (x, y) in N.items(): F.box(x - 24, y - 16, 48, 32, f'结点 {k}', 'blue', 10.5, 4)
F.box(30, 132, 50, 36, '主机 A', 'violet', 10.5, 4); F.box(620, 132, 50, 36, '主机 B', 'violet', 10.5, 4)
F.cells(84, 140, ['P2', 'P1'], 22, 20, size=9.5); F.cells(570, 140, ['P1', 'P2'], 22, 20, size=9.5)
F.line(132, 150, 154, 150, INK2, 1.1, arrow='end'); F.line(566, 150, 600, 150, INK2, 1.1, arrow='end')
for (x, y, t, c) in ((220, 106, 'P2', 'amber'), (300, 150, 'P2', 'amber'), (410, 116, 'P1', 'amber'), (310, 70, 'P1', 'amber'), (400, 190, 'P2', 'amber')): F.pill(x, y, t, c, 9.5)
F.text(240, 54, 'ACK', 10, color=MUTED); F.text(500, 100, 'ACK', 10, color=MUTED); F.text(500, 230, 'ACK', 10, color=MUTED)
F.text(350, 284, 'P1 走 A→C→E→B，P2 走 A→D→G→B：各自独立选路；每跳收到后返回 ACK', 11, color=MUTED)
