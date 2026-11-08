from common import wave_clock, wave_bus, wave_level
LABEL = '半同步通信：同步时钟 + 异步 WAIT 信号，可插入等待周期 Tw'
F = Fig(700, 400, '半同步通信（插入 Tw 等待周期）')
X0, T = 110, 90
labs = ['T₁', 'T₂', 'T_{w}', 'T_{w}', 'T₃', 'T₄']
F.line(X0 + 6, 72, X0 + 6 * T + 6, 72, ACCENT['green'], 1.4, arrow='both'); F.box(X0 + 3 * T - 60, 58, 130, 24, '总线传输周期', 'green', 11.5, 5)
F.text(90, 112, '时钟', 12.5, 'end', INK, valign='middle'); wave_clock(F, X0 - 10, 124, 6, T)
for i, l in enumerate(labs):
    F.text(X0 + i * T + T / 2 + 6, 152, l, 11.5, color=ACCENT['violet'] if 'w' not in l else ACCENT['red'])
for i in range(7): F.line(X0 + i * T + 6, 80, X0 + i * T + 6, 370, LINE, 0.8, dash='3 4')
F.text(90, 186, '地址', 12.5, 'end', INK, valign='middle'); wave_bus(F, 186, [(X0 + 6, X0 + 6 * T + 6, '地址有效')], 'blue')
F.text(90, 236, '读命令', 12.5, 'end', INK, valign='middle'); wave_level(F, [(X0 - 20, 226), (X0 + T + 6, 246), (X0 + 5 * T + 6, 226), (X0 + 6 * T + 40, 226)], ACCENT['amber'])
F.text(90, 290, 'WAIT̄', 12.5, 'end', INK, valign='middle'); wave_level(F, [(X0 - 20, 280), (X0 + 2 * T + 6, 300), (X0 + 4 * T + 6, 280), (X0 + 6 * T + 40, 280)], ACCENT['violet'])
F.text(90, 340, '数据', 12.5, 'end', INK, valign='middle'); wave_bus(F, 340, [(X0 + 4 * T + 6, X0 + 5 * T + 6, '数据')], 'red')
F.text(350, 390, '从设备来不及在 T3 前给出数据时，发出 WAIT̄，主设备插入若干个 Tw', 11.5, color=MUTED)
