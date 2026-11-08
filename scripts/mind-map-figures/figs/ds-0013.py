from common import btree, bt_legend
LABEL = 'B 树删除：借左（借前）：92 所在结点删后只剩 1 个，左兄弟够借'
F = Fig(560, 310, '借左（借前）：92 所在结点删后只剩 1 个，左兄弟够借'.split('：')[0])
kids = [(['83','86','87'],), (['!92'],), (['94','99'],)]
kids[1] = kids[1] + ([], {'hl': 'red'})
btree(F, (['88','93'], kids), 20, 104, unit=173, dy=96, stub=True)
F.text(280, 262, '借左（借前）：92 所在结点删后只剩 1 个，左兄弟够借'.split('：')[1], 13.5, color=INK2)
bt_legend(F, 30, 292)
