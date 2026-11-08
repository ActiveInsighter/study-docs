LABEL = '森林的中序（后根）遍历等同于对应二叉树的中序遍历'
F = Fig(860, 460, '森林的中序遍历 ≡ 对应二叉树的中序遍历')
tree = ('B', [('E', [('K', [None, 'L']), 'F']), ('C', ['G', ('D', [('H', ['M', ('I', [None, 'J'])]), None])])])
tones = {k: 'green' for k in 'BEKLF'}
tones.update({k: 'blue' for k in 'CG'})
tones.update({k: 'amber' for k in 'DHMIJ'})
F.tree(20, 90, tree, unit=44, levelh=62, r=19, tones=tones)
x = 470
F.text(x, 100, '规则（森林非空时）', 15, 'start', INK, 700)
F.text(x, 130, '① 中序遍历第一棵树根结点的子树森林\n② 访问第一棵树的根结点\n③ 中序遍历其余树构成的森林', 14, 'start', INK2, lh=1.6)
F.text(x, 250, '按三棵树分组：', 14, 'start', INK2)
F.cells(x, 266, ['K','L','E','F','B'], 30, 32, {i: 'green' for i in range(5)}, size=14)
F.cells(x + 158, 266, ['G','C'], 30, 32, {0: 'blue', 1: 'blue'}, size=14)
F.cells(x + 226, 266, ['M','H','I','J','D'], 30, 32, {i: 'amber' for i in range(5)}, size=14)
F.text(x, 340, '结果：K L E F B G C M H I J D', 15, 'start', INK, 600, mono=True)
F.legend(x, 380, [('green', '树 1'), ('blue', '树 2'), ('amber', '树 3')])
F.text(x, 420, '左孩子 = 第一个孩子，右孩子 = 右兄弟', 13, 'start', MUTED)
