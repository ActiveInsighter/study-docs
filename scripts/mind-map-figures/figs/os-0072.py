LABEL = '多级反馈队列调度：时间片逐级加倍，未完成的进程降入下一级队列'
F = Fig(720, 280, '多级反馈队列')
for i, (lab, ts, tone) in enumerate((('（FCFS）队列 1', '10ms', 'amber'), ('（FCFS）队列 2', '20ms', 'amber'), ('（FCFS + RR）队列 3', '40ms', 'green'))):
    y = 80 + i * 66
    F.text(150, y + 14, lab, 12, 'end', INK2, valign='middle')
    F.rect(160, y - 4, 320, 36, 'none', INK2, 1, 4); F.pill(166, y - 16, ts, 'blue', 10)
    for j in range(3): F.box(170 + j * 50, y + 2, 40, 24, '进程', tone, 10.5, 3)
    F.text(340, y + 14, '…', 13, color=MUTED, valign='middle'); F.box(380, y + 2, 40, 24, '进程', tone, 10.5, 3)
    F.line(482, y + 14, 540, y + 14, INK2, 1.3, arrow='end'); F.box(542, y, 30, 28, 'CPU', 'violet', 9.5, 3); F.line(574, y + 14, 620, y + 14, INK2, 1.3, arrow='end'); F.text(626, y + 14, '完成', 12, 'start', INK2, valign='middle')
    if i < 2: F.poly([(557, y + 30), (557, y + 46), (165, y + 46), (165, y + 62)], LINE, 1.2, dash='3 3', arrow='end')
F.poly([(557, 80 + 2 * 66 + 30), (557, 80 + 2 * 66 + 46), (165, 80 + 2 * 66 + 46), (165, 80 + 2 * 66 + 30)], LINE, 1.2, dash='3 3', arrow='end')
F.text(360, 272, '时间片用完未结束则降入下一级；只有上级队列为空时才调度下级队列', 11.5, color=MUTED)
