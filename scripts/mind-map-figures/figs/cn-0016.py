LABEL = '传输层的功能：为应用进程之间提供端到端的逻辑通信；IP 层提供主机之间的逻辑通信'
F = Fig(760, 420, '传输层：进程之间的逻辑通信')
def stack(x, name, aps):
    F.text(x + 50, 60, name, 11.5, color=INK, weight=600)
    for i in range(5):
        F.box(x, 70 + i * 34, 100, 34, '', 'white', rx=0); F.text(x - 6, 87 + i * 34, str(5 - i), 10, 'end', MUTED, valign='middle')
    for j, ap in enumerate(aps): F.ellipse(x + 30 + j * 40, 82 + (j % 2) * 10, 18, 9, ap, 'white', 10)
stack(40, '主机 A 的协议栈', ['AP1', 'AP2']); stack(620, '主机 B 的协议栈', ['AP3', 'AP4'])
F.line(150, 112, 610, 112, INK2, 1.2, arrow='both'); F.text(380, 104, '传输层提供应用进程间的逻辑通信', 11.5, color=INK, halo=True)
F.rect(250, 140, 110, 100, 'none', INK2, 1, 4); F.rect(400, 140, 110, 100, 'none', INK2, 1, 4); F.text(380, 154, 'IP 层', 11.5, color=INK2)
F.path('M90 240V250H690V240', INK2, 1.1, dash='6 4')
F.box(40, 290, 80, 60, '', 'white', rx=4); F.box(640, 290, 80, 60, '', 'white', rx=4); F.text(80, 284, '主机 A', 10.5, color=INK2); F.text(680, 284, '主机 B', 10.5, color=INK2)
for x in (50, 650): F.ellipse(x + 30, 306, 18, 9, 'AP1' if x == 50 else 'AP3', 'white', 9.5); F.ellipse(x + 30, 334, 18, 9, 'AP2' if x == 50 else 'AP4', 'white', 9.5)
F.line(122, 320, 270, 320, INK2, 1.2); F.text(196, 312, 'LAN1', 10.5, color=INK2); F.ellipse(290, 320, 20, 10, '', 'teal'); F.text(290, 300, '路由器 1', 10.5, color=INK2)
F.line(310, 320, 450, 320, INK2, 1.2); F.text(380, 312, 'WAN', 10.5, color=INK2); F.ellipse(470, 320, 20, 10, '', 'teal'); F.text(470, 300, '路由器 2', 10.5, color=INK2)
F.line(490, 320, 638, 320, INK2, 1.2); F.text(564, 312, 'LAN2', 10.5, color=INK2)
F.line(122, 372, 638, 372, ACCENT['green'], 1.2, arrow='both'); F.text(380, 366, 'IP 的作用范围（主机之间）', 11, color=ACCENT['green'], halo=True)
F.line(40, 402, 720, 402, ACCENT['blue'], 1.2, arrow='both'); F.text(380, 396, '传输层协议的作用范围（进程之间）', 11, color=ACCENT['blue'], halo=True)
