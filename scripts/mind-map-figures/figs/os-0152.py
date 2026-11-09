from common import disk_grid
LABEL = '隐式链接分配：每个盘块末尾存有指向下一个盘块的指针'
F = Fig(620, 380, '隐式链接分配')
chain = [9, 16, 1, 10, 25]
hl = {b: ('teal', str(chain[i + 1]) if i + 1 < len(chain) else '−1') for i, b in enumerate(chain)}
_n0 = len(F.items)
cs = disk_grid(F, 20, 50, hl=hl, dy=38, label_chip=True)
_n1 = len(F.items)
for a, b in zip(chain, chain[1:]): F.line(*cs[a], *cs[b], INK, 1.4, arrow='end', gap=10, gap2=12)
F.text(480, 76, '目录', 12, color=INK2)
F.table(380, 86, [['file', 'start', 'end'], ['jeep', '9', '25']], [70, 60, 70], 28, size=12, head_tone='gray', tones={(1, i): 'teal' for i in range(3)})
F.poly([(445, 144), (445, 196), (300, 196), (cs[9][0] + 14, cs[9][1])], LINE, 1, dash='3 3', arrow='end')
F.poly([(515, 144), (515, 342), (cs[25][0] + 14, cs[25][1])], LINE, 1, dash='3 3', arrow='end')
_ln = [i for i in F.items[_n1:] if i.startswith('<path')]; F.items[_n1:] = [i for i in F.items[_n1:] if not i.startswith('<path')]; F.items[_n0 + 1:_n0 + 1] = _ln
F.text(470, 370, '只能顺序访问；指针占用盘块空间', 11.5, color=MUTED)
