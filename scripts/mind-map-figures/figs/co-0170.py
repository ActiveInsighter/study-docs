LABEL = '不共享 Cache 的双核 CPU 结构'
F = Fig(460, 400, '不共享 Cache 的双核 CPU')
F.rect(30, 56, 400, 260, '#d4d4d8', '#71717a', 1.2, 20)
F.line(230, 66, 230, 306, '#52525b', 1.2, dash='5 4')
for k, x in enumerate((50, 250)):
    F.box(x + 20, 70, 120, 30, f'CPU 核{k + 1}', 'dark', 13, 4)
    F.rect(x + 10, 112, 140, 140, '#52525b', '#3f3f46', 1.2, 14)
    for i, t in enumerate(('CPU 状态', '中断逻辑', '执行单元')): F.box(x + 25, 124 + i * 40, 110, 32, t, 'gray', 12, 4)
    F.box(x + 25, 266, 110, 34, 'Cache', 'blue', 13, 4)
    F.line(x + 80, 302, x + 80, 334, INK2, 1.6)
F.box(30, 336, 400, 30, '内存', 'gray', 13, 4)
F.text(230, 388, '每个核有自己独立的 Cache', 12, color=MUTED)
