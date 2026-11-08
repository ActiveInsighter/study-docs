LABEL = '模块化设计原则：模块内高内聚，模块间低耦合'
F = Fig(560, 260, '高内聚、低耦合')
F.ellipse(150, 140, 110, 66, '', 'white'); F.ellipse(410, 140, 110, 66, '', 'white')
N = {'a': (150, 98), 'b': (100, 140), 'c': (150, 140), 'd': (200, 140), 'e': (160, 182)}
F.graph(N, [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('d', 'e')], r=9, directed=False, labels={k: '' for k in N}, tones={k: 'blue' for k in N})
F.path('M260 140q5 -8 10 0t10 0t10 0', ACCENT['red'], 1.6)
F.text(150, 60, '高内聚：模块内部联系紧密', 12.5, color=ACCENT['blue'], weight=600); F.text(280, 112, '耦合低', 12.5, color=ACCENT['red'], weight=600)
F.text(150, 228, '模块 1', 13, color=INK2); F.text(410, 228, '模块 2', 13, color=INK2)
