from common import record, code
LABEL = '二叉树的链式存储（二叉链表）'
F = Fig(760, 400, '二叉链表')
F.tree(20, 90, ('1', [('2', [None, ('4', ['6', None])]), ('3', [None, '5'])]), unit=40, levelh=54, r=16)
P = {'1': (470, 76), '2': (380, 136), '3': (560, 136), '4': (430, 196), '5': (620, 196), '6': (380, 256)}
ch = {'1': ('2', '3'), '2': (None, '4'), '3': (None, '5'), '4': ('6', None), '5': (None, None), '6': (None, None)}
cs = {}
for k, (x, y) in P.items():
    l, r = ch[k]
    cs[k] = record(F, x - 45, y, ['●' if l else '^', k, '●' if r else '^'], 30, 26, {1: 'blue'})
for k, (l, r) in ch.items():
    for j, c in ((0, l), (2, r)):
        if c:
            F.line(cs[k][j][0], cs[k][j][1], P[c][0], P[c][1], INK2, 1.3, arrow='end')
code(F, 30, 312, 'typedef struct BiTNode {\n  ElemType data;                     // 数据域\n  struct BiTNode *lchild, *rchild;   // 左、右孩子指针\n} BiTNode, *BiTree;', 12)
