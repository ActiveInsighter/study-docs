from common import btree, bt_legend
LABEL = 'B 树删除：借右（借后）：父结点 49 下移，右兄弟最小值 70 上移'
F = Fig(560, 310, '借右（借后）：父结点 49 下移，右兄弟最小值 70 上移'.split('：')[0])
kids = [(['25','!49'],), (['71','72'],), (['74','75','76'],)]
kids[0] = kids[0] + ([], {'hl': 'red'})
btree(F, (['70','73'], kids), 20, 104, unit=173, dy=96, stub=True)
F.text(280, 262, '借右（借后）：父结点 49 下移，右兄弟最小值 70 上移'.split('：')[1], 13.5, color=INK2)
bt_legend(F, 30, 292)
