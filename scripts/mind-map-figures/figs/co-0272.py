from common import gate
LABEL = '异或与同或'
F = Fig(560, 350, '异或 vs 同或')
for k, (name, expr, ys, g, lab) in enumerate((('异或', 'Y = A ⊕ B', '0110', 'xor', '=1'), ('同或', 'Y = A ⊙ B', '1001', 'xnor', '='))):
    x = 40 + k * 260
    F.text(x + 90, 76, name, 15, color=INK, weight=700); F.text(x + 90, 102, expr, 14, color=INK2, mono=True)
    rows = [['A', 'B', 'Y']] + [[a[0], a[1], y] for a, y in zip(('00', '01', '10', '11'), ys)]
    F.table(x + 30, 118, rows, [40, 40, 40], 28, size=13, mono_cols=(0, 1, 2), head_tone='blue', tones={(r, 2): 'green' for r in range(1, 5)})
    ins, out = gate(F, x + 72, 268, g, label=lab)
    for p in ins: F.line(p[0] - 18, p[1], p[0], p[1], INK2, 1.3)
    F.line(out[0], out[1], out[0] + 18, out[1], INK2, 1.3)
F.text(280, 338, '同或 = 异或取反；异或是天然的“加法”“奇偶校验”', 12.5, color=MUTED)
