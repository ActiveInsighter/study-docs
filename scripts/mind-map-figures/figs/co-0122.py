from common import block
LABEL = '串行进位（行波进位）加法器：n 个全加器串接'
F = Fig(760, 260, '串行进位的并行加法器（行波进位）')
xs = [560, 380, 110]
labs = [('1', 'C_{0}', 'C_{1}'), ('2', 'C_{1}', 'C_{2}'), ('n', 'C_{n−1}', 'C_{n}')]
for x, (i, cin, cout) in zip(xs, labs):
    block(F, x, 100, 90, 54, 'FA', top=f'S_{{{i}}}', bottoms=(f'A_{{{i}}}', f'B_{{{i}}}'), L=30, size=15)
F.line(700, 127, 652, 127, ACCENT['violet'], 1.5, arrow='end'); F.text(706, 127, 'C_{0}', 13, 'start', INK, valign='middle')
F.line(558, 127, 472, 127, ACCENT['violet'], 1.5, arrow='end'); F.text(515, 116, 'C_{1}', 12, color=INK2)
F.line(378, 127, 320, 127, ACCENT['violet'], 1.5, arrow='end'); F.text(290, 127, '…', 16, color=MUTED, valign='middle')
F.line(258, 127, 202, 127, ACCENT['violet'], 1.5, arrow='end'); F.text(232, 116, 'C_{n−1}', 12, color=INK2)
F.line(108, 127, 60, 127, ACCENT['violet'], 1.5, arrow='end'); F.text(54, 127, 'C_{n}', 13, 'end', INK, valign='middle')
F.text(380, 244, '进位信号逐级形成：每一位都要等低位的进位，速度与串行加法器一样慢', 12.5, color=MUTED)
