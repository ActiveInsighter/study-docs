LABEL = '将用户程序变为可在内存中执行的程序：编译、链接、装入'
F = Fig(760, 300, '编译 → 链接 → 装入')
for x, w, t, tone in ((20, 250, '第一步：编译', 'blue'), (280, 260, '第二步：链接', 'amber'), (550, 190, '第三步：装入', 'amber')):
    F.rect(x, 56, w, 220, tone, TONES[tone][1], 1, 8, opacity=0.5); F.text(x + w / 2, 74, t, 12, color=INK, weight=600)
F.box(34, 150, 50, 36, '代码', 'white', 11, 4)
F.text(150, 168, '编译程序产生\n的目标模块', 11, 'middle', INK2, lh=1.3, valign='middle'); F.line(86, 168, 104, 168, INK2, 1.2, arrow='end')
for i, y in enumerate((96, 130, 166, 230)):
    if i == 0: F.box(200, y, 50, 22, '库', 'white', 10.5, 3)
    elif i == 3: F.box(200, y, 50, 22, '', 'white', rx=3)
    else: F.box(200, y, 50, 22, '', 'white', rx=3)
F.text(225, 206, '⋮', 13, color=MUTED, valign='middle')
F.vbrace(192, 128, 254, '', right=False)
for y in (107, 141, 177, 241): F.line(252, y, 292, 168, INK2, 1)
F.box(294, 150, 60, 36, '链接\n程序', 'white', 11, 4); F.line(356, 168, 384, 168, INK2, 1.2, arrow='end')
F.box(386, 154, 90, 28, '装入模块', 'white', 11, 4); F.line(478, 168, 568, 168, INK2, 1.2, arrow='end')
F.box(570, 150, 54, 36, '装入\n程序', 'white', 11, 4); F.line(626, 168, 668, 168, INK2, 1.2, arrow='end')
F.text(700, 96, '内存', 11, color=INK2)
for i in range(5): F.box(670, 104 + i * 30, 60, 30, '', 'amber' if i in (2, 3) else 'white', rx=0)
