from common import merge_tree
LABEL = '需要补充的虚段个数：k = 4，n₀ = 9 时补 1 个'
F = Fig(780, 380, '例：4 路归并，9 个初始归并段')
pos = merge_tree(F, 40, 96, ('45', [('21', [('6', ['0', '1', '2', '3']), '4', '5', '6#1']), '7', '8', '9']), unit=40, levelh=72, r=17)
x, y = pos['0']; F.circle(x, y, 17, '0', 'white', 14, dash='4 3')
F.text(470, 96, 'u = (n_{0} − 1) % (k − 1)', 14, 'start', INK2, mono=True)
F.text(470, 122, '  = (9 − 1) % 3 = 2 ≠ 0', 14, 'start', INK2, mono=True)
F.text(470, 160, '补 (k − 1) − u = 3 − 2 = **1** 个虚段', 14, 'start', INK, mono=True)
F.text(470, 206, '✗ 不是 (9 + 3) % 4，补 3 个', 13, 'start', ACCENT['red'])
F.text(470, 232, 'u = 0 时无需补充', 13, 'start', MUTED)
F.text(390, 362, '权值 1…9 的 9 个归并段 + 1 个虚段 → 严格 4 叉树', 12.5, color=MUTED)
