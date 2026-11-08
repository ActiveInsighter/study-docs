LABEL = '显式链接分配：文件分配表 FAT 集中存放各盘块的下一块号'
F = Fig(640, 400, '显式链接：文件分配表 FAT')
F.table(30, 170, [['文件名', '…', '起始块号'], ['aaa', '…', '2'], ['bbb', '…', '7']], [70, 40, 80], 28, size=12, head_tone='gray', tones={(1, i): 'teal' for i in range(3)} | {(2, i): 'violet' for i in range(3)})
F.text(125, 274, '文件目录', 13, color=INK2)
fat = ['−2', '−1', '8', '−2', '−2', '−1', '−2', '1', '5', '−2', '…', '−2', '−2']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '…', '98', '99']
tone = {1: 'violet', 2: 'teal', 5: 'teal', 7: 'violet', 8: 'teal'}
F.text(400, 60, '盘块号', 12, color=INK2); F.text(470, 60, '下一块', 12, color=INK2)
for i, (n, v) in enumerate(zip(nums, fat)):
    F.box(370, 68 + i * 24, 60, 24, n, tone.get(i, 'white'), 11.5, 0, True); F.box(430, 68 + i * 24, 70, 24, v, tone.get(i, 'white'), 11.5, 0, True)
F.line(222, 212, 368, 128, ACCENT['teal'], 1.2, arrow='end'); F.line(222, 240, 368, 248, ACCENT['violet'], 1.2, arrow='end')
for a, b in ((2, 8), (8, 5), (7, 1)):
    F.curve(502, 80 + a * 24, 502, 80 + b * 24, -0.35, ACCENT['teal'] if a != 7 else ACCENT['violet'], 1.2)
F.text(560, 380, 'FAT（文件分配表）', 12, color=INK2)
F.text(170, 320, '−1：文件结束\n−2：空闲盘块', 11.5, 'middle', MUTED, lh=1.5)
