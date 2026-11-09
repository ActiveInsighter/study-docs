LABEL = 'TCP 连接释放：四次挥手，客户端最后等待 2MSL'
F = Fig(700, 440, 'TCP 连接释放（四次挥手）')
F.text(160, 56, '客户机 A', 12.5, color=INK, weight=600); F.text(540, 56, '服务器 B', 12.5, color=INK, weight=600)
L, R = 160, 540
for x in (L, R): F.line(x, 66, x, 420, INK2, 1)
for x, y, t in ((L, 90, 'ESTAB-\nLISHED'), (L, 160, 'FIN-WAIT-1'), (L, 250, 'FIN-WAIT-2'), (L, 330, 'TIME-WAIT'), (L, 400, 'CLOSED'),
                (R, 90, 'ESTAB-\nLISHED'), (R, 210, 'CLOSE-WAIT'), (R, 310, 'LAST-ACK'), (R, 380, 'CLOSED')):
    F.box(x - 50, y - 18, 100, 36, t, 'white', 11, 0)
F.text(L - 60, 140, '主动关闭', 11, 'end', INK2); F.text(R + 60, 260, '被动关闭', 11, 'start', INK2)
F.line(L + 50, 150, R - 50, 200, ACCENT['red'], 1.5, arrow='end'); F.text(350, 160, 'FIN = 1，seq = u', 11.5, color=ACCENT['red'], halo=True)
F.line(R - 50, 216, L + 50, 244, ACCENT['green'], 1.5, arrow='end'); F.text(350, 214, 'ACK = 1，seq = v，ack = u + 1', 11, color=ACCENT['green'], halo=True)
F.line(R - 60, 270, L + 60, 280, INK2, 1.2, dash='4 3', arrow='end'); F.text(350, 268, '数据传送（半关闭：B 还可以发）', 11, color=INK2, halo=True)
F.line(R - 50, 300, L + 50, 320, ACCENT['red'], 1.5, arrow='end'); F.text(350, 297, 'FIN = 1，ACK = 1，seq = w，ack = u + 1', 11, color=ACCENT['red'], halo=True)
F.line(L + 50, 340, R - 50, 374, ACCENT['green'], 1.5, arrow='end'); F.text(350, 335, 'ACK = 1，seq = u + 1，ack = w + 1', 11, color=ACCENT['green'], halo=True)
F.vbrace(L - 56, 330, 400, '等待 2MSL', right=False, size=11)
F.text(20, 430, '等 2MSL：可收到 B 重传的 FIN 并再次确认；让本连接的旧报文段全部消失', 10.5, 'start', MUTED)
F.text(R + 60, 200, '通知应用\n进程', 11, 'start', INK2, lh=1.3)
