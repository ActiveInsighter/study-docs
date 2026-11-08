from common import wave_digital, sine_path
LABEL = '调制：基带信号 → 2ASK、2FSK、2PSK'
F = Fig(780, 440, '数字数据 → 模拟信号的调制')
bits = [0, 1, 0, 0, 1, 1, 1, 0, 0]
X0, BW = 160, 66
for i, b in enumerate(bits): F.text(X0 + i * BW + BW / 2, 62, str(b), 13, color=INK, mono=True, weight=600)
for i in range(len(bits) + 1): F.line(X0 + i * BW, 70, X0 + i * BW, 420, LINE, 0.8, dash='3 4')
F.text(140, 110, '基带信号', 13, 'end', INK, 700, valign='middle')
wave_digital(F, X0, 126, [b for b in bits for _ in (0, 1)], BW, 34, INK)
for k, (name, lab) in enumerate((('调幅', '2ASK'), ('调频', '2FSK'), ('调相', '2PSK'))):
    y = 200 + k * 86
    F.text(100, y, name, 13, 'end', INK, 600, valign='middle'); F.text(140, y, lab, 13, 'end', INK2, mono=True, valign='middle')
    F.line(X0 - 6, y, X0 + len(bits) * BW + 20, y, INK2, 1.1, arrow='end')
    d = ''
    for i, b in enumerate(bits):
        x = X0 + i * BW
        if lab == '2ASK':
            seg = sine_path(x, y, BW, 4, 24) if b else f'M{x} {y}H{x + BW}'
        elif lab == '2FSK':
            seg = sine_path(x, y, BW, 4 if b else 1.5, 24)
        else:
            seg = sine_path(x, y, BW, 2, 24 if b else -24)
        F.path(seg, ACCENT['blue'], 1.4)
