LABEL = '运算器中乘除法用到的寄存器：ACC、MQ、X'
F = Fig(380, 380, '运算器')
F.rect(30, 64, 320, 296, 'none', ACCENT['blue'], 1.6, 12)
F.box(60, 92, 110, 52, 'ACC', 'blue', 18, 6, True); F.box(220, 92, 110, 52, 'MQ', 'blue', 18, 6, True)
F.line(170, 110, 218, 110, INK2, 1.4, arrow='end'); F.line(218, 126, 170, 126, INK2, 1.4, arrow='end')
F.box(60, 200, 110, 52, 'ALU', 'red', 18, 6, True)
F.line(100, 198, 100, 146, INK2, 1.4, arrow='end'); F.line(130, 146, 130, 198, INK2, 1.4, arrow='end')
F.box(60, 296, 110, 46, 'X', 'white', 18, 6, True); F.line(115, 294, 115, 254, INK2, 1.4, arrow='end')
F.text(275, 220, 'ACC：累加器\n（乘积高位 / 余数）\nMQ：乘商寄存器\nX：被乘数 / 除数', 12, 'middle', INK2, lh=1.5)
