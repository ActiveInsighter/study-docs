LABEL = '控制冲突：转移指令改变 PC，已进入流水线的后续指令作废'
F = Fig(910, 330, '控制冲突（转移导致断流）')
from common import wave_clock
F.text(80, 92, 'CLK', 12, 'end', INK, valign='middle', mono=True); wave_clock(F, 90, 104, 8, 80)
for i in range(8): F.text(130 + i * 80, 60, f'Cycle {i + 4}', 10.5, color=MUTED)
stg = ['IFetch', 'Reg/Dec', 'Exec', 'Mem', 'WR']
rows = [('12: Beq', 0, False), ('16: R-type', 1, True), ('20: R-type', 2, True), ('24: R-type', 3, True), ('1000: Target of Br', 4, False)]
for r, (name, st, gone) in enumerate(rows):
    y = 130 + r * 36
    F.text(160 + st * 80 - 4 if st else 86, y + 13, name, 11, 'end', INK2, valign='middle')
    for i, s in enumerate(stg):
        x = 170 + (st + i) * 80 - 80 + (0 if st else 80)
        x = 90 + (st + i) * 80 + (80 if st == 4 else 0)
        dead = gone and (st + i) < 4
        F.box(x, y, 80, 26, s, 'light' if dead else 'white', 11, 0)
F.rect(90 + 80, 160, 320, 104, 'violet', ACCENT['violet'], 1, 4, opacity=0.35)
F.line(90 + 4 * 80, 156, 90 + 4 * 80 + 80, 274, ACCENT['red'], 1.6, arrow='end')
F.text(420, 318, 'Beq 在 Mem 段才确定转移：其后已取入的 3 条指令作废（紫色区域）', 11.5, color=MUTED)
