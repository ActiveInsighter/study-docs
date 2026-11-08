LABEL = 'Cache 每行的结构：1 + 1 + 19 + 64×8 = 533 bit'
F = Fig(760, 380, 'Cache 每行：1 + 1 + 19 + 64×8 = 533 bit')
rows = [['有效位(1)', '脏位(1)', '标记(19)', '数据(64B)']]
V = {1: ['1', '0', '1…1101'], 3: ['1', '1', '0…0000']}
for i in range(8): rows.append(V.get(i, ['0', '0'] + ['−'] * 1) + [''])
W = [90] * 3 + [150]
W[-2] = 120
tones = {(r, c): 'red' for r in (2,) for c in range(4)}
F.table(150, 64, rows, W, 32, size=12.5, mono_cols=range(len(W) - 1), tones=tones)
for i in range(8): F.text(150 + sum(W) + 12, 64 + 32 * (i + 1) + 16, str(i), 11.5, 'start', MUTED, mono=True, valign='middle')
F.text(140, 144, 'Cache 行 →', 12.5, 'end', ACCENT['red'], valign='middle')
F.text(380, 364, 'Cache 数据部分共 8 × 64 B = 512 B；有效位、脏位、计数位、标记是额外开销', 12, color=MUTED)
