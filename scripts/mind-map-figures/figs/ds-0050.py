LABEL = '二叉树示意'
F = Fig(300, 170, bg=True)
P = {'r': (150, 34), 'a': (90, 86), 'b': (210, 86), 'c': (60, 138), 'd': (120, 138), 'e': (180, 138), 'f': (240, 138)}
for a, b in (('r', 'a'), ('r', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('b', 'f')):
    F.line(*P[a], *P[b], INK2, 1.5, gap=15, gap2=15)
for k, (x, y) in P.items():
    F.circle(x, y, 15, '', 'dark' if k == 'r' else ('gray' if k in 'ab' else 'white'))
