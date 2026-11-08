from graphs_common import mst_panel
LABEL = 'Kruskal 算法：每次选权值最小且不成环的边'
F = Fig(780, 470, 'Kruskal 算法：按边权从小到大，不成环就加入')
order = [('V1', 'V3'), ('V4', 'V6'), ('V2', 'V5'), ('V3', 'V6'), ('V2', 'V3')]
w = ['1', '2', '3', '4', '5']
mst_panel(F, 10, 70, {}, '(a) 原图', full=True)
for k in range(5):
    e = {o: ('new' if i == k else 'old') for i, o in enumerate(order[:k + 1])}
    x, y = [(270, 70), (530, 70), (10, 270), (270, 270), (530, 270)][k]
    mst_panel(F, x, y, e, '(' + 'bcdef'[k] + ') 边权 ' + w[k] + '：' + '–'.join(order[k]))
