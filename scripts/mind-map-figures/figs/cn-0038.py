LABEL = '两个路由器之间有交换机时，帧一定是以太网帧而不是 PPP 帧'
F = Fig(560, 230)
F.box(130, 40, 40, 30, 'A', 'blue', 12, 4); F.box(390, 40, 40, 30, 'B', 'blue', 12, 4)
F.box(250, 120, 60, 30, '⇄', 'blue', 14, 4); F.text(280, 172, '交换机 1', 12.5, color=INK2)
for x, t in ((70, ''), (170, '路由器 0'), (390, '路由器 1'), (490, '')):
    F.circle(x, 135, 20, '⇄', 'blue', 13)
    if t: F.text(x, 180, t, 12.5, color=INK2)
F.line(90, 135, 150, 135, ACCENT['red'], 1.6); F.line(190, 135, 248, 135, ACCENT['red'], 1.6); F.line(312, 135, 370, 135, ACCENT['red'], 1.6); F.line(410, 135, 470, 135, ACCENT['red'], 1.6)
F.line(150, 72, 266, 118, ACCENT['red'], 1.6); F.line(410, 72, 296, 118, ACCENT['red'], 1.6)
F.text(280, 214, '路由器 0 与路由器 1 之间经过交换机（局域网）：以太网帧', 11, color=MUTED)
