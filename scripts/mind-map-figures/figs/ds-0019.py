from common import merge_tree
LABEL = '三路平衡归并的归并树：WPL = 242，I/O 次数 484'
F = Fig(620, 345, '3 路归并树（9 个初始归并段）')
merge_tree(F, 58, 92, ('121', [('51', ['9', '30', '12']), ('38', ['18', '3#1', '17']), ('32', ['2', '6', '24'])]), unit=56, levelh=80)
F.text(310, 302, 'WPL = (9+30+12+18+3+17+2+6+24) × 2 = 242', 14, color=INK2, mono=True)
F.text(310, 326, '归并过程中磁盘 I/O 总次数 = 2 × WPL = 484', 13, color=MUTED)
