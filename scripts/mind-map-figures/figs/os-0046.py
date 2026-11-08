LABEL = '线程三状态模型：就绪、运行、阻塞'
F = Fig(560, 330, '线程的状态与转换')
P = {'就绪': (90, 110), '运行': (470, 110), '阻塞': (280, 270)}
for k, (x, y) in P.items(): F.ellipse(x, y, 56, 30, k, {'就绪': 'blue', '运行': 'green', '阻塞': 'amber'}[k], 15)
F.line(146, 100, 412, 100, INK2, 1.5, arrow='end'); F.text(280, 88, '(3) 被调度程序选中', 12.5, color=INK2)
F.line(412, 120, 146, 120, INK2, 1.5, arrow='end'); F.text(280, 140, '(2) 时间用完', 12.5, color=INK2)
F.line(440, 136, 316, 244, INK2, 1.5, arrow='end'); F.text(440, 200, '(1) 等待某事件', 12.5, 'start', INK2)
F.line(244, 244, 118, 136, INK2, 1.5, arrow='end'); F.text(120, 200, '(4) 等待的事件发生', 12.5, 'end', INK2)
