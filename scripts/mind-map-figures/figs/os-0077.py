LABEL = '调度对象：不支持内核级线程时是进程，支持时是内核线程'
F = Fig(560, 330)
for k, (lab, note) in enumerate((('进程', '不支持内核级线程的操作系统，调度程序的处理对象是进程'), ('内核线程', '支持内核级线程的操作系统，调度程序的处理对象是内核线程'))):
    y = 30 + k * 150
    for i, t in enumerate(['1', '2', '3', '……', 'n']):
        F.box(70 + i * 84, y, 84, 44, f'{lab}{t}' if t != '……' else '……', 'blue' if t != '……' else 'white', 12, 0)
    F.box(40, y + 44, 480, 44, '调度程序（scheduler）', 'white', 14, 0)
    F.text(280, y + 112, note, 12, color=INK2)
