from common import code
LABEL = '数据的逻辑结构与存储（物理）结构'
F = Fig(860, 470, '逻辑结构 ↔ 存储结构')
F.text(30, 84, '存储结构（物理）', 14, 'start', INK, 700)
# linked
F.text(40, 112, '链式存储：结点可以不连续，靠指针相连', 12.5, 'start', INK2)
for i, (addr, x) in enumerate((('0x0000', 60), ('0x0008', 200), ('0x1234', 340))):
    F.cells(x, 126, [f'a{i}', '●' if i < 2 else '∧'], 40, 28, {0: 'blue'}, size=12)
    F.text(x + 40, 172, addr, 11, color=MUTED, mono=True)
    if i < 2: F.line(x + 60, 140, x + 138, 140, INK2, 1.3, arrow='end')
code(F, 60, 202, 'ListNode a;  &a = 0x0000\n&(a->next) = 0x0008\n&(a->next->next) = 0x1234', 11.5)
F.text(440, 112, '顺序存储：连续存放，可随机存取', 12.5, 'start', INK2)
F.cells(460, 126, ['a[0]', 'a[1]', 'a[2]', 'a[3]', 'a[4]'], 52, 28, {i: 'green' for i in range(5)}, size=12, index=['0x00', '0x04', '0x08', '0x0C', '0x10'])
code(F, 460, 202, 'int a[5];  &a[0] = 0x0000\n&a[i] = &a[0] + i × sizeof(int)', 11.5)
F.line(30, 262, 830, 262, FAINT, 1)
F.text(30, 294, '逻辑结构', 14, 'start', INK, 700)
for i, (t, x) in enumerate((('线性结构', 40), ('树形结构', 250), ('图状结构', 450), ('集合', 650))):
    F.text(x + 70, 324, t, 13, color=INK2, weight=600)
F.graph({'a': (60, 380), 'b': (110, 380), 'c': (160, 380), 'd': (210, 380)}, [('a','b'), ('b','c'), ('c','d')], r=11, directed=False, labels={k: '' for k in 'abcd'})
F.tree(270, 356, ('r', [('x', ['y', 'z']), 'w']), unit=34, levelh=40, r=10, labels={k: '' for k in 'rxyzw'})
F.graph({'a': (480, 360), 'b': (560, 350), 'c': (520, 420), 'd': (600, 410)}, [('a','b'), ('a','c'), ('b','c'), ('b','d'), ('c','d')], r=11, directed=False, labels={k: '' for k in 'abcd'})
F.ellipse(720, 390, 56, 38, '', 'white', dash='4 3')
for (x, y) in ((700, 375), (735, 372), (710, 405), (745, 402)): F.circle(x, y, 8)
F.text(430, 456, '同一种逻辑结构既可以顺序存储，也可以链式存储（如二叉树可用数组或二叉链表）', 12.5, color=MUTED)
