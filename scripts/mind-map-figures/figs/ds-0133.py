LABEL = '三对角矩阵（带状矩阵）'
F = Fig(620, 390, '三对角矩阵（带状矩阵）')
rows = [['a₁,₁', 'a₁,₂', '0', '…', '0', '0'], ['a₂,₁', 'a₂,₂', 'a₂,₃', '…', '0', '0'], ['0', 'a₃,₂', 'a₃,₃', '…', '0', '0'],
        ['…', '…', '…', '…', '…', '…'], ['0', '0', '0', '…', 'aₙ₋₁,ₙ₋₁', 'aₙ₋₁,ₙ'], ['0', '0', '0', '…', 'aₙ,ₙ₋₁', 'aₙ,ₙ']]
F.items.append('<path d="M70 92 L130 76 L486 300 L470 340 L414 352 L58 128Z" fill="#e8effc" stroke="none" opacity="0.9"/>')
for r, row in enumerate(rows):
    for c, v in enumerate(row):
        x, y = 90 + c * 76, 96 + r * 46
        band = abs(r - c) <= 1 and v not in ('…',)
        F.text(x, y, v, 14, color=TONES['blue'][2] if band and v != '0' else MUTED, weight=600 if band and v != '0' else 400, valign='middle')
F.path('M52 76 q-10 0 -10 10 V340 q0 10 10 10', INK2, 1.5); F.path('M528 76 q10 0 10 10 V340 q0 10 -10 10', INK2, 1.5)
F.text(310, 378, '|i − j| > 1 时 a_{i,j} = 0；按行存入数组共 3n − 2 个元素，a_{i,j} 的下标 k = 2i + j − 3（从 0 起）', 12, color=INK2)
