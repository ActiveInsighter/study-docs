from common import proc_space
LABEL = '内核支持的线程（内核级线程）：TCB 在内核的线程表中'
F = Fig(560, 420, '内核支持的线程（内核级线程）')
proc_space(F, 0, 30, 'kernel')
