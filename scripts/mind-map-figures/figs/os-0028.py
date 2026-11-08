from common import proc_space
LABEL = '线程库支持的线程（用户级线程）：TCB 在用户空间，由运行时系统管理'
F = Fig(560, 420, '线程库支持的线程（用户级线程）')
proc_space(F, 0, 30, 'user')
F.text(100, 410, 'Runtime 运行时系统（由线程库实现）', 11, color=INK2); F.line(100, 398, 150, 252, ACCENT['blue'], 1, arrow='end')
