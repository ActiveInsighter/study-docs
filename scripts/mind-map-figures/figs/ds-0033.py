LABEL = '非连通图：连通分量与生成森林'
F = Fig(860, 360, '非连通图：连通分量 vs 生成森林')
import math
def K4(ox, oy, s=1, edges='all', t='white'):
    N = {'a': (ox, oy - 38 * s), 'b': (ox - 38 * s, oy), 'c': (ox + 38 * s, oy), 'd': (ox, oy + 38 * s)}
    allE = [('a','b'),('a','c'),('b','d'),('c','d'),('a','d'),('b','c')]
    F.graph(N, allE if edges == 'all' else edges, r=11, directed=False, labels={k: '' for k in N}, tones={k: t for k in N})
    return N
K4(80, 180); F.circle(160, 180, 11); F.text(110, 250, '原图（K₄ + 孤立点）', 12.5, color=INK2)
F.line(190, 150, 250, 110, ACCENT['green'], 2, arrow='end'); F.line(190, 210, 250, 250, ACCENT['red'], 2, arrow='end')
F.rect(270, 50, 250, 130, 'none', ACCENT['green'], 1.3, 12, dash='6 4')
K4(350, 118, t='green'); F.circle(460, 118, 11, '', 'green')
F.text(395, 72, '连通分量：唯一（2 个）', 12.5, color=ACCENT['green'], weight=600)
for k, es in enumerate(([('a','b'),('b','d'),('a','c')], [('a','b'),('a','c'),('a','d')], [('a','d'),('b','c'),('c','d')])):
    x = 300 + k * 190
    F.rect(x - 30, 200, 170, 130, 'none', ACCENT['red'], 1.3, 12, dash='6 4')
    K4(x + 40, 268, 0.9, es, 'red'); F.circle(x + 115, 268, 11, '', 'red')
F.text(585, 72, '生成森林：不唯一', 12.5, 'start', ACCENT['red'], weight=600)
F.text(585, 96, '每个连通分量各取一棵生成树', 12, 'start', MUTED)
F.text(585, 120, '（下方仅列出其中 3 种）', 12, 'start', MUTED)
