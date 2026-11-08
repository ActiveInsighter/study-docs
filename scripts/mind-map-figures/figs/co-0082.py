LABEL = '固态硬盘：闪存翻译层 + 多个闪存芯片（块由页组成）'
F = Fig(800, 392)
F.line(120, 52, 680, 52, INK, 5); F.text(130, 42, 'I/O 总线', 12, 'start', INK2)
F.rect(24, 72, 752, 296, 'none', INK2, 1.3, 16, dash='6 4'); F.text(40, 94, '固态硬盘 SSD', 13, 'start', INK, 700)
F.line(400, 54, 400, 100, INK, 3, arrow='end'); F.text(410, 80, '系统要读写的逻辑块号', 11.5, 'start', INK2)
F.box(300, 102, 200, 32, '闪存翻译层', 'violet', 13, 4)
F.line(400, 136, 400, 160, INK2, 1.2, arrow='both'); F.text(410, 152, '把逻辑块号映射为物理地址', 11.5, 'start', INK2)
F.rect(44, 166, 712, 190, '#fdf1d8', ACCENT['amber'], 1.2, 8)
for c in range(4):
    x = 56 + c * 176
    F.rect(x, 176, 164, 160, '#fde7e4', ACCENT['red'], 1.1, 6)
    for r, b in enumerate(('块0', '块1', '⋮', '块m')):
        y = 186 + r * 34
        if b == '⋮':
            F.text(x + 82, y + 12, '⋮', 13, color=MUTED, valign='middle'); continue
        F.rect(x + 8, y, 118, 26, '#e8effc', ACCENT['blue'], 1, 4)
        for j, p in enumerate(('页0', '页1', '…', '页n')):
            F.text(x + 24 + j * 28, y + 13, p, 10, color=TONES['blue'][2], valign='middle')
        F.text(x + 132, y + 13, b, 10, 'start', ACCENT['red'], valign='middle')
    F.text(x + 82, 330, f'闪存芯片 {c + 1}', 11, color=TONES['red'][2])
F.text(400, 384, '读写以页为单位；擦除以块为单位：写入前要先擦除整块', 11.5, color=MUTED)
