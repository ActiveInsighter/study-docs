LABEL = 'UMA 统一存储访问：所有处理器对内存的访问时间一致'
F = Fig(640, 360, 'UMA（Uniform Memory Access）')
def cpu(x, y, name):
    F.text(x + 75, y - 8, name, 11.5, color=INK, weight=600)
    F.cells(x, y, ['core1', '……', 'coreN'], 50, 24, {0: 'red', 1: 'red', 2: 'red'}, size=10, mono=False)
    F.box(x, y + 24, 150, 22, 'cache', 'teal', 10.5, 0)
cpu(60, 70, 'cpu1'); cpu(430, 70, 'cpuN'); F.text(320, 92, '……', 13, color=MUTED)
F.items.append('<path d="M40 180L70 162V172H570V162L600 180L570 198V188H70V198Z" fill="#fef3c7" stroke="#c98a12" stroke-width="1.2"/>'); F.text(612, 180, 'Bus', 12, 'start', INK, 700, valign='middle')
for x in (135, 505): F.line(x, 118, x, 160, '#c98a12', 2.6, arrow='both')
F.rect(150, 240, 340, 46, '#fdf1d8', ACCENT['amber'], 1.2, 6); F.text(500, 263, 'Memory', 12, 'start', INK, 700, valign='middle')
for i, r in enumerate(('ram1', 'ram2', '……', 'ramN')): F.box(162 + i * 82, 250, 70, 26, r, 'violet', 10.5, 3)
F.line(320, 200, 320, 238, '#c98a12', 2.6, arrow='both')
F.text(320, 314, '每个处理器可以有私有 Cache；bus 资源一定时，随 CPU / core 增多，', 11.5, color=MUTED)
F.text(320, 334, '整体处理性能并不能线性提高，内存带宽成为性能瓶颈', 11.5, color=MUTED)
