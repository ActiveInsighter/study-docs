LABEL = '十字链表（有向图）：顶点结点与弧结点'
F = Fig(860, 360, '十字链表（有向图）')
N = {'V1': (60, 120), 'V2': (170, 90), 'V3': (130, 200)}
F.graph(N, [('V1','V2'), ('V1','V3'), ('V2','V3'), ('V3','V1', '', {'shift': 5})], r=20, size=13)
F.text(110, 260, 'V1→V2, V1→V3, V2→V3, V3→V1', 12, color=MUTED, mono=True)
F.text(280, 74, '顶点结点', 12.5, 'start', MUTED); F.cells(350, 60, ['data', 'firstin', 'firstout'], 62, 22, size=11, mono=False)
F.text(560, 74, '弧结点', 12.5, 'start', MUTED); F.cells(610, 60, ['tail', 'head', 'hlink', 'tlink'], 52, 22, size=11, mono=False)
F.text(610, 100, 'hlink：同弧头的下一条弧　tlink：同弧尾的下一条弧', 11, 'start', MUTED)
arcs = {0: [('0', '1'), ('0', '2')], 1: [('1', '2')], 2: [('2', '0')]}
from common import record
for i, v in enumerate(['V1', 'V2', 'V3']):
    y = 140 + i * 66
    F.text(272, y + 13, str(i), 12, 'end', MUTED, mono=True, valign='middle')
    record(F, 280, y, [v, '●', '●'], 50, 26, {0: 'blue'}, size=12)
    x = 460
    for j, (t, h) in enumerate(arcs[i]):
        last = j == len(arcs[i]) - 1
        cs = record(F, x, y, [t, h, '●', '^' if last else '●'], 38, 26, {0: 'amber', 1: 'amber'}, size=12)
        if j == 0: F.line(280 + 125, y + 13, x - 2, y + 13, ACCENT['blue'], 1.3, arrow='end')
        else: F.line(px, y + 13, x - 2, y + 13, ACCENT['blue'], 1.3, arrow='end')
        px = cs[3][0]
        x += 190
F.legend(280, 344, [('blue', '出弧链（tlink，同尾）'), ('amber', '弧结点 ⟨tail, head⟩')])
F.text(840, 344, '入弧链 hlink 同理把同一弧头的弧串起来', 12, 'end', MUTED)
