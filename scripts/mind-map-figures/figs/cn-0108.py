LABEL = '细分 SDN 控制器：北向接口层、全网状态管理层、南向通信层'
F = Fig(560, 540, '细分 SDN 控制器')
for x, t in ((100, '路由选择'), (250, '接入控制'), (380, '负载均衡')): F.ellipse(x, 70, 50, 18, t, 'blue', 11)
F.text(250, 70, '···', 12, color=MUTED, valign='middle') if False else None
F.line(30, 100, 450, 100, ACCENT['blue'], 1.2, dash='6 4'); F.text(530, 100, '北向 API', 11.5, 'end', ACCENT['blue'], valign='middle')
layers = [('接口，对于网络控制应用程序的抽象', ['网络图', 'REST 风格的 API', '…', '意图']), ('网络范围的分布式、健壮的状态管理', ['统计', '…', '流表', '链路状态信息', '主机信息', '交换机信息']), ('到 / 来自受控设备的通信', ['OpenFlow', '…', 'SNMP'])]
y = 116
for title, items in layers:
    h = 70 if len(items) <= 4 else 100
    F.rect(50, y, 380, h, ACCENT['blue'], 'none', 0, 4, opacity=0.9)
    F.text(240, y + 16, title, 11, color='#ffffff', weight=600)
    for i, it in enumerate(items):
        col, row = i % 4, i // 4
        if len(items) > 4: col, row = i % 3, i // 3
        F.box(66 + col * (360 / (4 if len(items) <= 4 else 3)), y + 30 + row * 34, 80, 26, it, 'white', 10, 3)
    y += h + 10
F.vbrace(436, 116, y - 10, 'SDN 控制器', color=ACCENT['blue'])
F.line(30, y + 6, 450, y + 6, ACCENT['blue'], 1.2, dash='6 4'); F.text(530, y + 6, '南向 API', 11.5, 'end', ACCENT['blue'], valign='middle')
F.ellipse(240, y + 70, 180, 50, '', 'light')
for x, yy in ((150, y + 60), (240, y + 50), (330, y + 62), (190, y + 90), (290, y + 92)): F.ellipse(x, yy, 12, 6, '', 'teal')
