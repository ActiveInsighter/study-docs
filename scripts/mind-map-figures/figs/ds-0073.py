from common import btree, bt_legend
LABEL = 'B 树删除：借右（借前）：25 所在结点删后只剩 1 个，右兄弟够借'
F = Fig(560, 310, '借右（借前）：25 所在结点删后只剩 1 个，右兄弟够借'.split('：')[0])
kids = [(['!25'],), (['70','71','72'],), (['74','75','76'],)]
kids[0] = kids[0] + ([], {'hl': 'red'})
btree(F, (['49','73'], kids), 20, 104, unit=173, dy=96, stub=True)
F.text(280, 262, '借右（借前）：25 所在结点删后只剩 1 个，右兄弟够借'.split('：')[1], 13.5, color=INK2)
bt_legend(F, 30, 292)
