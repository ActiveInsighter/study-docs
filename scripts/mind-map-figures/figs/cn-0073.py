LABEL = '选择重传中 WT + WR ≤ 2^n 的原因：n = 3、WT = 6、WR = 3 时会出现误解'
F = Fig(560, 270, '例：n = 3，W_{T} = 6，W_{R} = 3')
seq = ['0', '1', '2', '3', '4', '5', '6', '7', '0', '1', '2']
def row(y, lo, hi, mark=None):
    for i, s in enumerate(seq): F.text(50 + i * 44, y, s, 14, color=INK, mono=True, valign='middle')
    F.rect(30 + lo * 44, y - 18, (hi - lo) * 44, 36, 'none', INK, 1.6, 3)
    if mark is not None: F.circle(50 + mark * 44, y, 13, '', 'red', sw=1.2); F.text(50 + mark * 44, y, '0', 13, color=TONES['red'][2], mono=True, valign='middle')
row(70, 0, 6)
F.text(30, 116, '① 接收到了全部 ACK，发送窗口移动 3 位', 12, 'start', INK2)
row(146, 3, 9, 8)
F.text(30, 192, '② 全部 ACK 都丢了，重发 0', 12, 'start', INK2); F.pill(390, 182, '接收方无法区分：出现误解', 'red', 11)
row(226, 0, 6, 0)
