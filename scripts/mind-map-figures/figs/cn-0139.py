from common import sine_path
LABEL = '信道带宽：信道能通过的最高频率与最低频率之差'
F = Fig(640, 340, '信道带宽（以电话线为例）')
for k, (f, cyc, ok) in enumerate((('200 Hz', 2, False), ('300 Hz', 3, True), ('3300 Hz', 5, True), ('4000 Hz', 9, False))):
    y = 80 + k * 56
    F.text(80, y, f, 12, 'end', INK, valign='middle', mono=True)
    F.path(sine_path(90, y, 140, cyc, 12), ACCENT['blue'], 1.4); F.line(232, y, 244, y, INK2, 1.2, arrow='end')
    F.box(250, y - 12, 190, 24, '', 'gray', rx=12)
    if ok: F.path(sine_path(456, y, 80, cyc * 0.6, 12), ACCENT['blue'], 1.4); F.line(538, y, 548, y, INK2, 1.2, arrow='end')
    else: F.text(480, y, '✕', 22, color=ACCENT['red'], weight=700, valign='middle')
F.text(345, 300, '电话线', 11.5, color=INK2)
F.text(320, 328, '信道带宽 = 最高频率 − 最低频率，如 3300 Hz − 300 Hz = 3000 Hz', 12, color=INK2)
