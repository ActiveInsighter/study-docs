LABEL = 'KMP 算法：失配时主串指针 i 不回溯，模式串指针 j 按 next 数组回退'
F = Fig(860, 340, 'KMP：主串指针不回溯，模式串按 next 回退')
F.text(70, 96, '主串 S', 13, 'end', INK2, 600, valign='middle')
F.cells(84, 80, ['?'] * 15, 40, 32, {i: 'dark' for i in range(6)}, size=13, index=1)
F.text(70, 162, '模式串 T', 13, 'end', INK2, 600, valign='middle')
F.cells(84, 146, list('abaabc'), 40, 32, {i: 'blue' for i in range(6)}, size=14, index=1)
F.text(70, 228, 'next', 13, 'end', INK2, 600, valign='middle', mono=True)
F.cells(84, 212, ['', '0', '1', '1', '2', '2', '3'][1:], 40, 32, size=14)
x = 380
F.text(x, 210, '模式串 T = "abaabc"：', 13, 'start', INK, 600)
msgs = [('6', 'j = 3'), ('5', 'j = 2'), ('4', 'j = 2'), ('3', 'j = 1'), ('2', 'j = 1')]
for k, (p, j) in enumerate(msgs):
    F.text(x, 234 + k * 18, f'第 {p} 个元素匹配失败：i 不变，令 {j}', 12, 'start', INK2)
F.text(x, 234 + 5 * 18, '第 1 个元素匹配失败：j = 0，然后 i++、j++', 12, 'start', ACCENT['green'])
F.text(84, 290, 'next[j] = 失配时 j 应回退到的位置', 12.5, 'start', MUTED)
