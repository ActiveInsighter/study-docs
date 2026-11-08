LABEL = '有向图示例：A ⇄ B，B → C'
F = Fig(460, 300)
import math
N = {'A': (80, 80), 'B': (360, 80), 'C': (220, 230)}
for (a, b) in (('A', 'B'), ('B', 'A')):
    (x1, y1), (x2, y2) = N[a], N[b]
    s = 6 if a == 'A' else -6
    F.line(x1, y1 + s, x2, y2 + s, INK2, 1.5, arrow='end', gap=27, gap2=29)
F.line(*N['B'], *N['C'], INK2, 1.5, arrow='end', gap=27, gap2=29)
for k, (x, y) in N.items():
    F.circle(x, y, 26, k, 'white', 16)
F.text(230, 284, 'A ⇄ B 互通；B → C', 13, color=INK2)
