from graphs_common import adj_matrix
from common import code
LABEL = '并查集的应用：判断图是否有环'
F = Fig(860, 420, '并查集的应用：判断图是否有环')
N = {'a': (60, 80), 'c': (180, 80), 'b': (60, 180), 'd': (130, 180), 'e': (230, 180)}
F.graph(N, [('a','c','1'), ('a','b','3',{'side':-1}), ('b','c','4',{'side':-1}), ('d','e','2')], r=15, directed=False, size=13)
F.text(30, 236, '用邻接矩阵表示无向图的边：', 12.5, 'start', MUTED)
adj_matrix(F, 40, 248, list('abcde'), [['0','3','1','0','0'],['3','0','4','0','0'],['1','4','0','0','0'],['0','0','0','0','2'],['0','0','0','2','0']], cw=30, ch=26)
code(F, 300, 80, '// 用并查集判断无向图是否有环（邻接矩阵）\nint hasAcyclic(int g[5][5]) {\n  int S[5];                       // 定义、初始化并查集\n  for (int i = 0; i < 5; i++) S[i] = -1;\n  for (int i = 0; i < 5; i++)     // 遍历各条边（上三角）\n    for (int j = i + 1; j < 5; j++)\n      if (g[i][j] > 0) {\n        int iRoot = Find(S, i);\n        int jRoot = Find(S, j);\n        if (iRoot != jRoot)\n          Union(S, iRoot, jRoot);\n        else                      // 两端已在同一集合\n          return 1;               // 再加这条边必成环\n      }\n  return 0;                       // 图中没有环\n}', 12)
