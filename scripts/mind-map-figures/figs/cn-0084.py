LABEL = '虚拟局域网 VLAN：把局域网内的设备划分成与物理位置无关的逻辑组'
F = Fig(700, 300, '虚拟局域网 VLAN')
cores = {'c': (350, 170), 'l1': (200, 110), 'l2': (500, 110), 'l3': (200, 230), 'l4': (500, 230)}
for k in ('l1', 'l2', 'l3', 'l4'): F.line(*cores['c'], *cores[k], ACCENT['blue'], 1.2)
for k, (x, y) in cores.items(): F.ellipse(x, y, 16, 8, '', 'teal')
groups = {'l1': (60, ['y', 'y', 'y', 'g']), 'l2': (360, ['y', 'y', 'y', 'g']), 'l3': (60, ['y', 'g', 'g', 'g']), 'l4': (360, ['y', 'g', 'g', 'g'])}
for k, (x0, tones) in groups.items():
    yy = 56 if k in ('l1', 'l2') else 270
    for i, t in enumerate(tones):
        x = x0 + 30 + i * 70
        F.box(x - 14, yy - 10, 28, 20, '', 'amber' if t == 'y' else 'gray', rx=3); F.line(x, yy + (10 if yy < 100 else -10), *cores[k], ACCENT['blue'], 1)
F.legend(560, 160, [('gray', 'VLAN1')]); F.legend(560, 186, [('amber', 'VLAN2')])
F.text(620, 230, '每个 VLAN 是一个\n单独的广播域', 11, 'middle', MUTED, lh=1.4)
