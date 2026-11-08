from common import chain, code
LABEL = '栈的链式存储：链头为栈顶'
F = Fig(720, 280, '链栈（不带头结点，链头为栈顶）')
F.text(84, 124, 'Lhead', 13, 'end', INK2, mono=True, valign='middle')
F.line(88, 124, 110, 124, INK2, 1.3, arrow='end')
end = chain(F, 112, 110, [['a₁'], ['a₂']], tail='', data_tone='blue')
F.text(end + 6, 124, '…', 16, 'start', MUTED, valign='middle')
F.line(end + 30, 124, end + 52, 124, INK2, 1.3, arrow='end')
F.cells(end + 54, 110, ['aₙ', '∧'], 34, 28, {0: 'blue'}, size=13)
F.text(140, 96, '栈顶结点', 12, color=ACCENT['red']); F.text(end + 88, 96, '栈底结点', 12, color=MUTED)
code(F, 40, 190, 'typedef struct Linknode {\n  ElemType data;           // 数据域\n  struct Linknode *next;   // 指针域\n} *LiStack;                // 栈类型定义', 12.5)
F.text(690, 260, '入栈、出栈都在链头进行', 12.5, 'end', MUTED)
