from common import wave_clock, wave_bus, wave_level
LABEL = '同步定时：统一时钟，T1 给地址、T2 读命令、T3 取数据、T4 撤销'
F = Fig(640, 360, '同步定时（读操作）')
X0, T = 120, 110
F.line(X0 + 10, 72, X0 + 4 * T + 10, 72, ACCENT['green'], 1.4, arrow='both'); F.box(X0 + 2 * T - 60, 58, 140, 24, '总线传输周期', 'green', 11.5, 5)
F.text(90, 112, '时钟', 12.5, 'end', INK, valign='middle'); wave_clock(F, X0 - 10, 124, 4, T); F.path(f'M{X0 + 4 * T - 10} 124H{X0 + 4 * T + 40}', INK, 1.6)
for i in range(4):
    F.line(X0 + i * T + 6, 140, X0 + (i + 1) * T + 6, 140, ACCENT['violet'], 1, arrow='both'); F.text(X0 + i * T + T / 2 + 6, 152, f'T_{{{i + 1}}}', 11.5, color=ACCENT['violet'])
for i in range(5): F.line(X0 + i * T + 6, 80, X0 + i * T + 6, 330, LINE, 0.8, dash='3 4')
F.text(90, 190, '地址', 12.5, 'end', INK, valign='middle'); wave_bus(F, 190, [(X0 + 6, X0 + 4 * T + 6, '地址有效')], 'blue')
F.text(90, 246, '读命令', 12.5, 'end', INK, valign='middle'); wave_level(F, [(X0 - 20, 236), (X0 + T + 6, 256), (X0 + 3 * T + 6, 236), (X0 + 4 * T + 40, 236)], ACCENT['amber'])
F.text(90, 302, '数据', 12.5, 'end', INK, valign='middle'); wave_bus(F, 302, [(X0 + 2 * T + 6, X0 + 3 * T + 6, '数据')], 'red')
F.text(330, 350, '读命令低电平有效；从设备须在 T3 上升沿前把数据送上数据总线', 11.5, color=MUTED)
