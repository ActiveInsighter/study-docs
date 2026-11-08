from common import spacetime
LABEL = '时空图：四段流水线执行 5 条指令'
F = Fig(560, 280, '时空图（4 段流水线）')
fills = {}
for i in range(5):
    for s in range(4):
        fills[(s, i + s)] = f'I_{{{i + 1}}}'
spacetime(F, 90, 230, 4, 8, 50, 34, fills, ['取指令', '译码', '执行', '存结果'], tone=lambda r, c, t: 'violet' if t == 'I_{1}' else ('amber' if t == 'I_{5}' else 'white'))
for i in range(6): F.text(90 + i * 50, 252, f't_{{{i}}}', 11.5, color=INK2)
