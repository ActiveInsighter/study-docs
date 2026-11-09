LABEL = 'TCP 连接建立：三次握手'
F = Fig(680, 380, 'TCP 连接建立（三次握手）')
F.text(160, 60, '客户机 A', 12.5, color=INK, weight=600); F.text(520, 60, '服务器 B', 12.5, color=INK, weight=600)
L, R = 160, 520
for x in (L, R): F.line(x, 70, x, 360, INK2, 1)
for x, y, t in ((L, 90, 'CLOSED'), (L, 160, 'SYN-SENT'), (L, 270, 'ESTAB-\nLISHED'), (R, 90, 'CLOSED'), (R, 140, 'LISTEN'), (R, 220, 'SYN-RCVD'), (R, 300, 'ESTAB-\nLISHED')):
    F.box(x - 50, y - 18, 100, 36, t, 'white', 11.5, 0)
F.text(L - 60, 140, '主动打开', 11, 'end', INK2); F.text(R + 60, 120, '被动打开', 11, 'start', INK2)
F.line(L + 50, 160, R - 50, 220, ACCENT['blue'], 1.5, arrow='end'); F.text(340, 190, 'SYN = 1，seq = x', 11.5, color=ACCENT['blue'], valign='middle', chip=True)
F.line(R - 50, 222, L + 50, 252, ACCENT['green'], 1.5, arrow='end'); F.text(340, 237, 'SYN = 1，ACK = 1，seq = y，ack = x + 1', 11, color=ACCENT['green'], valign='middle', chip=True)
F.line(L + 50, 262, R - 50, 292, ACCENT['blue'], 1.5, arrow='end'); F.text(340, 277, 'ACK = 1，seq = x + 1，ack = y + 1', 11, color=ACCENT['blue'], valign='middle', chip=True)
F.text(240, 120, '无数据（SYN 不允许携带数据）', 10.5, color=ACCENT['green']); F.text(340, 308, '（第三次握手可以携带数据了）', 10.5, color=ACCENT['blue'])
F.line(270, 340, 410, 340, INK2, 1.2, arrow='both'); F.text(340, 332, '数据传送', 11, color=INK2, halo=True)
