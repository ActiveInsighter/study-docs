from common import btree, bt_legend
LABEL = 'B 树删除：合并（合并前）：25 所在结点不足下限，左右兄弟都不够借'
F = Fig(560, 310, '合并（合并前）：25 所在结点不足下限，左右兄弟都不够借'.split('：')[0])
kids = [(['!25'],), (['71','72'],), (['74','75','76'],)]
kids[0] = kids[0] + ([], {'hl': 'red'})
btree(F, (['70','73'], kids), 20, 104, unit=173, dy=96, stub=True)
F.text(280, 262, '合并（合并前）：25 所在结点不足下限，左右兄弟都不够借'.split('：')[1], 13.5, color=INK2)
bt_legend(F, 30, 292)
