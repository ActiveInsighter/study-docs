LABEL = 'TCB（线程控制块）的内容'
F = Fig(620, 290, 'TCB（线程控制块）')
F.rect(150, 56, 140, 220, 'blue', ACCENT['blue'], 1.2, 6); F.text(220, 72, 'TCB', 12, color=INK2)
rows = [('线程标识符', 'TID，与 PID 类似', 'white'), ('程序计数器 PC', '线程目前执行到哪里', 'amber'), ('其他寄存器', '线程运行的中间结果', 'amber'), ('堆栈指针', '堆栈保存函数调用信息、局部变量等', 'amber'), ('线程运行状态', '运行 / 就绪 / 阻塞', 'white'), ('优先级', '线程调度、资源分配的参考', 'white')]
for i, (a, b, t) in enumerate(rows):
    y = 84 + i * 30
    F.box(162, y, 116, 28, a, t, 12, 0); F.line(280, y + 14, 320, y + 14, INK2, 1.2, arrow='end'); F.text(326, y + 14, b, 12, 'start', INK2, valign='middle')
F.vbrace(156, 116, 200, '线程切换时\n要保存 / 恢复', right=False)
