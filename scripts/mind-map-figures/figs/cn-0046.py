LABEL = '一个典型的数据通信模型：源系统、传输系统、目的系统'
F = Fig(820, 300, '数据通信系统的模型')
F.text(30, 60, '发送：你好你好你好', 11.5, 'start', INK2); F.text(790, 60, '收到：你好你好你好', 11.5, 'end', INK2)
items = [(40, '信源', '输入信息', 'gray'), (190, '发送器', '输入数据', 'gray'), (350, '传输系统', '发送的信号', 'amber'), (510, '接收器', '接收的信号', 'green'), (660, '信宿', '输出数据', 'green')]
for x, t, lab, tone in items:
    F.box(x + 30, 110, 90, 30, t, tone, 12, 4)
    F.text(x + 20, 156, lab, 10.5, color=INK2)
F.line(20, 125, 68, 125, ACCENT['blue'], 1.2, arrow='end'); F.line(162, 125, 218, 125, ACCENT['blue'], 1.2, arrow='end'); F.line(312, 125, 378, 125, ACCENT['blue'], 1.2, arrow='end'); F.line(472, 125, 538, 125, ACCENT['blue'], 1.2, arrow='end'); F.line(632, 125, 688, 125, ACCENT['blue'], 1.2, arrow='end'); F.line(782, 125, 806, 125, ACCENT['blue'], 1.2, arrow='end')
F.text(790, 156, '输出信息', 10.5, color=INK2)
F.text(240, 92, '数字信号 → 调制解调器 → 模拟信号', 10.5, color=INK2); F.text(580, 92, '模拟信号 → 调制解调器 → 数字信号', 10.5, color=INK2)
F.line(330, 80, 330, 260, LINE, 1, dash='4 4'); F.line(500, 80, 500, 260, LINE, 1, dash='4 4')
F.box(110, 210, 110, 44, '源系统', 'gray', 14, 4); F.box(360, 210, 110, 44, '传输系统', 'amber', 14, 4); F.box(600, 210, 110, 44, '目的系统', 'green', 14, 4)
F.text(415, 92, '广域网（公用电话网）', 10.5, color=ACCENT['amber'])
