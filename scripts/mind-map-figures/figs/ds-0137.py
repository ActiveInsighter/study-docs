from graphs_common import mst_panel
LABEL = 'Prim 算法：从一个顶点出发，每次加入与当前集合相连的最小边'
F = Fig(780, 470, 'Prim 算法：只有一个集合，不断扩大')
order = [('V1', 'V3'), ('V3', 'V6'), ('V4', 'V6'), ('V2', 'V3'), ('V2', 'V5')]
mst_panel(F, 10, 70, {}, '(a) 原图', full=True)
for k in range(5):
    e = {o: ('new' if i == k else 'old') for i, o in enumerate(order[:k + 1])}
    x, y = [(270, 70), (530, 70), (10, 270), (270, 270), (530, 270)][k]
    mst_panel(F, x, y, e, '(' + 'bcdef'[k] + ') 加入 ' + '–'.join(order[k]))
