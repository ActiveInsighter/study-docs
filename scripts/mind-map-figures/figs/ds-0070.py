from common import heap_tree
LABEL = '堆排序：输出堆顶后把最后一个元素换到堆顶并向下调整'
F = Fig(660, 520, '堆排序：输出堆顶 → 调整成新堆')
steps = [('大根堆', [87,45,78,32,17,65,53,9], {1: 'red'}),
         ('87 与 09 交换并断开', [9,45,78,32,17,65,53], {1: 'red'}),
         ('09 与较大孩子 78 交换', [78,45,9,32,17,65,53], {3: 'red'}),
         ('09 与 65 交换，新堆', [78,45,65,32,17,9,53], {6: 'red'})]
for k, (cap, arr, t) in enumerate(steps):
    cx, cy = 20 + (k % 2) * 320, 96 + (k // 2) * 216
    heap_tree(F, cx, cy, ['%02d' % v for v in arr], unit=32, levelh=46, r=14, tones=t, size=11)
    F.text(cx + 144, cy + 168, cap, 12.5, color=INK2)
F.text(630, 60, '已输出：87', 12.5, 'end', ACCENT['green'], 600)
