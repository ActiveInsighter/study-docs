LABEL = '硬件多线程：单核处理器中为每个线程准备独立的寄存器组和 PC'
F = Fig(620, 330, '硬件多线程（单核处理器）')
F.rect(20, 56, 440, 220, '#fafafa', '#a1a1aa', 1.2, 10); F.text(240, 72, '单核处理器', 11.5, color=INK, weight=600)
for k, x in enumerate((40, 250)):
    F.rect(x, 84, 190, 70, 'white', '#a1a1aa', 1.1, 6); F.text(x + 95, 98, f'线程 {k + 1} 的寄存器组', 11, color=INK2)
    F.box(x + 14, 108, 80, 34, '通用寄\n存器组', 'green', 10.5, 3); F.box(x + 110, 108, 60, 34, 'PC', 'red', 11, 3)
for i in range(3):
    x = 80 + i * 120
    F.items.append(f'<path d="M{x} 176H{x + 80}L{x + 66} 200H{x + 14}Z" fill="#fdf1d8" stroke="#c98a12" stroke-width="1.2"/>'); F.text(x + 40, 188, '功能部件', 10.5, color='#78350f', valign='middle')
F.box(80, 222, 120, 26, '指令发射槽', 'amber', 11, 3); F.box(280, 222, 120, 26, '指令发射槽', 'amber', 11, 3)
F.box(490, 80, 110, 196, '主存储器\n\n多模块交叉\n存储器', 'blue', 11, 4)
F.line(20, 298, 610, 298, INK2, 2); F.text(320, 312, '总线', 10.5, color=MUTED)
