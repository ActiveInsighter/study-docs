from common import subtree, avl_node, edge
LABEL = 'RL 平衡旋转（先右后左双旋）'
F = Fig(760, 380, 'RL 型：先右旋 C，再左旋 C')
A, B, C = (120, 76), (210, 130), (160, 186)
avl_node(F, *A, 'A', '−2', 'amber'); avl_node(F, *B, 'B', '1'); avl_node(F, *C, 'C', '1', 'red')
edge(F, A, B, 16, 16); edge(F, B, C, 16, 16); edge(F, A, (70, 130)); edge(F, B, (260, 186)); edge(F, C, (130, 232)); edge(F, C, (190, 232))
subtree(F, 70, 130, 'AL', 'H'); subtree(F, 260, 186, 'BR', 'H'); subtree(F, 130, 232, 'CL', 'H', hot=True); subtree(F, 190, 232, 'CR', 'H−1')
F.line(330, 170, 420, 170, LINE, 1.6, arrow='end'); F.text(375, 156, '两次旋转', 13, color=INK2, weight=600)
C2, A2, B2 = (590, 90), (510, 150), (670, 150)
avl_node(F, *C2, 'C', '0', 'red'); avl_node(F, *A2, 'A', '0', 'amber'); avl_node(F, *B2, 'B', '−1')
edge(F, C2, A2, 16, 16); edge(F, C2, B2, 16, 16)
for (p, x, lab, h, hot) in ((A2, 480, 'AL', 'H', 0), (A2, 540, 'CL', 'H', 1), (B2, 640, 'CR', 'H−1', 0), (B2, 700, 'BR', 'H', 0)):
    edge(F, p, (x, 196)); subtree(F, x, 196, lab, h, hot=bool(hot))
F.text(380, 318, '在 A 的右孩子 B 的左子树上插入：C 先右旋到 B 的位置，再左旋到 A 的位置', 13, color=INK2)
F.text(380, 344, '中序不变：AL < A < CL < C < CR < B < BR', 13, color=MUTED)
