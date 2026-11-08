from common import disk_grid
LABEL = '连续分配：目录记录文件的起始块号和长度'
F = Fig(620, 380, '连续分配')
hl = {}
for f, (s, l, t) in {'count': (0, 2, 'teal'), 'tr': (14, 3, 'blue'), 'mail': (19, 6, 'violet'), 'list': (28, 4, 'amber'), 'f': (6, 2, 'red')}.items():
    for b in range(s, s + l): hl[b] = (t, '')
cs = disk_grid(F, 20, 50, hl=hl, dy=38)
for f, b in (('count', 0), ('tr', 14), ('mail', 19), ('list', 28), ('f', 6)): F.text(cs[b][0], cs[b][1] - 13, f, 10, color=INK2)
F.text(480, 76, '目录', 12, color=INK2)
F.table(380, 86, [['file', 'start', 'length'], ['count', '0', '2'], ['tr', '14', '3'], ['mail', '19', '6'], ['list', '28', '4'], ['f', '6', '2']], [70, 60, 70], 28, size=12, head_tone='gray', tones={(1, i): 'teal' for i in range(3)} | {(2, i): 'blue' for i in range(3)} | {(3, i): 'violet' for i in range(3)} | {(4, i): 'amber' for i in range(3)} | {(5, i): 'red' for i in range(3)}, zebra=False)
