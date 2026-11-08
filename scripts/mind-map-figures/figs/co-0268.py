LABEL = '虚拟存储器的三个地址空间：主存（实地址）、程序（虚地址）、辅存'
F = Fig(760, 330, '虚拟存储器的三个地址空间')
F.text(150, 64, '主存地址空间（实地址）', 12.5, color=INK, weight=600)
tones = {2: 'blue', 4: 'green', 5: 'red', 7: 'amber'}
for i in range(8):
    F.box(100, 74 + i * 24, 110, 24, '', tones.get(i, 'white'), rx=0); F.text(92, 86 + i * 24, str(i), 11, 'end', MUTED, mono=True, valign='middle')
F.text(60, 76, '主存\n页号', 11, 'end', MUTED, lh=1.2)
F.text(155, 286, '主存', 12, color=INK2)
F.text(400, 64, '程序空间（虚地址）', 12.5, color=INK, weight=600)
for i, t in enumerate(('blue', 'green', 'red', 'amber')):
    F.box(350, 74 + i * 24, 110, 24, '4K', t, 11, 0); F.text(342, 86 + i * 24, str(i), 11, 'end', MUTED, mono=True, valign='middle')
F.text(310, 76, '虚拟\n页号', 11, 'end', MUTED, lh=1.2)
for i, j in enumerate((2, 4, 5, 7)):
    F.line(348, 86 + i * 24, 212, 86 + j * 24, INK2, 1.2, arrow='end')
F.text(620, 64, '辅存空间', 12.5, color=INK, weight=600)
for k in range(5): F.ellipse(620, 96 + k * 14, 60, 10, '', 'gray', sw=1.1)
F.text(620, 190, '硬盘、磁盘', 12, color=INK2)
F.text(350, 230, '实地址 = [[blue:主存页号]] + 页内字地址', 12.5, 'start', INK2)
F.text(350, 254, '虚地址 = [[red:虚存页号]] + 页内字地址', 12.5, 'start', INK2)
F.text(350, 278, '辅存地址 = [[violet:磁盘号 + 盘面号 + 磁道号 + 扇区号]]', 12.5, 'start', INK2)
