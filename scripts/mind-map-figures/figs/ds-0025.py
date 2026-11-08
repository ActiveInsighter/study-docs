from common import merge_tree
LABEL = '二路归并的最佳归并树（哈夫曼树）：WPL = 34'
F = Fig(560, 430, '2 路最佳归并树（哈夫曼树）')
merge_tree(F, 70, 86, ('16', [('10', [('5#1', [('3', ['1', '2#1']), '2#2']), '5#2']), '6']), unit=72, levelh=62, r=19)
labels = {}
F.text(280, 380, 'WPL_{min} = (1+2)×4 + 2×3 + 5×2 + 6×1 = **34**', 15, color=INK, mono=True)
F.text(280, 404, '叶结点权值 = 归并段长度（R1…R5 记录数）；每次合并最小的两段', 12.5, color=MUTED)
