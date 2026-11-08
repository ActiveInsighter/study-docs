LABEL = '动态分区分配：进程按需分配，回收后产生外部碎片'
F = Fig(760, 280, '动态分区分配')
cols = [[('OS', 8, 'dark'), ('', 56, 'white')], [('OS', 8, 'dark'), ('进程 1', 20, 'amber'), ('进程 2', 14, 'amber'), ('进程 3', 18, 'amber'), ('', 4, 'white')],
        [('OS', 8, 'dark'), ('进程 1', 20, 'amber'), ('', 14, 'white'), ('进程 3', 18, 'amber'), ('', 4, 'white')], [('OS', 8, 'dark'), ('进程 1', 20, 'amber'), ('进程 4', 8, 'amber'), ('', 6, 'white'), ('进程 3', 18, 'amber'), ('', 4, 'white')],
        [('OS', 8, 'dark'), ('', 20, 'white'), ('进程 4', 8, 'amber'), ('', 6, 'white'), ('进程 3', 18, 'amber'), ('', 4, 'white')], [('OS', 8, 'dark'), ('进程 2', 14, 'amber'), ('', 6, 'white'), ('进程 4', 8, 'amber'), ('', 6, 'white'), ('进程 3', 18, 'amber'), ('', 4, 'white')]]
for k, col in enumerate(cols):
    x = 30 + k * 122; y = 60
    for t, mb, tone in col:
        h = mb * 3
        F.box(x, y, 70, h, t, tone, 10.5, 0)
        F.text(x + 74, y + h / 2, f'{mb} MB', 9.5, 'start', ACCENT['red'] if tone == 'white' and k else MUTED, valign='middle'); y += h
F.text(380, 268, '空闲区（白色）被切得越来越碎：外部碎片', 11.5, color=MUTED)
