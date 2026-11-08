from mp import core
LABEL = '向量处理器：特殊的 SIMD，一次处理多个数据组成的向量'
F = Fig(760, 300, '向量处理器（SIMD）')
for k, x in enumerate((20, 470)):
    F.rect(x, 56, 270, 200, '#fafafa', '#a1a1aa', 1.2, 10); F.text(x + 135, 72, '处理器', 11.5, color=INK, weight=600)
    for i in range(3):
        F.box(x + 10 + i * 86, 84, 78, 24, '局部存储器', 'white', 9.5, 3)
        F.box(x + 10 + i * 86, 114, 37, 30, '向量寄\n存器组', 'green', 8.5, 3); F.box(x + 51 + i * 86, 114, 37, 30, '地址寄\n存器组', 'green', 8.5, 3)
        F.items.append(f'<path d="M{x + 22 + i * 86} 156H{x + 76 + i * 86}L{x + 66 + i * 86} 174H{x + 32 + i * 86}Z" fill="#e0f3f1" stroke="#23877c" stroke-width="1.1"/>'); F.text(x + 49 + i * 86, 165, '向量ALU', 8.5, color='#134e4a', valign='middle')
        F.line(x + 49 + i * 86, 176, x + 49 + i * 86, 200, INK2, 1)
    F.box(x + 95, 200, 80, 22, 'CU', 'white', 10, 3); F.line(x + 30, 200, x + 220, 200, INK2, 1)
F.box(320, 56, 120, 200, '主存储器\n\n支持多端口\n同时读取的\n多模块交叉\n存储器', 'blue', 10.5, 4)
F.line(20, 278, 740, 278, INK2, 2); F.text(380, 292, '总线', 10.5, color=MUTED)
