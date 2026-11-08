from common import chain, code
LABEL = '串的链式存储：每个结点存 1 个字符与存多个字符的对比'
F = Fig(720, 380, '串的链式存储')
code(F, 30, 84, 'typedef struct StringNode {\n  char ch;                 // 每个结点存 1 个字符\n  struct StringNode *next;\n} StringNode, *String;', 13)
chain(F, 40, 152, [['a'], ['b'], ['c'], ['d'], ['e']], head='S')
F.box(500, 146, 196, 40, '存储密度低\n字符 1B，指针 4B', 'red', 12, 8)
code(F, 30, 236, 'typedef struct StringNode {\n  char ch[4];              // 每个结点存多个字符\n  struct StringNode *next;\n} StringNode, *String;', 13)
chain(F, 40, 304, [['a', 'b', 'c', 'd'], ['e', '#', '#', '#']], head='S')
F.box(500, 298, 196, 40, '存储密度提高\n末结点不足用 # 补齐', 'green', 12, 8)
