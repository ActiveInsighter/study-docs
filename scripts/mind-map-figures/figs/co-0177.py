LABEL = '内存映射 I/O 与独立编址 I/O 的对比'
F = Fig(760, 420, '内存映射 I/O vs 独立编址 I/O')
def col(x, title, mem_labels, side):
    F.text(x + 110, 64, title, 14, color=INK, weight=700)
    F.text(x - 24, 84, '地址', 11, color=MUTED)
    F.box(x, 90, 140, 90, '内存', 'blue', 13, 0)
    for g in range(2):
        for k in range(3):
            y = 180 + g * 100 + k * 24
            F.box(x, y, 60, 24, f'寄存器{k}', 'amber', 10.5, 0)
            F.text(x - 8, y + 12, mem_labels[g * 3 + k], 11, 'end', ACCENT['red'], mono=True, valign='middle')
        F.box(x + 60, 180 + g * 100, 80, 96, f'设备控\n制器{g}', 'amber', 11, 0)
    F.text(x - 8, 98, '0', 11, 'end', INK2, mono=True); F.text(x - 8, 172, 'N−1', 11, 'end', INK2, mono=True)
col(60, '内存映射 I/O', ['N', 'N+1', 'N+2', 'N+3', 'N+4', 'N+5'], 'r')
col(560, '独立编址 I/O', ['0', '1', '2', '0', '1', '2'], 'l')
F.box(230, 90, 150, 76, '控制器中的寄存器与\n内存地址统一编址', 'gray', 11, 8)
F.box(230, 240, 150, 120, '优点：简化了指令，\n可以采用对内存进行\n操作的指令来对控制器\n进行操作', 'green', 11, 8)
F.box(390, 90, 150, 76, '寄存器独立编址：\n控制器中的寄存器使用\n单独的地址', 'gray', 11, 8)
F.box(390, 210, 150, 150, '缺点：需要设置专门的\n指令来实现对控制器的\n操作；不仅要指明\n寄存器的地址，还要\n指明控制器的编号', 'red', 11, 8)
