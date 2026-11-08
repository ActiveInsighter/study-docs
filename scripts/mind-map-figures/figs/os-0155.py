from common import proc_space
LABEL = '用户级线程的调度：内核选进程分配时间片，运行时系统在进程内选线程'
F = Fig(560, 430, '用户级线程的调度')
proc_space(F, 0, 30, 'user', sched=True)
F.box(290, 294, 90, 22, '调度程序', 'blue', 11, 3); F.line(382, 305, 418, 305, INK2, 1.2, arrow='end')
F.text(280, 418, '(1) 内核选择一个进程并为其分配时间片　(2) 运行时系统在进程内选择一个线程', 11, color=ACCENT['red'])
