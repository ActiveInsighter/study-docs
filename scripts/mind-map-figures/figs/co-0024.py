from common import instr, memcol
LABEL = '间接寻址：EA = (A)，可多次间接'
F = Fig(760, 300, '间接寻址：EA = (A)')
for k, x in enumerate((30, 400)):
    c = instr(F, x, 80, 'LDA' if k == 0 else 'OP', '', 'A', (60, 50, 50), 28)
    if k == 0:
        memcol(F, x + 220, 90, ['', 'EA', '', '操作数', ''], 90, 28)
        F.poly([c, (c[0], 132), (x + 212, 132)], INK2, 1.2, arrow='end'); F.text(x + 206, 132, 'A', 12, 'end', INK, mono=True, valign='middle')
        F.poly([(x + 310, 132), (x + 330, 132), (x + 330, 170), (x + 190, 170), (x + 190, 188), (x + 212, 188)], INK2, 1.2, arrow='end'); F.text(x + 206, 202, 'EA', 12, 'end', INK, mono=True)
        F.text(x + 100, 250, '一次间接寻址', 12.5, color=INK2)
    else:
        memcol(F, x + 220, 90, ['', '1 | A₁', '', '0 | EA', '', '操作数'], 100, 28)
        F.poly([c, (c[0], 132), (x + 212, 132)], INK2, 1.2, arrow='end'); F.text(x + 206, 132, 'A', 12, 'end', INK, mono=True, valign='middle')
        F.poly([(x + 320, 132), (x + 336, 132), (x + 336, 170), (x + 190, 170), (x + 190, 188), (x + 212, 188)], INK2, 1.2, arrow='end'); F.text(x + 206, 202, 'A₁', 12, 'end', INK, mono=True)
        F.poly([(x + 320, 188), (x + 336, 188), (x + 336, 226), (x + 190, 226), (x + 190, 244), (x + 212, 244)], INK2, 1.2, arrow='end'); F.text(x + 206, 258, 'EA', 12, 'end', INK, mono=True)
        F.text(x + 100, 250, '两次间接寻址', 12.5, color=INK2)
F.text(380, 292, '首位为 1 表示还需继续间接；扩大寻址范围，但要多次访存', 12, color=MUTED)
