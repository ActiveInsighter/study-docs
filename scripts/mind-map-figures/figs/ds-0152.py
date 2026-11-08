LABEL = '并查集：将各个元素划分为若干个互不相交的子集'
F = Fig(640, 312, '将元素划分为若干互不相交的子集')
groups = [('S_{0}', 'green', {'A': (130, 92), 'B': (130, 148), 'E': (90, 196), 'F': (170, 196), 'K': (60, 248), 'L': (130, 248)}),
          ('S_{1}', 'violet', {'C': (300, 120), 'G': (300, 200)}),
          ('S_{2}', 'amber', {'D': (480, 100), 'H': (420, 160), 'I': (480, 160), 'J': (540, 160), 'M': (420, 220)})]
for name, t, nodes in groups:
    xs = [p[0] for p in nodes.values()]; ys = [p[1] for p in nodes.values()]
    F.rect(min(xs) - 36, 62, max(xs) - min(xs) + 72, 214, 'none', '#a1a1aa', 1.2, 18, dash='5 4')
    for k, (x, y) in nodes.items():
        F.circle(x, y, 19, k, t, 14, dash='3 3')
    F.text((min(xs) + max(xs)) / 2, 294, '子集 ' + name, 13.5, color=INK2, weight=600)
