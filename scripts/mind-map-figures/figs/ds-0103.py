from common import subtree, avl_node, edge
LABEL = 'RR 平衡旋转（左单旋）'
F = Fig(760, 330, 'RR 型：左单旋')
A, B = (150, 80), (220, 140)
avl_node(F, *A, 'A', '−2', 'amber'); avl_node(F, *B, 'B', '−1')
edge(F, A, B, 16, 16); edge(F, A, (100, 186)); edge(F, B, (180, 186)); edge(F, B, (260, 186))
subtree(F, 100, 186, 'AL', 'H'); subtree(F, 180, 186, 'BL', 'H'); subtree(F, 260, 186, 'BR', 'H+1', hot=True)
F.line(330, 150, 420, 150, LINE, 1.6, arrow='end'); F.text(375, 136, '左旋', 13, color=INK2, weight=600)
A2, B2 = (530, 140), (600, 80)
avl_node(F, *B2, 'B', '0'); avl_node(F, *A2, 'A', '0', 'amber')
edge(F, B2, A2, 16, 16); edge(F, B2, (650, 186)); edge(F, A2, (490, 186)); edge(F, A2, (570, 186))
subtree(F, 490, 186, 'AL', 'H'); subtree(F, 570, 186, 'BL', 'H'); subtree(F, 650, 186, 'BR', 'H+1', hot=True)
F.text(380, 270, '在 A 的右孩子 B 的右子树上插入：B 向左上旋转代替 A 成为根，A 左下旋成为 B 的左孩子', 13, color=INK2)
F.text(380, 296, 'B 原来的左子树 BL 作为 A 的右子树　　中序不变：AL < A < BL < B < BR', 13, color=MUTED)
