from common import btree, bt_legend
LABEL = 'B 树删除：与兄弟及父结点中的分隔关键字合并'
F = Fig(560, 310, '合并后')
btree(F, (['73'], [(['25', '!70', '71', '72'],), (['74', '75', '76'],)], {'hl': 'red'}), 20, 104, unit=260, dy=96, stub=True)
F.text(280, 262, '父结点 70 下移与 25、71 72 合并；父结点只剩 1 个关键字，也低于下限', 13, color=INK2)
bt_legend(F, 30, 292)
