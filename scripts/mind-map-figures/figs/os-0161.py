LABEL = '微内核：单机环境下的客户 / 服务器模式'
F = Fig(700, 230, '单机环境下的客户 / 服务器模式')
labs = ['客户\n进程', '客户\n进程', '进程\n服务器', 'I/O 设备\n服务器', '……', '文件\n服务器', '虚拟存储器\n服务器']
for i, l in enumerate(labs):
    F.box(30 + i * 82, 60, 82, 46, l, 'blue' if i < 2 else ('white' if l == '……' else 'green'), 11, 0)
F.box(30, 106, 574, 60, '', 'white', rx=0); F.text(317, 140, '内核', 13, color=INK, weight=600)
F.poly([(110, 106), (110, 150), (210, 150), (210, 108)], ACCENT['blue'], 1.4, arrow='end'); F.text(110, 182, '请求', 12, color=ACCENT['blue'])
F.poly([(520, 108), (520, 150), (360, 150), (360, 108)], ACCENT['green'], 1.4, arrow='start'); F.text(520, 182, '回答', 12, color=ACCENT['green'])
F.vbrace(610, 62, 104, '用户方式'); F.vbrace(610, 108, 164, '核心方式')
F.text(330, 214, '客户进程通过内核向服务器进程发请求，服务器处理后经内核回答', 11.5, color=MUTED)
