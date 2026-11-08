LABEL = 'B 树非叶结点的结构'
F = Fig(720, 210, 'B 树非叶结点的结构')
F.cells(40, 70, ['n', 'P_{0}', 'K_{1}', 'P_{1}', 'K_{2}', 'P_{2}', '…', 'K_{n}', 'P_{n}'], 70, 34, {i: ('blue' if i in (2, 4, 7) else 'white') for i in range(9)}, size=15, mono=False)
F.text(40, 134, 'K_{i}：关键字，满足 K_{1} < K_{2} < … < K_{n}　　P_{i}：指向子树根结点的指针', 13.5, 'start', INK2)
F.text(40, 160, 'P_{i−1} 所指子树的关键字均 < K_{i}，P_{i} 所指子树的关键字均 > K_{i}', 13.5, 'start', ACCENT['red'])
F.text(40, 186, 'n：结点中关键字个数，⌈m/2⌉ − 1 ≤ n ≤ m − 1', 13.5, 'start', INK2)
