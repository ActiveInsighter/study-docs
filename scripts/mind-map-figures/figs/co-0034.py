LABEL = '存储芯片的基本原理：MAR、译码器、存储矩阵、MDR、控制电路'
F = Fig(800, 380, '存储芯片的基本原理')
F.rect(260, 100, 500, 210, '#f4f4f5', '#a1a1aa', 1.2, 8); F.text(510, 206, '存储矩阵：2^{n} 个存储单元 × 存储字长', 13, color=INK2, valign='middle')
for r in range(4):
    F.line(240, 124 + r * 50, 760, 124 + r * 50, ACCENT['red'], 1)
F.box(170, 110, 60, 190, '译\n码\n器', 'red', 13, 5)
F.box(110, 160, 40, 110, 'M\nA\nR', 'violet', 12, 4)
F.line(150, 215, 168, 215, INK2, 1.3, arrow='end')
F.line(60, 215, 108, 215, INK2, 1.6, arrow='end'); F.text(54, 215, '地址总线\n（n 位）', 11.5, 'end', INK2, valign='middle')
F.cells(280, 60, list('10100011'), 58, 26, {i: 'green' for i in range(8)}, size=12); F.text(278, 73, 'MDR', 12, 'end', ACCENT['green'], 700, valign='middle')
F.line(510, 58, 510, 36, INK2, 1.6, arrow='both'); F.text(520, 40, '数据总线（宽度 = 存储字长）', 11.5, 'start', INK2)
F.box(110, 60, 70, 60, '控制\n电路', 'amber', 12, 5)
for i, (lab, y) in enumerate((('片选线 CS / CE', 70), ('读控制线 RD / OE', 90), ('写控制线 WE', 110))):
    F.line(30, y, 108, y, INK2, 1.2, arrow='end'); F.text(26, y, lab, 11, 'end', INK2, valign='middle') if False else F.text(34, y - 6, lab, 10.5, 'start', MUTED)
F.text(400, 340, '控制电路：MAR、MDR、译码器电平稳定后才进行下一步；CS 低电平时芯片工作；只有 WE 时“低写高读”', 12, color=MUTED)
F.text(400, 362, '总容量 = 存储单元个数 × 存储字长', 12, color=INK2)
