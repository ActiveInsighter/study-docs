from common import subtree, avl_node, edge
LABEL = 'LR 平衡旋转（先左后右双旋）'
F = Fig(760, 380, 'LR 型：先左旋 C，再右旋 C')
A, B, C = (220, 76), (130, 130), (180, 186)
avl_node(F, *A, 'A', '2', 'amber'); avl_node(F, *B, 'B', '−1'); avl_node(F, *C, 'C', '1', 'red')
edge(F, A, B, 16, 16); edge(F, B, C, 16, 16); edge(F, A, (270, 130)); edge(F, B, (80, 186)); edge(F, C, (150, 232)); edge(F, C, (210, 232))
subtree(F, 270, 130, 'AR', 'H'); subtree(F, 80, 186, 'BL', 'H'); subtree(F, 150, 232, 'CL', 'H', hot=True); subtree(F, 210, 232, 'CR', 'H−1')
F.line(330, 170, 420, 170, LINE, 1.6, arrow='end'); F.text(375, 156, '两次旋转', 13, color=INK2, weight=600)
C2, B2, A2 = (590, 90), (510, 150), (670, 150)
avl_node(F, *C2, 'C', '0', 'red'); avl_node(F, *B2, 'B', '0'); avl_node(F, *A2, 'A', '−1', 'amber')
edge(F, C2, B2, 16, 16); edge(F, C2, A2, 16, 16)
for (p, x, lab, h, hot) in ((B2, 480, 'BL', 'H', 0), (B2, 540, 'CL', 'H', 1), (A2, 640, 'CR', 'H−1', 0), (A2, 700, 'AR', 'H', 0)):
    edge(F, p, (x, 196)); subtree(F, x, 196, lab, h, hot=bool(hot))
F.text(380, 318, '在 A 的左孩子 B 的右子树上插入：C 先左旋到 B 的位置，再右旋到 A 的位置', 13, color=INK2)
F.text(380, 344, '中序不变：BL < B < CL < C < CR < A < AR（新结点也可能插入 CR）', 13, color=MUTED)
