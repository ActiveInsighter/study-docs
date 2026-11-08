LABEL = 'UDP 首部格式：源端口、目的端口、长度、校验和，共 8 字节'
F = Fig(560, 240, 'UDP 首部格式（8 B）')
F.text(40, 62, '0', 11, 'start', MUTED, mono=True); F.text(260, 62, '15 16', 11, color=MUTED, mono=True); F.text(480, 62, '31', 11, 'end', MUTED, mono=True)
F.box(40, 70, 220, 36, '16 位源端口号', 'white', 12, 0, align='start'); F.box(260, 70, 220, 36, '16 位目的端口号', 'white', 12, 0, align='start')
F.box(40, 106, 220, 36, '16 位 UDP 长度', 'white', 12, 0, align='start'); F.box(260, 106, 220, 36, '16 位 UDP 校验和', 'white', 12, 0, align='start')
F.box(40, 142, 440, 60, '数据（如果有）', 'blue', 13, 0)
F.vbrace(486, 70, 142, '8 B')
F.pill(170, 76, '可以不用，填 0', 'green', 9.5); F.pill(420, 76, '一定要', 'red', 9.5); F.pill(168, 112, '首部 + 数据', 'red', 9.5); F.pill(410, 112, '可以不用，填 0', 'green', 9.5)
