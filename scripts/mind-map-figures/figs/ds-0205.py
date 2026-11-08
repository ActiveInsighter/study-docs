from common import code
LABEL = '树的先根遍历：序列 A B E K F C G D H I J'
F = Fig(860, 600, '树的先根遍历')
tones = {**{k: 'green' for k in 'BEFK'}, **{k: 'blue' for k in 'CG'}, **{k: 'amber' for k in 'DHIJ'}, 'A': 'red'}
F.tree(20, 92, ('A', [('B', [('E', ['K']), 'F']), ('C', ['G']), ('D', ['H', 'I', 'J'])]), unit=44, levelh=60, r=17, tones=tones)
F.text(250, 72, '树', 13, color=MUTED)
F.line(380, 160, 440, 160, LINE, 1.6, arrow='both'); F.text(410, 148, '左孩子右兄弟', 11.5, color=MUTED)
F.tree(450, 92, ('A', [('B', [('E', ['K', ('F', [None, ('C', ['G', ('D', [('H', [None, ('I', [None, 'J'])]), None])])])]), None]), None]), unit=36, levelh=44, r=15, size=13, tones=tones)
F.text(30, 360, '若树非空，先访问根结点，再依次先根遍历每棵子树', 13.5, 'start', INK2)
F.text(30, 392, '遍历序列：A B E K F C G D H I J', 15, 'start', INK, 700, mono=True)
F.text(30, 418, '≡ 对应二叉树的先序遍历', 13.5, 'start', ACCENT['red'], 600)

code(F, 30, 450, 'void PreOrder(TreeNode *R) {\\n  if (R != NULL) {\\n    visit(R);                 // 访问根结点\\n    while (R 还有下一个子树 T)\\n      PreOrder(T);            // 先根遍历下一棵子树\\n  }\\n}'.replace('\\n', '\n'), 11.5)
