from common import spacetime
LABEL = '流水线时空图：k 段流水线完成 n 个任务共需 (k + n − 1)Δt'
F = Fig(620, 330, '流水线的性能指标')
fills = {}
for s in range(4):
    for i, l in enumerate(['1', '2', '3', '4', '…', '…', 'n−1', 'n']):
        fills[(s, s + i)] = l
spacetime(F, 100, 240, 4, 11, 42, 34, fills, ['取指令', '译码', '执行', '存结果'], tone=lambda r, c, t: 'violet' if c == r else 'white')
F.line(100, 262, 268, 262, INK2, 1.2, arrow='both'); F.text(184, 276, 'kΔt', 12, color=INK2, mono=True)
F.line(268, 262, 562, 262, INK2, 1.2, arrow='both'); F.text(415, 276, '(n − 1)Δt', 12, color=INK2, mono=True)
F.line(100, 296, 562, 296, INK2, 1.2, arrow='both'); F.text(331, 312, '(k + n − 1)Δt', 12, color=INK2, mono=True)
F.brace(226, 268, 96, 'Δt', down=False)
