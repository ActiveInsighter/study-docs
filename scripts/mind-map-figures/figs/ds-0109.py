from common import rb
LABEL = '结点的黑高 bh：从该结点到任一 NIL 的路径上黑结点个数（不含自身）'
F = Fig(720, 400, '黑高 bh')
t = (6, 'B', (2, 'B', None, None), (15, 'R', (11, 'B', (8, 'R', None, None), (14, 'R', None, None)), (18, 'B', None, (20, 'R', None, None))))
pos = rb(F, 20, 80, t, unit=60, levelh=66, r=18)
bh = {'6': 2, '2': 1, '15': 2, '11': 1, '18': 1, '8': 1, '14': 1, '20': 1}
for k, v in bh.items():
    x, y = pos[k]
    F.text(x + 24, y - 14, f'bh={v}', 12, 'start', ACCENT['blue'], 600, mono=True, halo=True)
F.text(360, 386, 'NIL 结点的 bh = 0；根的黑高即整棵树的黑高（此处 bh = 2）', 12.5, color=MUTED)
