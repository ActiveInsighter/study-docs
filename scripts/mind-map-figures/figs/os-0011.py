from common import proc_space
LABEL = '内核级线程的调度：内核直接选择一个线程并为其分配时间片'
F = Fig(560, 430, '内核级线程的调度')
proc_space(F, 0, 30, 'kernel')
F.box(100, 300, 90, 22, '调度程序', 'blue', 11, 3); F.line(192, 311, 238, 311, INK2, 1.2, arrow='end')
F.text(280, 418, '(1) 内核选择一个线程并为其分配时间片', 11, color=ACCENT['red'])
