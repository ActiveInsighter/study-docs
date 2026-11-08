from common import threads_model
LABEL = '线程的实现方式：用户级、内核级、组合方式'
F = Fig(760, 330, '线程的实现方式')
threads_model(F, 'user', 20, 0, '(a) 用户级方式')
threads_model(F, 'kernel', 270, 0, '(b) 内核级方式')
threads_model(F, 'combo', 520, 0, '(c) 组合方式')
F.text(380, 296, '用户级线程（波浪线）· 内核级线程（蓝圈）· 进程（绿圈）；操作系统只“看得见”内核级线程', 11.5, color=MUTED)
