from common import loser_tree
LABEL = '败者树下次比较：新元素沿路径与各层败者比较，只需比较 h 次'
F = Fig(800, 486, '败者树 · 下次比较（输出 1 后，3 号段补入 6）')
runs = [r[:] for r in __import__('common').RUNS8]
leaves = ['27', '12', '6', '17', '2', '9', '11', '4']
loser_tree(F, 20, 72, inner={4: '1', 5: '4', 6: '6', 7: '7', 2: '2', 3: '8', 1: '3'}, champ='5', leaves=leaves,
           hl_nodes=(5, 2, 1), hl_path={(10, 5), (5, 2), (2, 1)}, winners={5: '6胜', 2: '6胜', 1: '2胜'})
F.text(470, 58, '① 6 vs 4 号段 17 → 6 胜\n② 6 vs 2 号段 12 → 6 胜\n③ 6 vs 5 号段 2 → 5 号段胜出', 12.5, 'start', INK2, lh=1.5)
F.text(400, 468, '新元素只与路径上的败者比较，比较次数 = 树高 ⌈log₂k⌉；首次构造需 k−1 次', 12.5, color=MUTED)
