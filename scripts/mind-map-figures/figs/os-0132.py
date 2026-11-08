LABEL = '索引顺序文件：索引表按关键字指向逻辑文件中的分组'
F = Fig(640, 300, '索引顺序文件')
F.table(30, 70, [['键', '逻辑地址'], ['An Qi', '●'], ['Bao Rong', '●'], ['Chen Lin', '●'], ['', ''], ['', '']], [110, 90], 28, size=12, head_tone='gray', tones={(1, 0): 'amber', (1, 1): 'amber', (2, 0): 'blue', (2, 1): 'blue', (3, 0): 'blue', (3, 1): 'blue'}, zebra=False)
F.text(130, 250, '索引表', 12, color=INK2)
rows = [('An Qi', 'amber'), ('An Kang', 'amber'), ('', 'amber'), ('', 'amber'), ('Bao Rong', 'blue'), ('', 'blue'), ('…', 'white')]
for i, (t, tone) in enumerate(rows): F.box(380, 70 + i * 26, 110, 26, t, tone, 11.5, 0); F.box(490, 70 + i * 26, 110, 26, '', tone, rx=0)
F.text(435, 62, '姓名', 11.5, color=INK2); F.text(545, 62, '其他属性', 11.5, color=INK2)
F.text(490, 270, '逻辑文件', 12, color=INK2)
F.line(200, 112, 378, 84, INK2, 1.1, arrow='end'); F.line(200, 140, 378, 188, INK2, 1.1, arrow='end'); F.line(200, 168, 378, 240, INK2, 1.1, arrow='end')
