LABEL = '超流水：把一个时钟周期再细分，流水段更多'
F = Fig(420, 330, '2. 超流水技术')
F.cells(80, 56, ['IF', 'ID', 'EX', 'WR'], 50, 24, {2: 'blue'}, size=11.5, mono=False)
F.text(400, 300, '每个流水段只占半个时钟周期', 11, 'end', MUTED)
for i in range(9):
    y = 96 + i * 18
    F.cells(30 + i * 25, y, ['', '', '', ''], 25, 18, {2: 'blue'})
F.line(30, 280, 400, 280, INK2, 1.3, arrow='end'); F.line(30, 280, 30, 84, INK2, 1.3, arrow='end')
for i in range(7): F.text(30 + i * 50, 298, str(i), 11, color=INK2, mono=True)
