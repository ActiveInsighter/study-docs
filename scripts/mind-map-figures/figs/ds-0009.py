LABEL = '非强连通的有向图示例'
F = Fig(460, 300)
N = {'A': (80, 80), 'B': (360, 80), 'C': (220, 220)}
F.graph(N, [('A', 'B')], r=26, tones={'B': 'blue', 'C': 'blue'})
# B <-> C as two parallel arcs
import math
(bx, by), (cx, cy) = N['B'], N['C']
L = math.hypot(cx - bx, cy - by); ux, uy = (cx - bx) / L, (cy - by) / L; nx, ny = -uy * 6, ux * 6
F.line(bx + nx, by + ny, cx + nx, cy + ny, INK2, 1.5, arrow='end', gap=27, gap2=29)
F.line(cx - nx, cy - ny, bx - nx, by - ny, INK2, 1.5, arrow='end', gap=27, gap2=29)
F.text(80, 136, '只出不进', 13, color=MUTED)
F.text(310, 172, 'B ⇄ C 互通', 13, 'start', ACCENT['blue'])
F.text(230, 284, 'A 不能从 B、C 到达 → 不是强连通图', 13, color=INK2)
