LABEL = '快重传与快恢复（TCP Reno）'
F = Fig(780, 420, '快重传与快恢复')
X0, Y0, SX, SY = 130, 360, 26, 11
F.line(X0, Y0, X0 + 24 * SX, Y0, INK2, 1.3, arrow='end'); F.line(X0, Y0, X0, 60, INK2, 1.3, arrow='end')
F.text(X0 + 24 * SX, Y0 + 30, '传输轮次', 12, 'end', INK2); F.text(X0 + 6, 52, '拥塞窗口 cwnd（单位 MSS）', 12, 'start', INK2)
for i in range(0, 23, 2): F.text(X0 + i * SX, Y0 + 16, str(i), 10.5, color=INK2, mono=True)
for v in (5, 10, 15, 20, 25): F.text(X0 - 8, Y0 - v * SY, str(v), 10.5, 'end', INK2, mono=True, valign='middle'); F.line(X0, Y0 - v * SY, X0 + 22 * SX, Y0 - v * SY, '#f0f0f0', 0.8)
T = [(12, 24), (13, 1), (14, 2), (15, 4), (16, 8), (17, 12), (18, 13), (19, 14), (20, 15), (21, 16), (22, 17)]
F.path('M' + 'L'.join(f'{X0 + a * SX} {Y0 - b * SY}' for a, b in T), ACCENT['amber'], 1.4, dash='4 3')
for a, b in T[1:]: F.circle(X0 + a * SX, Y0 - b * SY, 3, '', 'amber', sw=0)
F.text(X0 + 16 * SX, Y0 - 3 * SY, 'TCP Tahoe 版本（已废弃不用）', 10.5, 'start', ACCENT['amber'])
F.text(X0 + 19 * SX, Y0 - 24 * SY, 'TCP Reno 版本', 11, 'start', ACCENT['teal'])
F.text(X0 + 12 * SX, Y0 - 27 * SY, '收到 3 个重复的确认 → 执行快重传算法', 11, color=ACCENT['red'])
F.text(X0 + 13 * SX + 6, Y0 - 12 * SY + 18, '快恢复', 11, 'start', INK2)
P = [(0, 1), (1, 2), (2, 4), (3, 8), (4, 16), (5, 17), (6, 18), (7, 19), (8, 20), (9, 21), (10, 22), (11, 23), (12, 24), (13, 12), (14, 13), (15, 14), (16, 15), (17, 16), (18, 17), (19, 18), (20, 19), (21, 20), (22, 21)]
F.path('M' + 'L'.join(f'{X0 + a * SX} {Y0 - b * SY}' for a, b in P), ACCENT['teal'], 2)
for a, b in P: F.circle(X0 + a * SX, Y0 - b * SY, 3, '', 'teal', sw=0)
F.line(X0, Y0 - 16 * SY, X0 + 4 * SX, Y0 - 16 * SY, ACCENT['red'], 1, dash='3 3'); F.text(X0 - 8, Y0 - 16 * SY - 12, 'ssthresh 初值 16', 10, 'end', ACCENT['red'])
F.line(X0, Y0 - 12 * SY, X0 + 13 * SX, Y0 - 12 * SY, ACCENT['red'], 1, dash='3 3'); F.text(X0 - 8, Y0 - 12 * SY + 12, '新 ssthresh 12', 10, 'end', ACCENT['red'])
F.text(X0 + 2 * SX, Y0 + 40, '慢开始（指数增长）', 11.5, color=ACCENT['amber'])
F.text(X0 + 6 * SX, Y0 - 19 * SY - 40, '拥塞避免 “加法增大”', 11.5, color=ACCENT['teal'])
F.text(X0 + 13 * SX + 8, Y0 - 18 * SY, '“乘法减小”', 11, 'start', INK2)
