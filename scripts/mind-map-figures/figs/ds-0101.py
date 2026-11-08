from common import rb
LABEL = '红黑树查找：与 BST 相同，左小右大，查到 NIL 即失败'
F = Fig(800, 370, '红黑树的查找')
t = (13, 'B', (8, 'R', (1, 'B', None, (6, 'R', None, None)), (11, 'B', None, None)), (17, 'R', (15, 'B', None, None), (25, 'B', (22, 'R', None, None), (27, 'R', None, None))))
rb(F, 10, 80, t, unit=56, levelh=60)
F.text(400, 356, '从根出发，左小右大；走到 NIL（空叶结点）则查找失败', 12.5, color=MUTED)
