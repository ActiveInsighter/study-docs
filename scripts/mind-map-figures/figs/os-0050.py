LABEL = '多级队列调度：按进程类型分成不同优先级的队列'
F = Fig(560, 330, '多级队列调度')
for i, t in enumerate(('系统进程', '交互进程', '交互编辑进程', '批处理进程', '学生进程')):
    y = 70 + i * 44
    F.line(30, y + 15, 90, y + 15, ACCENT['blue'], 2, arrow='end')
    F.box(92, y, 360, 30, t, 'blue', 13, 4)
    F.line(454, y + 15, 530, y + 15, ACCENT['blue'], 2, arrow='end')
F.text(30, 62, '最高优先级', 11.5, 'start', ACCENT['red']); F.text(30, 304, '最低优先级', 11.5, 'start', MUTED)
F.text(280, 316, '进程固定分配到某一队列；队列之间按优先级（或时间片）调度', 11.5, color=MUTED)
