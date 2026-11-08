LABEL = '无缓冲时的处理时间：磁盘→缓冲区 100us，缓冲区→用户区 50us，CPU 分析 50us'
F = Fig(700, 330, '计算周期（假设工作区已满）')
for i, (t, d) in enumerate((('磁盘', '100us'), ('缓冲区', '50us'), ('用户区（工作区）', '50us'), ('分析', ''))):
    x = 40 + i * 160
    F.box(x, 56, 110 if i < 3 else 70, 28, t, 'blue', 11.5, 4)
    if i < 3: F.line(x + 112, 70, x + 156, 70, ACCENT['blue'], 3, arrow='end'); F.text(x + 134, 96, d, 11, color=INK2)
F.text(640, 96, '50us', 11, color=INK2)
labs = [('磁盘 → 缓冲区', 150, 'gray'), ('缓冲区 → 用户区', 190, 'green'), ('CPU 分析', 230, 'amber')]
for t, y, tone in labs: F.text(110, y, t, 11.5, 'end', INK2, valign='middle')
F.line(120, 270, 680, 270, INK2, 1.3, arrow='end'); F.line(120, 270, 120, 120, INK2, 1.3, arrow='end')
for k, x0 in enumerate((130, 280, 460)):
    F.rect(x0, 144, 100, 10, TONES['gray'][1], 'none', 0, 2); F.rect(x0 + 100, 184, 50, 10, TONES['green'][1], 'none', 0, 2); F.rect(x0 + 150, 224, 50, 10, TONES['amber'][1], 'none', 0, 2)
F.text(440, 190, '……', 14, color=MUTED)
for x, t in ((130, '0'), (230, '100'), (280, '150'), (610, '1500')): F.text(x, 288, t, 11, color=INK2, mono=True)
F.text(400, 318, '单缓冲：每块的处理时间为 max(C, T) + M = 150us', 11.5, color=MUTED)
