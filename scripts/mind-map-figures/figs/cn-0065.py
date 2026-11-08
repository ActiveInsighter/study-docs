LABEL = '报文交换：各结点存储转发整个报文'
F = Fig(640, 200, '报文交换：存储 — 转发')
N = [(60, 140, 'A', '发送报文'), (220, 80, 'B', '等待 — 发送'), (400, 100, 'C', '等待 — 发送'), (570, 110, 'D', '')]
for x, y, n, t in N:
    F.box(x - 22, y - 16, 44, 32, '✉' if n in 'AD' else '⌛', 'blue' if n in 'AD' else 'amber', 15, 6)
    F.text(x, y - 26, n, 13, color=INK, weight=700); F.text(x, y + 32, t, 12, color=ACCENT['blue'])
for a, b in zip(N, N[1:]): F.curve(a[0] + 24, a[1], b[0] - 24, b[1], -0.2, INK2, 1.4); F.text((a[0] + b[0]) / 2, min(a[1], b[1]) - 18, '传输', 11.5, color=INK2)
