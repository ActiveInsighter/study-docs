LABEL = '分页存储原理：进程的页离散地放入内存的页框中'
F = Fig(560, 440, '分页：页 → 页框')
for i in range(4): F.box(40, 70 + i * 60, 150, 60, f'进程 A 的页 {i}（4KB）', 'amber', 12.5, 0)
frames = [('页框 0（4KB）', 'green'), ('A 的页 2', 'amber'), ('A 的页 0', 'amber'), ('A 的页 3', 'amber'), ('……', 'blue'), ('A 的页 1', 'amber'), ('页框 n−1', 'light')]
for i, (t, tone) in enumerate(frames): F.box(270, 60 + i * 50, 150, 50, t, tone, 12.5, 0)
F.text(440, 84, '低地址', 13, 'start', INK, 700); F.text(440, 396, '高地址', 13, 'start', INK, 700); F.line(470, 100, 470, 376, INK2, 1.4, arrow='end')
F.text(115, 330, '进程的逻辑地址空间', 11.5, color=MUTED); F.text(345, 428, '物理内存（页框）', 11.5, color=MUTED)
