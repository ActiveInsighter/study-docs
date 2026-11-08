from common import gate, wire
LABEL = '中断判优：硬件排队器或软件查询程序'
F = Fig(800, 360, '中断判优：硬件排队器 / 查询程序')
xs = [60, 180, 300, 420]
prev = None
for i, x in enumerate(xs):
    F.text(x + 20, 62, f'INTP_{{{i + 1}}}', 12, color=INK, mono=True)
    F.line(x + 20, 120, x + 20, 76, INK2, 1.2, arrow='end'); F.text(x + 28, 96, '1' if i == 0 else '0', 10.5, 'start', ACCENT['red'])
    F.box(x, 120, 40, 28, '1', 'white', 12, 3)
    F.box(x, 190, 40, 28, '1' if i == 0 else '&', 'white', 12, 3)
    F.line(x + 20, 150, x + 20, 188, INK2, 1.2); F.circle(x + 20, 168, 2.5, '', 'dark', sw=0); F.text(x + 28, 164, '0' if i == 0 else '1', 10.5, 'start', ACCENT['red'])
    F.line(x + 20, 220, x + 20, 290, INK2, 1.2); F.text(x + 20, 304, f'1  INTR_{{{i + 1}}}', 11.5, color=ACCENT['red'], mono=True)
    if i:
        for j in range(i):
            F.poly([(xs[j] + 20, 168), (xs[j] + 30, 168), (xs[j] + 30, 240 + j * 6), (x + 30 + j * 4, 240 + j * 6), (x + 30 + j * 4, 220)], INK2, 1)
F.box(140, 318, 220, 26, '硬件排队器', 'blue', 11.5, 4)
F.box(500, 100, 34, 170, '查\n询\n程\n序', 'green', 11.5, 4)
for i, n in enumerate('ABC'):
    y = 80 + i * 90
    F.items.append(f'<path d="M640 {y}L690 {y + 26}L640 {y + 52}L590 {y + 26}Z" fill="#fdf1d8" stroke="#c98a12" stroke-width="1.2"/>'); F.text(640, y + 26, f'{n} 请求？', 11.5, color='#78350f', valign='middle')
    F.line(692, y + 26, 720, y + 26, INK2, 1.2, arrow='end'); F.text(724, y + 26, f'转 {n} 的服务\n程序入口地址', 10.5, 'start', INK2, lh=1.3, valign='middle'); F.text(700, y + 18, 'Y', 10, color=INK2)
    if i < 2: F.line(640, y + 52, 640, y + 88, INK2, 1.2, arrow='end'); F.text(648, y + 72, 'N', 10, 'start', INK2)
F.line(640, 50, 640, 78, INK2, 1.2, arrow='end')
