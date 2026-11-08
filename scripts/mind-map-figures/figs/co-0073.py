LABEL = '源程序转换为可执行文件的过程'
F = Fig(860, 220, '从源程序到可执行程序')
st = [('hello.c', '源程序（文本）'), ('hello.i', '修改了的源程序'), ('hello.s', '汇编程序（文本）'), ('hello.o', '可重定位目标文件'), ('hello', '可执行文件')]
tools = [('预处理器', 'cpp', 'amber'), ('编译器', 'ccl', 'green'), ('汇编器', 'as', 'blue'), ('链接器', 'ld', 'violet')]
for i, (f, d) in enumerate(st):
    x = 16 + i * 192
    F.text(x + 40, 112, f, 13, color=INK, mono=True, weight=600)
    F.text(x + 40, 136, d, 11, color=MUTED)
    if i < 4:
        t, c, tone = tools[i]
        F.line(x + 74, 108, x + 104, 108, INK2, 1.3, arrow='end')
        F.box(x + 106, 84, 76, 46, f'{t}\n({c})', tone, 12.5, 8)
        F.line(x + 182, 108, x + 210, 108, INK2, 1.3, arrow='end')
F.text(708, 70, 'printf.o', 12, color=INK2, mono=True); F.line(708, 76, 708, 82, INK2, 1.2, arrow='end')
F.text(430, 196, '预处理（展开 #include、宏）→ 编译 → 汇编 → 链接（合并库函数目标文件）', 12.5, color=MUTED)
