LABEL = '无向图中子图、连通分量、极小连通子图、生成树的关系'
F = Fig(560, 360, '无向图中的几个概念')
F.ellipse(280, 190, 250, 150, '', 'light')
F.text(280, 64, '子图', 14, color=INK2, weight=600)
F.ellipse(280, 200, 190, 116, '', 'white', dash='5 4')
F.text(280, 104, '连通图', 13, color=MUTED, weight=600)
F.circle(190, 210, 68, '', 'blue'); F.text(190, 202, '连通分量', 14, color=TONES['blue'][2], weight=700); F.text(190, 224, '（极大连通子图）', 12, color=TONES['blue'][2])
F.circle(360, 210, 72, '', 'green'); F.text(360, 186, '极小连通子图', 14, color=TONES['green'][2], weight=700)
F.circle(360, 236, 32, '生成树', 'white', 13)
