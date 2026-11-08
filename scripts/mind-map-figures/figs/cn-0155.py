LABEL = 'CSMA/CA：DIFS、RTS、SIFS、CTS、DATA、ACK 的时序，其他站推迟访问'
F = Fig(640, 450, 'CSMA/CA 的工作过程')
xs = {'源': 80, '目的地': 300, '其他结点 1': 440, '其他结点 2': 560}
for k, x in xs.items(): F.text(x, 60, k, 12, color=INK, weight=600); F.line(x, 76, x, 430, INK2, 1.3, arrow='end')
def msg(y, lab, a='源', b='目的地', also=False, tone='green'):
    F.line(xs[a], y, xs[b], y + 30, INK2, 1.2, arrow='end'); F.pill((xs[a] + xs[b]) / 2 - 16, y + 4, lab, tone, 10)
    if also: F.line(xs[a], y, xs['其他结点 2'], y + 40, INK2, 1, dash='4 3', arrow='end'); F.pill(xs['其他结点 1'] - 16, y + 22, lab, 'blue', 10)
F.vbrace(74, 80, 104, 'DIFS', right=False, size=11)
msg(106, 'RTS')
F.vbrace(306, 140, 164, 'SIFS', size=11)
msg(166, 'CTS', '目的地', '源', also=True)
F.vbrace(74, 200, 224, 'SIFS', right=False, size=11)
msg(226, 'DATA')
F.vbrace(306, 264, 288, 'SIFS', size=11)
msg(290, 'ACK', '目的地', '源', also=True)
F.rect(400, 200, 200, 130, 'amber', 'none', 0, 4, opacity=0.6); F.text(500, 260, '推迟访问\n（时间由 CTS 告知）', 12, color=TONES['amber'][2], weight=600, lh=1.4, valign='middle')
F.text(170, 380, 'DIFS：128 ms　SIFS：28 ms', 12.5, color=ACCENT['red'], weight=600)
F.text(170, 410, '若没收到 CTS / ACK，进行冻结退避', 12, color=ACCENT['green'])
