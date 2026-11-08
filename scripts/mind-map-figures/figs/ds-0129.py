from common import rb
LABEL = '红黑树判断题：下列哪棵满足红黑树定义（答案 D）'
F = Fig(860, 560, '下列选项中，满足红黑树定义的是？')
A = (10, 'B', (5, 'B', None, None), (30, 'B', (20, 'R', None, None), (40, 'R', (37, 'R', None, None), None)))
B = (10, 'R', (5, 'B', None, None), (20, 'B', None, (30, 'R', None, None)))
C = (13, 'B', (8, 'R', (1, 'B', None, (6, 'B', None, None)), (11, 'B', None, None)), (17, 'R', (15, 'B', None, None), (25, 'B', (22, 'R', None, None), (27, 'R', None, None))))
D = (13, 'B', (8, 'R', (1, 'B', None, (6, 'R', None, None)), (11, 'B', None, None)), (17, 'R', (15, 'B', None, None), (25, 'B', (22, 'R', None, None), (27, 'R', None, None))))
for (tag, t, x, y, u, note, ok) in (('A', A, 20, 96, 34, '✗ 37 与 40 红红相连', False), ('B', B, 470, 96, 40, '✗ 根结点是红色', False),
                                   ('C', C, 10, 350, 29, '✗ 经过 6 的路径多一个黑结点', False), ('D', D, 440, 350, 29, '✓ 满足全部性质', True)):
    F.text(x + 14, y - 30, tag, 16, 'start', INK, 700)
    rb(F, x, y, t, unit=u, levelh=44, r=12, size=10)
    F.text(x + 14 + 22, y - 30, note, 12.5, 'start', ACCENT['green'] if ok else ACCENT['red'], 600)
