from common import merge_tree
LABEL = '补充长度为 0 的虚段后构造严格 3 叉最佳归并树'
F = Fig(560, 380, '补 1 个虚段（长度 0）')
pos = merge_tree(F, None, 90, ('91', [('20', [('5', ['2', '3', '0']), '6', '9']), '24', ('47', ['12', '17', '18'])]), unit=52, levelh=72)
x, y = pos['0']
F.circle(x, y, 20, '0', 'white', 14, dash='4 3')
F.text(x + 26, y + 5, '虚段', 12, 'start', MUTED)
F.text(280, 356, 'WPL_{min} = (2+3+0)×3 + (6+9+12+17+18)×2 + 24×1 = 163', 13.5, color=INK2, mono=True)
