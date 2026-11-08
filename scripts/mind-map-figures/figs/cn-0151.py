LABEL = 'SDN 体系结构：网络控制应用程序、SDN 控制器、SDN 控制的交换机'
F = Fig(620, 420, 'SDN 体系结构')
F.text(310, 56, '网络控制应用程序', 12.5, color=ACCENT['blue'], weight=700)
for x, t in ((180, '路由选择'), (320, '接入控制'), (450, '负载均衡')): F.ellipse(x, 100, 52, 18, t, 'blue', 11.5)
F.line(60, 134, 520, 134, ACCENT['blue'], 1.2, dash='6 4'); F.text(590, 134, '北向 API', 11.5, 'end', ACCENT['blue'], valign='middle')
F.box(160, 150, 300, 50, 'SDN 控制器\n（网络操作系统）', 'blue', 12.5, 4)
F.line(60, 220, 520, 220, ACCENT['blue'], 1.2, dash='6 4'); F.text(590, 220, '南向 API', 11.5, 'end', ACCENT['blue'], valign='middle')
F.ellipse(310, 310, 180, 60, '', 'light')
import math
P = [(220, 290), (300, 280), (380, 290), (250, 330), (340, 340), (410, 320)]
for i, a in enumerate(P):
    for b in P[i + 1:]:
        if math.dist(a, b) < 120: F.line(*a, *b, ACCENT['blue'], 1)
for x, y in P: F.ellipse(x, y, 12, 6, '', 'teal')
for x in (220, 300, 380): F.line(x, 202, x, 278, ACCENT['blue'], 1, dash='3 3')
F.text(310, 396, 'SDN 控制的交换机', 12, color=ACCENT['blue'])
F.vbrace(50, 60, 214, '控制\n平面', right=False, size=11.5); F.vbrace(50, 226, 380, '数据\n平面', right=False, size=11.5)
