from common import code
LABEL = '并查集优化：Find 时压缩路径，把查找路径上的结点都挂到根下'
F = Fig(860, 440, '压缩路径：Find(L) 后路径上的结点直接挂到根')
def up(nodes, par, tones):
    for c, p in par.items():
        F.line(*nodes[c], *nodes[p], INK2, 1.3, arrow='end', gap=15, gap2=17)
    for k, (x, y) in nodes.items():
        F.circle(x, y, 15, k, tones.get(k, 'white'), 13)
t = {'A': 'red', 'B': 'blue', 'E': 'blue', 'L': 'blue'}
up({'A': (100, 76), 'B': (100, 122), 'E': (70, 168), 'F': (130, 168), 'K': (40, 214), 'L': (100, 214), 'C': (100, 260), 'G': (100, 306)},
   {'B': 'A', 'E': 'B', 'F': 'B', 'K': 'E', 'L': 'E', 'C': 'L', 'G': 'C'}, t)
F.line(170, 190, 220, 190, LINE, 1.6, arrow='end'); F.text(195, 176, '压缩', 12, color=MUTED)
up({'A': (320, 96), 'E': (260, 152), 'B': (320, 152), 'L': (380, 152), 'K': (260, 208), 'F': (320, 208), 'C': (380, 208), 'G': (380, 264)},
   {'E': 'A', 'B': 'A', 'L': 'A', 'K': 'E', 'F': 'B', 'C': 'L', 'G': 'C'}, t)
code(F, 450, 86, '// Find：先找到根，再压缩路径\nint Find(int S[], int x) {\n  int root = x;\n  while (S[root] >= 0)\n    root = S[root];      // 循环找到根\n  while (x != root) {    // 压缩路径\n    int t = S[x];        // t 指向 x 的父结点\n    S[x] = root;         // x 直接挂到根下\n    x = t;\n  }\n  return root;\n}', 12)
els = list('ABCDEFGHIJKLM'); S = ['-8', '0', '11', '-5', '0', '1', '2', '3', '3', '3', '4', '0', '7']
F.text(84, 370, '元素', 12.5, 'end', INK2, valign='middle')
F.cells(96, 358, els, 44, 24, size=12, mono=False)
F.text(84, 396, 'S[]', 12.5, 'end', INK2, valign='middle', mono=True)
F.cells(96, 384, S, 44, 26, {1: 'green', 4: 'green', 11: 'green'}, size=12)
F.text(96, 430, '根存 −(结点数)；绿色为被改写的 S[]', 12, 'start', MUTED)
