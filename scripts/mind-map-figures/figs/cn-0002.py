LABEL = 'PPP 协议的工作流程：链路静止 → 建立 → 鉴别 → 网络层协议 → 链路打开 → 终止'
F = Fig(700, 420, 'PPP 协议的工作流程')
st = [('链路静止', 60), ('链路建立', 130), ('鉴别', 200), ('网络层协议', 270), ('链路打开', 340)]
for t, y in st: F.box(260, y, 140, 40, t, 'white', 13, 0)
for (la, a), (lb, b) in zip(st, st[1:]):
    F.line(330, a + 42, 330, b - 2, INK2, 1.3, arrow='end')
lbls = ['物理层连接建立', 'LCP 配置协商', '鉴别成功或无需鉴别', 'NCP 配置协商']
for i, l in enumerate(lbls): F.text(340, st[i][1] + 58, l, 11, 'start', INK2)
F.box(40, 200, 120, 40, '链路终止', 'white', 13, 0)
F.line(258, 220, 162, 220, INK2, 1.3, arrow='end'); F.text(210, 210, '鉴别失败', 11, color=INK2)
F.poly([(258, 150), (230, 150), (230, 90), (258, 90)], INK2, 1.3, arrow='end'); F.text(226, 120, 'LCP 配置协商失败', 11, 'end', INK2)
F.poly([(258, 360), (100, 360), (100, 242)], INK2, 1.3, arrow='end'); F.text(96, 310, '链路故障或\n关闭请求', 11, 'end', INK2, lh=1.3)
F.poly([(100, 198), (100, 80), (258, 80)], INK2, 1.3, arrow='end'); F.text(96, 130, 'LCP 链路\n终止', 11, 'end', INK2, lh=1.3)
for i, t in enumerate(('设备之间无链路', '物理链路', 'LCP 链路', '已鉴别的 LCP 链路', '已鉴别的 LCP\n链路和 NCP 链路')):
    F.box(480, st[i][1], 180, 40, t, 'blue', 12, 0)
    if i: F.line(570, st[i - 1][1] + 42, 570, st[i][1] - 2, INK2, 1.2, arrow='end')
