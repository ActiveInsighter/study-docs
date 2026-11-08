from common import wave_clock
LABEL = '定长的机器周期：每个机器周期都是 4 个节拍'
F = Fig(760, 230, '定长的机器周期')
T = 40
X0 = 60
F.text(50, 86, 'CLK', 12, 'end', INK, valign='middle', mono=True); wave_clock(F, X0, 96, 12, T)
x = X0
for i in range(4): F.text(x + i * T + T / 2, 112, 'T_{%d}' % i, 11, color=ACCENT['violet'])
F.line(x, 124, x + 4 * T, 124, INK2, 1.1, arrow='both'); F.text(x + 4 * T / 2, 142, '机器周期（取指令）', 11.5, color=INK2)
F.line(x, 70, x, 160, LINE, 0.8, dash='3 3')
x += 4 * T
for i in range(4): F.text(x + i * T + T / 2, 112, 'T_{%d}' % i, 11, color=ACCENT['violet'])
F.line(x, 124, x + 4 * T, 124, INK2, 1.1, arrow='both'); F.text(x + 4 * T / 2, 142, '机器周期（取数 / 存数）', 11.5, color=INK2)
F.line(x, 70, x, 160, LINE, 0.8, dash='3 3')
x += 4 * T
for i in range(4): F.text(x + i * T + T / 2, 112, 'T_{%d}' % i, 11, color=ACCENT['violet'])
F.line(x, 124, x + 4 * T, 124, INK2, 1.1, arrow='both'); F.text(x + 4 * T / 2, 142, '机器周期（执行指令）', 11.5, color=INK2)
F.line(x, 70, x, 160, LINE, 0.8, dash='3 3')
x += 4 * T
F.line(x, 70, x, 160, LINE, 0.8, dash='3 3')
F.line(X0, 174, X0 + 12 * T, 174, ACCENT['red'], 1.3, arrow='both'); F.text(X0 + 12 * T / 2, 192, '指令周期', 12, color=ACCENT['red'], weight=600)
