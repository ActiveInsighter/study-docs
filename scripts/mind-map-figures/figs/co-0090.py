LABEL = '直接映射 Cache 的电路：行号直接定位，标记比较决定是否命中'
F = Fig(760, 400)
F.box(80, 70, 140, 32, '标记', 'blue', 13, 0); F.box(220, 70, 80, 32, '行号', 'amber', 13, 0); F.box(300, 70, 160, 32, '块内地址', 'gray', 13, 0)
F.text(150, 62, 't bit', 11.5, color=MUTED); F.text(260, 62, 'c bit', 11.5, color=MUTED); F.text(380, 62, 'b bit', 11.5, color=MUTED); F.brace(80, 300, 50, 'm bit（主存块号）', down=False)
for i, lab in enumerate(('标记', '标记', '…', '标记')):
    y = 200 + i * 28
    F.box(110, y, 70, 28, lab, 'blue' if lab != '…' else 'light', 12, 0); F.box(180, y, 160, 28, '', 'red' if i == 1 else 'white', rx=0)
F.text(260, 188, 'Cache 存储体', 11.5, color=MUTED)
F.ellipse(150, 154, 32, 16, '比较', 'white', 12)
F.line(150, 104, 150, 136, INK2, 1.3, arrow='end'); F.line(150, 198, 150, 172, INK2, 1.3, arrow='end')
F.poly([(260, 104), (260, 130), (400, 130), (400, 242), (342, 242)], ACCENT['amber'], 1.3, arrow='end'); F.text(408, 160, '行号直接选中一行', 11.5, 'start', ACCENT['amber'])
F.text(108, 150, '相等', 11.5, 'end', ACCENT['green']); F.text(196, 140, '不等', 11.5, 'start', ACCENT['red'])
F.poly([(118, 154), (90, 154), (90, 330), (180, 330)], ACCENT['green'], 1.3, arrow='end'); F.text(90, 342, 'Cache 命中', 11.5, 'start', ACCENT['green'])
F.circle(196, 330, 10, '×', 'white', 12)
F.line(196, 312, 196, 320, INK2, 1.2); F.line(196, 340, 196, 368, INK2, 1.3, arrow='end'); F.text(204, 360, 'Cache 读出', 11.5, 'start', INK2)
F.poly([(182, 154), (520, 154), (520, 116), (462, 116), (462, 86)], ACCENT['red'], 1.3, arrow='end'); F.text(530, 150, '缺失 → 访问主存', 11.5, 'start', ACCENT['red'])
F.box(590, 180, 90, 60, '主存', 'green', 13, 4); F.poly([(462, 86), (635, 86), (635, 178)], INK2, 1.3, arrow='end')
F.line(635, 242, 635, 368, INK2, 1.3, arrow='end'); F.text(644, 330, '主存读出', 11.5, 'start', INK2)
F.rect(60, 372, 660, 16, '#e3f4e8', ACCENT['green'], 1.2, 8); F.text(390, 380, '数据总线', 11, color=TONES['green'][2], valign='middle')
