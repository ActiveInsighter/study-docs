LABEL = '进程的七状态模型：在五状态基础上增加就绪挂起与阻塞挂起'
F = Fig(700, 340, '进程的七状态模型')
P = {'创建态': (70, 80), '就绪态': (240, 80), '运行态': (440, 80), '终止态': (620, 80), '就绪挂起': (200, 190), '阻塞态': (500, 190), '阻塞挂起': (350, 280)}
for k, (x, y) in P.items(): F.box(x - 52, y - 18, 104, 36, k, 'blue' if '挂起' not in k else 'violet', 13.5, 18)
def e(a, b, lab, dx=0, dy=0, c='blue', bend=0):
    (x1, y1), (x2, y2) = P[a], P[b]
    import math
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    sx, sy, ex, ey = x1 + ux * 40 + dx, y1 + uy * 22 + dy, x2 - ux * 44 + dx, y2 - uy * 24 + dy
    F.line(sx, sy, ex, ey, ACCENT[c], 1.5, arrow='end')
    F.text((sx + ex) / 2 - uy * 12, (sy + ey) / 2 + ux * 12 - 4, lab, 10.5, color=ACCENT[c], halo=True)
e('创建态', '就绪态', '创建'); e('就绪态', '运行态', '获得 CPU', dy=-6); e('运行态', '就绪态', '时间片到', dy=6); e('运行态', '终止态', '退出')
e('运行态', '阻塞态', '事件等待'); e('阻塞态', '就绪态', '事件发生')
e('创建态', '就绪挂起', '内存不足', c='violet'); e('就绪态', '就绪挂起', '挂起', dx=-6, c='violet'); e('就绪挂起', '就绪态', '激活', dx=6, c='violet')
e('阻塞态', '阻塞挂起', '挂起', dx=6, c='violet'); e('阻塞挂起', '阻塞态', '激活', dx=-6, c='violet'); e('阻塞挂起', '就绪挂起', '事件出现', c='violet')
e('运行态', '就绪挂起', '内存被抢占', c='violet')
