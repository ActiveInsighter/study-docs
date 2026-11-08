LABEL = '并查集的存储结构：用森林表示，每个子集一棵树'
F = Fig(640, 300, '用森林存储：每个子集是一棵树')
F.tree(30, 90, ('A', [('B', [('E', ['K', 'L']), 'F'])]), unit=48, levelh=58, r=18, tones={k: 'green' for k in 'ABEFKL'})
F.tree(260, 110, ('C', ['G']), unit=48, levelh=80, r=18, tones={'C': 'violet', 'G': 'violet'})
F.tree(360, 100, ('D', [('H', ['M']), 'I', 'J']), unit=60, levelh=66, r=18, tones={k: 'amber' for k in 'DHIJM'})
F.text(320, 288, '同一棵树中的元素属于同一个集合；根结点代表该集合', 12.5, color=MUTED)
