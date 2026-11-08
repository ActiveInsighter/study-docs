LABEL = '分层的操作系统：层 0 为硬件，层 N 为用户接口，每层只能调用相邻低层'
F = Fig(460, 400, '分层的操作系统')
for r, t, lab in ((150, 'blue', '层 N\n用户接口'), (112, 'green', '…'), (74, 'amber', '层 1'), (36, 'violet', '层 0\n硬件')):
    F.circle(230, 220, r, '', t)
F.text(230, 100, '层 N　用户接口', 12.5, color=INK, weight=600); F.text(230, 132, '⋯', 13, color=MUTED); F.text(230, 168, '层 1', 12.5, color=INK, weight=600); F.text(230, 220, '层 0\n硬件', 12.5, color=INK, weight=600, valign='middle')
F.text(230, 390, '每层只能调用紧邻它的低层的功能和服务（单向依赖）', 11.5, color=MUTED)
