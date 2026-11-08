LABEL = '分段存储的地址变换：段号 2、偏移量 100 → 物理地址 8292'
F = Fig(640, 340, '分段的地址变换')
F.text(130, 86, '段表寄存器', 11.5, color=INK2); F.box(30, 94, 110, 26, '段表始址 F', 'white', 11, 0); F.box(140, 94, 100, 26, '段表长度 M', 'white', 11, 0)
F.circle(300, 107, 13, '>', 'white', 13); F.line(300, 94, 300, 60, INK2, 1.2, arrow='end'); F.text(300, 52, '越界', 11.5, color=ACCENT['red']); F.line(242, 107, 286, 107, INK2, 1.2, arrow='end')
F.text(430, 86, '段号 S　偏移量 W', 11, color=INK2); F.box(370, 94, 60, 26, '2', 'amber', 12, 0, True); F.box(430, 94, 80, 26, '100', 'gray', 12, 0, True); F.text(518, 107, '逻辑地址 A', 11.5, 'start', INK2, valign='middle')
F.poly([(400, 122), (400, 140), (300, 140), (300, 122)], INK2, 1.2, arrow='end'); F.poly([(300, 140), (70, 140), (70, 157)], INK2, 1.2, arrow='end')
F.circle(70, 170, 13, '+', 'white', 14); F.line(70, 122, 70, 128, INK2, 1)
F.text(140, 200, '段号　段长 C　基址 b', 11, 'start', INK2)
rows = [('0', '1KB', '6KB'), ('1', '600', '4KB'), ('2', '500', '8KB'), ('3', '200', '9200')]
for i, (s, c, b) in enumerate(rows):
    y = 208 + i * 24
    F.text(130, y + 12, s, 11, 'end', INK2, mono=True, valign='middle'); F.box(140, y, 60, 24, c, 'white', 11, 0, True); F.box(200, y, 60, 24, b, 'blue' if s == '2' else 'white', 11, 0, True)
F.poly([(70, 184), (70, 268), (138, 268)], INK2, 1.2, arrow='end')
F.circle(470, 170, 13, '+', 'white', 14); F.line(470, 122, 470, 156, INK2, 1.2, arrow='end'); F.poly([(262, 268), (330, 268), (330, 170), (456, 170)], INK2, 1.2, arrow='end')
F.box(430, 204, 80, 26, '8292', 'blue', 12, 0, True); F.line(470, 184, 470, 202, INK2, 1.2, arrow='end')
F.text(470, 300 - 50, '', 1)
F.box(560, 220, 60, 100, '', 'white', rx=0); F.rect(560, 250, 60, 30, '#e8effc', ACCENT['blue'], 1, 0); F.text(590, 334, '主存', 11, color=INK2)
F.text(554, 252, '8KB', 10, 'end', INK2, mono=True); F.text(554, 266, '8292', 10, 'end', ACCENT['blue'], mono=True); F.text(554, 282, '8692', 10, 'end', INK2, mono=True)
F.poly([(512, 217), (530, 217), (530, 266), (558, 266)], INK2, 1.2, arrow='end')
F.text(300, 334, '偏移量 100 < 段长 500，不越界；E = 8K + 100 = 8292', 11, color=MUTED)
