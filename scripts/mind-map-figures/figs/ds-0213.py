from common import btree, bt_legend, bnode2
LABEL = 'B 树删除：父结点不足下限时继续向上合并，树高可能减一'
F = Fig(760, 300, '继续合并：父结点不足下限 → 与兄弟、根合并，树高减一')
btree(F, (['82'], [(['73'], [], {'hl': 'red'}), (['87', '93'],)]), 20, 90, unit=190, dy=100)
F.line(410, 140, 470, 140, LINE, 1.6, arrow='end')
bnode2(F, 610, 126, ['73', '!82', '87', '93'], minline=2)
F.text(610, 190, '新根（原根 82 下移合并）', 13, color=INK2)
F.text(380, 250, '合并可能逐层向上传递；当根结点的关键字被合并下去后，树的高度减 1', 13.5, color=INK2)
bt_legend(F, 40, 284)
