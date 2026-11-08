from common import gate
LABEL = '与非、或非、异或：表达式、真值表与电路符号；反演律'
F = Fig(860, 420, '门电路与摩根定律（反演律）')
F.box(30, 60, 200, 70, '反演律\n¬(A+B) = ¬A · ¬B\n¬(A·B) = ¬A + ¬B', 'blue', 13, 10)
cols = [('与非', 'Y = ¬(A·B) = ¬A + ¬B', ['1', '1', '1', '0'], 'nand', '与：“屏蔽”'), ('或非', 'Y = ¬(A+B) = ¬A · ¬B', ['1', '0', '0', '0'], 'nor', ''), ('异或', 'Y = A ⊕ B', ['0', '1', '1', '0'], 'xor', '天然的“加法”“奇偶”')]
for k, (name, expr, ys, g, note) in enumerate(cols):
    x = 260 + k * 200
    F.text(x + 80, 80, name, 15, color=INK, weight=700)
    F.text(x + 80, 108, expr, 12.5, color=INK2, mono=True)
    rows = [['A', 'B', 'Y']] + [[a, b, y] for (a, b), y in zip(('00', '01', '10', '11'), ys)]
    F.table(x + 20, 130, rows, [40, 40, 40], 28, size=13, mono_cols=(0, 1, 2), head_tone='blue', tones={(r, 2): 'green' for r in range(1, 5)})
    ins, out = gate(F, x + 62, 290, g)
    for i, p in enumerate(ins):
        F.line(p[0] - 20, p[1], p[0], p[1], INK2, 1.3); F.text(p[0] - 24, p[1], 'AB'[i], 12, 'end', INK2, valign='middle')
    F.line(out[0], out[1], out[0] + 20, out[1], INK2, 1.3); F.text(out[0] + 24, out[1], 'Y', 12, 'start', INK2, valign='middle')
    if note: F.text(x + 80, 362, note, 12.5, color=ACCENT['blue'])
F.text(430, 400, '二进制加法 0+0=00，0+1=01，1+0=01，1+1=10：本位和正是 A ⊕ B', 12.5, color=MUTED)
