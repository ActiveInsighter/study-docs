LABEL = '单级目录结构：所有文件的 FCB 放在一个目录中'
F = Fig(560, 180, '单级目录结构')
for i, t in enumerate(('FCB₁', 'FCB₂', 'FCB₃', '…', 'FCBₙ')):
    F.box(30 + i * 100, 60, 100, 36, t, 'blue' if t != '…' else 'white', 13, 0)
    F.ellipse(80 + i * 100, 140, 36, 18, f'文件{t[3:]}' if t != '…' else '…', 'white' if t != '…' else 'none', 12)
    if t != '…': F.line(80 + i * 100, 96, 80 + i * 100, 120, INK2, 1.2, arrow='end')
