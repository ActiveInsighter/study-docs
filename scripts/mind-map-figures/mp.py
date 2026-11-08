from svgkit import *
def core(F, x, y, w=120, h=110, alu='ALU', pc=True, regs=('数据寄\n存器组', '地址寄\n存器组')):
    F.box(x, y, w, h, '', 'white', rx=6)
    F.box(x + 8, y + 10, (w - 24) / 2, 32, regs[0], 'amber', 9.5, 3); F.box(x + 16 + (w - 24) / 2, y + 10, (w - 24) / 2, 32, regs[1], 'green', 9.5, 3)
    F.items.append(f'<path d="M{x + w / 2 - 24} {y + 52}H{x + w / 2 + 24}L{x + w / 2 + 14} {y + 70}H{x + w / 2 - 14}Z" fill="#e0f3f1" stroke="#23877c" stroke-width="1.2"/>')
    F.text(x + w / 2, y + 61, alu, 9.5, color='#134e4a', weight=700, valign='middle')
    F.box(x + 20, y + 80, w - 40, 22, 'CU', 'white', 10, 3)
    if pc: F.box(x + w - 46, y + 83, 22, 16, 'PC', 'red', 8.5, 2)
def machine(F, x, y, title='计算机'):
    F.rect(x, y, 230, 170, '#fafafa', '#a1a1aa', 1.2, 10); F.text(x + 115, y + 16, title, 11.5, color=INK, weight=600)
    F.text(x + 70, y + 34, '处理器', 10.5, color=MUTED); core(F, x + 10, y + 40, 120, 104)
    F.box(x + 150, y + 30, 60, 114, '主存储器', 'blue', 10.5, 4)
    F.line(x + 10, y + 156, x + 220, y + 156, INK2, 2); F.text(x + 115, y + 166, '总线', 10, color=MUTED)
    return (x + 115, y + 85)
