LABEL = '分块（索引顺序）查找：块间有序、块内无序'
F = Fig(760, 262, '分块查找')
tones = ['blue', 'amber', 'red', 'violet']
idx = [('24', '1'), ('54', '7'), ('78', '10'), ('88', '13')]
F.text(232, 96, '索引表', 13, 'end', INK2, 600, valign='middle')
for i, (mx, st) in enumerate(idx):
    F.box(244 + i * 56, 66, 56, 28, mx, tones[i], 13, 0, True)
    F.box(244 + i * 56, 94, 56, 28, st, tones[i], 13, 0, True)
F.text(470, 80, '块内最大关键字', 12, 'start', MUTED, valign='middle'); F.text(470, 108, '块的起始地址', 12, 'start', MUTED, valign='middle')
vals = '24 21 6 11 8 22 32 31 54 72 61 78 88 83'.split()
blk = [0]*6 + [1]*3 + [2]*3 + [3]*2
F.text(56, 196, '查找表', 13, 'end', INK2, 600, valign='middle')
F.cells(66, 182, vals, 46, 30, {i: tones[b] for i, b in enumerate(blk)}, size=13, index=1)
for i, s in enumerate([0, 6, 9, 12]):
    F.line(272 + i * 56, 122, 66 + s * 46 + 23, 180, INK2, 1.2, arrow='end')
F.text(380, 248, '先在索引表中确定所在块（顺序或折半），再在块内顺序查找', 12.5, color=MUTED)
