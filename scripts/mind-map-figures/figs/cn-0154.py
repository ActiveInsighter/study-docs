LABEL = '电路交换、报文交换、分组交换的比较'
F = Fig(880, 470, '三种交换方式的比较')
for k, (title, x0) in enumerate((('电路交换', 120), ('报文交换', 380), ('分组交换', 640))):
    F.text(x0 + 90, 60, title, 13, color=INK, weight=700)
    for i, n in enumerate('ABCD'):
        x = x0 + i * 56
        F.line(x, 72, x, 360, INK2, 1.1); F.text(x, 376, n, 12, color=INK, weight=600)
    if k == 0:
        for i in range(3): F.line(x0 + i * 56, 90 + i * 14, x0 + (i + 1) * 56, 104 + i * 14, INK2, 1.1, arrow='end')
        F.line(x0 + 168, 132, x0, 150, INK2, 1.1, arrow='end')
        F.items.append(f'<path d="M{x0} 150L{x0 + 168} 170V250L{x0} 230Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.2"/>'); F.text(x0 + 84, 200, '报文', 12, color=TONES['red'][2])
        for i in range(3): F.line(x0 + i * 56, 260 + i * 14, x0 + (i + 1) * 56, 274 + i * 14, INK2, 1.1, arrow='end')
        F.vbrace(x0 - 6, 88, 148, '连接建立', right=False, size=11); F.vbrace(x0 - 6, 150, 250, '数据传送', right=False, size=11); F.vbrace(x0 - 6, 256, 310, '连接释放', right=False, size=11)
    elif k == 1:
        for i in range(3):
            F.items.append(f'<path d="M{x0 + i * 56} {90 + i * 80}L{x0 + (i + 1) * 56} {104 + i * 80}V{150 + i * 80}L{x0 + i * 56} {136 + i * 80}Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.2"/>'); F.text(x0 + i * 56 + 28, 120 + i * 80, '报文', 11, color=TONES['red'][2])
    else:
        for i in range(3):
            for p in range(4):
                y = 90 + p * 18 + i * 38
                F.items.append(f'<path d="M{x0 + i * 56} {y}L{x0 + (i + 1) * 56} {y + 8}V{y + 22}L{x0 + i * 56} {y + 14}Z" fill="#e8effc" stroke="#3b6fd4" stroke-width="1"/>')
                if i == 0: F.text(x0 - 8, y + 8, f'P{p + 1}', 10, 'end', INK2, valign='middle')
F.line(350, 80, 350, 330, INK2, 1.2, arrow='end'); F.text(358, 320, 't', 12, 'start', INK2)
F.rect(30, 396, 820, 62, 'none', INK2, 1.2, 6); F.text(70, 427, '数据传送\n的特点', 11, 'middle', INK2, lh=1.3, valign='middle')
F.line(130, 418, 250, 418, INK2, 2, arrow='end'); F.text(190, 410, '比特流直达终点', 10.5, color=INK2)
F.text(470, 427, '报文 · 存储转发', 11.5, color=INK2); F.text(730, 427, '分组 · 存储转发（可流水线）', 11.5, color=INK2)
