LABEL = '超长指令字：一条长指令包含多个并行操作'
F = Fig(420, 330, '3. 超长指令字')
F.cells(80, 56, ['IF', 'ID', 'EX', 'WR'], 50, 24, {2: 'blue'}, size=11.5, mono=False)
F.cells(180, 80, ['EX'], 50, 18, {0: 'blue'}, mono=False); F.cells(180, 98, ['EX'], 50, 18, {0: 'blue'}, mono=False)
for i in range(3):
    y = 130 + i * 50
    F.cells(30 + i * 50, y, ['', '', '', ''], 50, 18, {2: 'blue'})
    F.cells(130 + i * 50, y + 18, [''], 50, 18, {0: 'blue'}); F.cells(130 + i * 50, y + 36, [''], 50, 18, {0: 'blue'})
F.line(30, 280, 400, 280, INK2, 1.3, arrow='end'); F.line(30, 280, 30, 84, INK2, 1.3, arrow='end')
for i in range(7): F.text(30 + i * 50, 298, str(i), 11, color=INK2, mono=True)
