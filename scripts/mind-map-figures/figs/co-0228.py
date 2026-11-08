LABEL = 'NUMA 非统一存储访问：每个处理器有自己的本地内存，访问本地更快'
F = Fig(640, 330, 'NUMA（Non-Uniform Memory Access）')
for x, n in ((60, 'cpu1'), (430, 'cpuN')):
    F.text(x + 75, 62, n, 11.5, color=INK, weight=600)
    F.cells(x, 70, ['core1', '……', 'coreN'], 50, 24, {0: 'red', 1: 'red', 2: 'red'}, size=10, mono=False); F.box(x, 94, 150, 22, 'cache', 'teal', 10.5, 0)
    F.line(x + 75, 118, x + 75, 156, '#c98a12', 2.6, arrow='both')
    F.rect(x, 158, 150, 60, '#fdf1d8', ACCENT['amber'], 1.2, 6); F.text(x + 8, 172, 'Memory' + ('1' if x == 60 else 'N'), 10.5, 'start', INK, 700)
    for i, r in enumerate(('ram1', '…', 'ramN')): F.box(x + 6 + i * 48, 182, 42, 26, r, 'violet', 9.5, 3)
    F.line(x + 75, 220, x + 75, 262, '#c98a12', 2.6, arrow='both')
F.text(320, 110, '……', 13, color=MUTED); F.text(320, 190, '……', 13, color=MUTED)
F.items.append('<path d="M40 282L70 264V274H570V264L600 282L570 300V290H70V300Z" fill="#fef3c7" stroke="#c98a12" stroke-width="1.2"/>'); F.text(612, 282, 'Bus', 12, 'start', INK, 700, valign='middle')
F.text(320, 320, '访问本地内存快、访问其他处理器的内存慢', 11.5, color=MUTED)
