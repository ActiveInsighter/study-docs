LABEL = '802.1Q 帧：在以太网 MAC 帧的源地址后插入 4 字节 VLAN 标记'
F = Fig(700, 300, '802.1Q 帧（插入 VLAN 标记）')
F.text(300, 62, '以太网的 MAC 帧（max：1518 字节）', 12, color=INK, weight=600)
from common import frame
frame(F, 100, 74, [('目的地址', 90, 'white', None), ('源地址', 90, 'white', None), ('类型', 70, 'white', None), ('数据载荷', 110, 'white', None), ('FCS', 70, 'white', None)], 30)
for x, t in ((145, '6'), (235, '6'), (305, '2'), (395, '46~1500'), (485, '4')): F.text(x, 120, t, 11, color=INK2, mono=True)
F.text(330, 160, '插入 VLAN 标记后的 802.1Q 帧（max：1522 字节）', 12, color=INK, weight=600)
frame(F, 100, 172, [('目的地址', 90, 'white', None), ('源地址', 90, 'white', None), ('VLAN 标记', 70, 'amber', None), ('类型', 70, 'white', None), ('数据载荷', 110, 'white', None), ('FCS', 70, 'white', None)], 30)
for x, t in ((145, '6'), (235, '6'), (315, '4'), (375, '2'), (465, '46~1500'), (555, '4')): F.text(x, 218, t, 11, color=ACCENT['red'] if t == '4' and x == 315 else INK2, mono=True)
F.curve(60, 100, 96, 186, 0.3, ACCENT['blue'], 2.4); F.text(16, 224, '插入 4 字节\nVLAN 标记', 11, 'start', TONES['amber'][2], lh=1.3)
F.text(350, 256, 'VLAN 标记的前两个字节表明是 IEEE 802.1Q 帧，接下来 4 位没用，', 12, color=INK2)
F.text(350, 278, '后面 12 位是 VLAN 标识符 VID，唯一表示该以太网帧属于哪个 VLAN', 12, color=ACCENT['red'])
