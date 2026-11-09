LABEL = '记忆 ⌈m/2⌉−1：满结点分裂后每个结点至少剩 ⌈m/2⌉−1 个关键字'
F = Fig(760, 380, '为什么下限是 ⌈m/2⌉ − 1：看分裂')
def row(y, m):
    F.text(60, y + 14, f'{m} 叉', 15, 'end', INK, 700, valign='middle')
    F.cells(76, y, ['']*m, 22, 28, {i: 'blue' for i in range(m)}, size=11)
    F.text(76 + m * 22 + 8, y + 14, f'溢出：{m} 个关键字', 12, 'start', MUTED, valign='middle')
    k = -(-m // 2)
    F.line(348, y + 14, 390, y + 14, LINE, 1.5, arrow='end')
    F.cells(470, y - 22, [''], 22, 22, {0: 'red'})
    F.cells(400, y + 18, [''] * (k - 1), 22, 22, {i: 'blue' for i in range(k - 1)})
    F.cells(560 - 22 * (m - k), y + 18, [''] * (m - k), 22, 22, {i: 'blue' for i in range(m - k)})
    F.line(474, y, 410, y + 16, INK2, 1.2); F.line(488, y, 548, y + 16, INK2, 1.2)
    F.text(600, y + 14, f'⌈{m}/2⌉ − 1 = {k - 1}', 14, 'start', ACCENT['red'], 600, mono=True, valign='middle')
for i, m in enumerate((5, 6, 7)):
    row(92 + i * 96, m)
F.text(380, 362, 'm 叉树插满后有 m 个关键字，从第 ⌈m/2⌉ 个处分裂，左边剩 ⌈m/2⌉ − 1 个', 12.5, color=MUTED)
