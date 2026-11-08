from common import wave_digital
LABEL = '二进制与四进制码元的波形对比'
F = Fig(640, 260, '二进制码元 vs 四进制码元')
F.text(120, 96, '二进制', 14, 'end', INK, 700, valign='middle')
b2 = [0, 1, 0, 0, 1, 1, 0, 1]
wave_digital(F, 140, 110, [b for b in b2 for _ in (0, 1)], 54, 30, ACCENT['blue'])
for i, b in enumerate(b2): F.text(167 + i * 54, 130, str(b), 12, color=ACCENT['violet'], mono=True)
F.text(120, 196, '四进制', 14, 'end', INK, 700, valign='middle')
b4 = [0, 1, 2, 3, 1, 2, 0, 3]
d = 'M140 230'
for i, v in enumerate(b4): d += f'V{230 - v * 14}H{140 + (i + 1) * 54}'
F.path(d, ACCENT['blue'], 1.8)
for i, v in enumerate(b4): F.text(167 + i * 54, 250, str(v), 12, color=ACCENT['violet'], mono=True)
F.text(320, 160, '四进制：每个码元携带 2 bit', 11, 'middle', MUTED)
