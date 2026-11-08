LABEL = '电路交换：通话前建立一条专用的物理通路'
F = Fig(760, 320, '电路交换')
sw = {'S1': (220, 140), 'S2': (370, 50), 'S3': (470, 160), 'S4': (620, 60)}
for k, (x, y) in sw.items():
    F.box(x, y, 50, 100, '', 'white', rx=2)
    for i in range(4):
        F.circle(x - 4, y + 15 + i * 24, 4, '', 'white', sw=1); F.circle(x + 54, y + 15 + i * 24, 4, '', 'white', sw=1)
    F.text(x + 25, y - 10, '交换机', 11, color=INK2)
phones = {'A': (40, 110), 'C': (40, 170), 'D': (40, 220), 'B': (720, 160)}
for k, (x, y) in phones.items(): F.box(x - 14, y - 10, 28, 20, '☎', 'white', 12, 4); F.text(x - 22, y, k, 12, 'end', INK, 700, valign='middle')
blue = ACCENT['blue']
F.poly([(54, 110), (216, 179), (274, 203), (366, 89), (424, 113), (466, 223), (524, 223), (616, 123), (674, 123), (706, 160)], blue, 2, arrow=None)
F.line(54, 170, 216, 203, ACCENT['red'], 1.4); F.line(54, 220, 216, 227, ACCENT['red'], 1.4)
F.text(100, 82, '用户线', 11, color=INK2); F.text(330, 160, '中继线', 11, color=INK2); F.text(680, 110, '用户线', 11, color=INK2)
F.text(150, 290, 'C、D 可以通过本地交换机实现通信；蓝线为 A 与 B 之间建立的专用电路', 11.5, 'start', ACCENT['red'])
