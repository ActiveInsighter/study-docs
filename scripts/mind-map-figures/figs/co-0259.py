LABEL = '超标量：每个时钟周期同时发射多条指令'
F = Fig(420, 330, '1. 超标量技术')
F.cells(80, 56, ['IF', 'ID', 'EX', 'WR'], 50, 24, {2: 'blue'}, size=11.5, mono=False)
for i in range(9):
    g = i // 3
    y = 96 + i * 18
    F.cells(30 + g * 50, y, ['', '', '', ''], 50, 18, {2: 'blue'})
F.line(30, 280, 400, 280, INK2, 1.3, arrow='end'); F.line(30, 280, 30, 84, INK2, 1.3, arrow='end')
for i in range(7): F.text(30 + i * 50, 298, str(i), 11, color=INK2, mono=True)
