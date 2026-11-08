from common import sine_path
LABEL = '模拟数据 → 模拟信号：把声音加载到高频载波上传输（如广播）'
F = Fig(640, 220, '模拟数据 → 模拟信号（调制）')
F.circle(80, 110, 26, '', 'violet'); F.path('M70 124L80 96L90 124M74 112H86', ACCENT['violet'], 1.6); F.circle(80, 94, 4, '', 'violet', sw=1.4)
F.path(sine_path(120, 116, 50, 4, 6), ACCENT['violet'], 1.4); F.path(sine_path(220, 112, 90, 7, 18), ACCENT['blue'], 1.6); F.path(sine_path(400, 116, 50, 4, 6), ACCENT['violet'], 1.4)
F.line(190, 80, 380, 80, INK2, 1.4, arrow='end'); F.text(285, 70, '高频载波信号', 11, color=INK2)
F.box(480, 90, 90, 50, '收音机', 'amber', 13, 8)
F.text(320, 190, '声音数据（模拟）加载到载波上，可利用频分复用充分利用带宽资源', 11.5, color=MUTED)
