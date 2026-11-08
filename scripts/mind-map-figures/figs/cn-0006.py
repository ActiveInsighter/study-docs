from common import wave_digital, encode
LABEL = '差分曼彻斯特编码'
F = Fig(600, 100)
bits = [1, 0, 0, 1, 1, 0, 1, 0]
F.text(130, 56, '差分曼彻斯特', 12, 'end', INK2, valign='middle')
for i in range(9): F.line(140 + i * 56, 26, 140 + i * 56, 80, LINE, 0.8, dash='3 4')
wave_digital(F, 140, 70, encode(bits, 'dman'), 56, 30, ACCENT['blue'])
for i, b in enumerate(bits): F.text(168 + i * 56, 92, str(b), 10.5, color=MUTED, mono=True)
