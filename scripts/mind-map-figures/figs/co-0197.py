LABEL = 'Cache 每行的结构：1 + 1 + 1 + 20 + 64×8 = 535 bit'
F = Fig(760, 380, 'Cache 每行：1 + 1 + 1 + 20 + 64×8 = 535 bit')
rows = [['有效位(1)', '脏位(1)', '计数位(1)', '标记(20)', '数据(64B)']]
V = {2: ['1', '1', '1', '1…1111'], 3: ['1', '0', '0', '0…0000']}
for i in range(8): rows.append(V.get(i, ['0', '0'] + ['−'] * 2) + [''])
W = [90] * 4 + [150]
W[-2] = 120
tones = {(r, c): 'red' for r in (3,) for c in range(5)}
F.table(150, 64, rows, W, 32, size=12.5, mono_cols=range(len(W) - 1), tones=tones)
for i in range(8): F.text(150 + sum(W) + 12, 64 + 32 * (i + 1) + 16, str(i), 11.5, 'start', MUTED, mono=True, valign='middle')
F.text(140, 176, 'Cache 行 →', 12.5, 'end', ACCENT['red'], valign='middle')
F.text(380, 364, 'Cache 数据部分共 8 × 64 B = 512 B；有效位、脏位、计数位、标记是额外开销', 12, color=MUTED)
