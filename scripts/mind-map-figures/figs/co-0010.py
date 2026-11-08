LABEL = '存储器的简单模型：n 根地址线经译码器产生 2^n 根选通线'
F = Fig(560, 330, '存储器的简单模型：2^{n} 根选通线')
F.box(110, 110, 70, 140, '译\n码\n器', 'red', 16, 6)
for i, y in enumerate((130, 150, 230)):
    F.line(50, y, 108, y, INK2, 1.4)
F.text(44, 130, 'A_{0}', 13, 'end', INK, valign='middle'); F.text(80, 190, '⋮', 16, color=MUTED, valign='middle'); F.text(44, 230, 'A_{n−1}', 13, 'end', INK, valign='middle')
cells = [('0 号存储单元', 90), ('1 号存储单元', 150), ('2^{n} − 1 号存储单元', 270)]
for lab, y in cells:
    F.box(300, y - 20, 200, 40, lab, 'white', 14, 4)
    F.poly([(180, min(max(y, 120), 240)), (240, min(max(y, 120), 240)), (240, y), (298, y)], INK2, 1.4, arrow='end')
F.text(400, 214, '⋮', 18, color=MUTED, valign='middle')
F.text(280, 316, '一根选通线选中一个存储单元：n 位地址 → 2^{n} 个单元', 12, color=MUTED)
