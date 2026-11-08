LABEL = '广域网是连接众多局域网的网络：结点交换机构成广域网核心'
F = Fig(760, 330, '广域网与局域网')
F.ellipse(380, 180, 160, 90, '', 'green'); F.text(380, 284, '广域网', 12, color=INK2); F.text(380, 50, '互联网', 12, color=INK2)
import math
sw = [(260, 150), (340, 120), (440, 130), (500, 190), (420, 230), (300, 220)]
for i, a in enumerate(sw):
    for b in sw[i + 1:]:
        if math.dist(a, b) < 200: F.line(*a, *b, INK2, 1)
for x, y in sw: F.box(x - 14, y - 9, 28, 18, '⇄', 'blue', 10, 3)
F.text(500, 100, '结点交换机', 11, color=INK2)
for side, x0 in ((0, 40), (1, 600)):
    for r in range(2):
        y = 120 + r * 80
        F.line(x0, y, x0 + 120, y, INK2, 1.2)
        for j in range(3): F.box(x0 + 10 + j * 38, y + 10, 24, 18, '', 'white', rx=2); F.line(x0 + 22 + j * 38, y, x0 + 22 + j * 38, y + 10, INK2, 1)
    F.text(x0 + 60, 104, '局域网', 11, color=INK2)
    rx = 180 if side == 0 else 580
    F.ellipse(rx, 160, 14, 7, '', 'teal'); F.line(rx, 160, sw[0 if side == 0 else 3][0], sw[0 if side == 0 else 3][1], INK2, 1)
    F.line(x0 + (120 if side == 0 else 0), 120, rx, 160, INK2, 1); F.line(x0 + (120 if side == 0 else 0), 200, rx, 160, INK2, 1)
F.text(180, 186, '路由器', 10.5, color=INK2, halo=True)
