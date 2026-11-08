LABEL = '完全二叉树的编号规律：下标从 1 或从 0 开始'
F = Fig(620, 300, '完全二叉树的编号规律')
for k, (x0, base, lt, rt) in enumerate(((20, 1, 'i × 2', 'i × 2 + 1'), (320, 0, '(i+1) × 2 − 1', '(i+1) × 2'))):
    nm = lambda i: str(i - 1 + base)
    P = {1: (x0 + 140, 112), 2: (x0 + 70, 180), 3: (x0 + 210, 180), 4: (x0 + 35, 248), 5: (x0 + 105, 248), 6: (x0 + 175, 248), 7: (x0 + 245, 248)}
    for i in range(2, 8):
        F.line(*P[i // 2], *P[i], INK2, 1.4, gap=17, gap2=17)
    for i, (x, y) in P.items():
        F.circle(x, y, 17, nm(i), 'red' if i == 1 else ('amber' if i < 4 else 'green'), 14, mono=True)
    F.curve(x0 + 120, 104, x0 + 64, 158, -0.35, ACCENT['blue'], 1.4)
    F.curve(x0 + 160, 104, x0 + 216, 158, 0.35, ACCENT['blue'], 1.4)
    F.text(x0 + 40, 120, lt, 12.5, 'middle', ACCENT['blue'], 600, mono=True)
    F.text(x0 + 244, 120, rt, 12.5, 'middle', ACCENT['blue'], 600, mono=True)
    F.text(x0 + 140, 78, f'下标从 {base} 开始', 13, color=INK2, weight=600)
F.text(310, 290, '双亲：从 1 开始为 ⌊i/2⌋；从 0 开始为 ⌊(i−1)/2⌋', 12.5, color=MUTED)
