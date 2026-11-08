from common import loser_tree
LABEL = '败者树初始情况：8 个归并段的首元素作为叶子'
F = Fig(800, 476, '败者树 · 初始情况（8 路归并）')
loser_tree(F, 20, 72)
F.text(400, 458, '叶结点 = 各归并段当前的首元素；黑色结点用来存放每场比较的“败者”', 12.5, color=MUTED)
