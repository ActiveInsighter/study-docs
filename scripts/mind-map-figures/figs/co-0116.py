from mp import core
LABEL = '共享存储多处理（SMP）系统：多核处理器共享 LLC 与主存'
F = Fig(700, 312, '共享存储多处理（SMP）系统 / 多核处理器')
F.rect(20, 56, 520, 210, '#fafafa', '#a1a1aa', 1.2, 10); F.text(280, 72, '处理器', 11.5, color=INK, weight=600)
for i in range(3):
    F.text(95 + i * 160, 92, f'核 core', 10.5, color=MUTED); core(F, 35 + i * 160, 100, 140, 110)
F.box(60, 222, 440, 26, 'LLC（Last-Level Cache，共享）', 'red', 11.5, 4)
F.box(570, 56, 80, 200, '主存储器', 'blue', 12, 4)
F.line(20, 282, 680, 282, INK2, 2); F.text(350, 296, '总线', 10.5, color=MUTED)
F.line(280, 266, 280, 282, INK2, 1.4); F.line(610, 256, 610, 282, INK2, 1.4)
F.text(610, 46, '如 Intel i5、i7', 10.5, color=MUTED)
