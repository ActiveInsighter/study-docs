LABEL = '哈夫曼树的构造、编码、WPL 与压缩率'
F = Fig(860, 540, '哈夫曼树：构造 · 编码 · WPL · 压缩率')
F.text(40, 84, '① 字符频次', 14, 'start', INK, 700)
F.table(40, 98, [['字符', 'a', 'b', 'c', 'd', 'e', 'f'], ['频次', '7', '1', '1', '1', '1', '2'], ['编码', '1', '0000', '0001', '0010', '0011', '01']], [56] + [52] * 6, 30, mono_cols=range(1, 7), size=13)
t = ('13', [('6', [('4', [('2#1', ['b', 'c']), ('2#2', ['d', 'e'])]), 'f']), 'a'])
tones = {k: 'green' for k in 'abcdef'}
pos = F.tree(40, 240, t, unit=50, levelh=54, r=16, size=13, tones=tones)
for k, code in {'a': '1', 'f': '01', 'b': '0000', 'c': '0001', 'd': '0010', 'e': '0011'}.items():
    x, y = pos[k]
    F.text(x, y + 32, code, 11.5, color=ACCENT['violet'], mono=True)
F.text(330, 240, '左 0 右 1', 12.5, 'start', ACCENT['violet'])
x = 480
F.text(x, 84, '② 编码  abcaaadeaaaff', 14, 'start', INK, 700)
F.text(x, 110, '1 0000 0001 111 0010 0011 111 01 01', 13, 'start', ACCENT['violet'], mono=True)
F.text(x, 132, '共 27 bit；前缀码，解码时从根沿树走到叶', 12.5, 'start', MUTED)
F.text(x, 180, '③ WPL', 14, 'start', INK, 700)
F.text(x, 206, '(1+1+1+1)×4 + 2×2 + 7×1 = **27**', 14, 'start', INK2, mono=True)
F.text(x, 254, '④ 压缩率（char 占 8 bit）', 14, 'start', INK, 700)
F.text(x, 280, '27 ÷ (13 × 8) = 27 / 104 ≈ **26%**', 14, 'start', INK2, mono=True)
F.text(x, 328, '⑤ 定长编码对比', 14, 'start', INK, 700)
F.text(x, 354, '6 个字符需 ⌈log₂6⌉ = 3 bit', 14, 'start', INK2)
F.text(x, 378, '3 ÷ 8 = 37.5%，哈夫曼编码更省', 14, 'start', INK2)
