from common import frame
LABEL = 'UDP 伪首部：源 IP、目的 IP、0、17、UDP 长度，仅用于计算校验和'
F = Fig(780, 330, 'UDP 伪首部（12 B，只参与校验和计算）')
frame(F, 120, 70, [('源 IP 地址', 130, 'amber', 4), ('目的 IP 地址', 130, 'amber', 4), ('0', 40, 'amber', 1), ('17', 40, 'amber', 1), ('UDP 长度', 90, 'amber', 2)], 30)
F.text(110, 85, '伪首部', 11, 'end', INK2, valign='middle')
frame(F, 120, 160, [('伪首部', 120, 'amber', 12), ('源端口', 80, 'green', 2), ('目的端口', 80, 'green', 2), ('长度', 80, 'green', 2), ('校验和', 80, 'green', 2)], 30)
F.line(120, 100, 120, 158, INK2, 1, dash='3 3'); F.line(550, 100, 240, 158, INK2, 1, dash='3 3')
F.text(110, 175, '字节', 11, 'end', MUTED, valign='middle')
F.box(240, 210, 80, 30, '首部', 'green', 12, 0); F.box(320, 210, 400, 30, '数据', 'blue', 12, 0); F.text(230, 225, 'UDP 用户数据报', 11, 'end', INK2, valign='middle')
F.box(200, 268, 100, 30, '首部', 'blue', 12, 0); F.box(300, 268, 420, 30, '数据', 'blue', 12, 0); F.text(190, 283, 'IP 数据报', 11, 'end', INK2, valign='middle')
F.line(520, 242, 520, 266, ACCENT['blue'], 2, arrow='end')
F.text(640, 52, '17：UDP 的协议号；伪首部不向下传送', 11, 'end', ACCENT['red'])
