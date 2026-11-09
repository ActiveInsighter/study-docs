from common import disk_grid
LABEL = '索引分配：每个文件有一个索引块，存放其所有盘块号'
F = Fig(640, 380, '索引分配')
data = [9, 16, 1, 10, 25]
hl = {b: ('violet', '') for b in data}; hl[19] = ('white', '')
_n0 = len(F.items)
cs = disk_grid(F, 20, 50, hl=hl, dy=38, label_chip=True)
F.circle(cs[19][0], cs[19][1], 14, '', 'none', sw=1.2); F.items[-1] = F.items[-1].replace('stroke="none"', f'stroke="{INK2}"')
_n1 = len(F.items)
for b in data: F.line(cs[19][0] - 10, cs[19][1], cs[b][0] + 10, cs[b][1], LINE, 1, arrow='end')
_ln = F.items[_n1:]; del F.items[_n1:]; F.items[_n0 + 1:_n0 + 1] = _ln  # pointers run underneath blocks and numbers
F.text(510, 64, '目录', 12, color=INK2)
F.table(420, 72, [['file', 'index_block'], ['jeep', '19']], [80, 100], 28, size=12, head_tone='gray', tones={(1, 0): 'violet', (1, 1): 'violet'})
F.text(510, 160, '索引块 19', 12, color=INK2)
for i, v in enumerate(['9', '16', '1', '10', '25', '−1', '−1', '−1']): F.box(470, 170 + i * 22, 80, 22, v, 'violet' if v != '−1' else 'white', 11, 0, True)
F.line(cs[19][0] + 16, cs[19][1], 468, 200, INK2, 1.2, arrow='end'); F.line(560, 128, 560, 168, ACCENT['blue'], 1.2, arrow='end')
