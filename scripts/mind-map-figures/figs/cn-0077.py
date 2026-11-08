LABEL = '若 A 向 B 发送信息的工作流程：ARP 广播请求、单播响应，再封装发送'
F = Fig(820, 380, 'ARP：A 向 B 发送信息')
N = {'1': (60, 70), 'hub': (180, 70), 'sw1': (300, 70), '2': (260, 150), '3': (340, 150), 'r1': (400, 90), 'r2': (470, 70), 'sw2': (580, 70), '4': (610, 150), '5': (700, 70)}
for a, b in (('1', 'hub'), ('hub', 'sw1'), ('sw1', '2'), ('sw1', '3'), ('sw1', 'r1'), ('r1', 'r2'), ('r2', 'sw2'), ('sw2', '4'), ('sw2', '5')): F.line(*N[a], *N[b], ACCENT['blue'], 1.2)
for k, (x, y) in N.items():
    if k in '12345': F.box(x - 14, y - 10, 28, 20, k, 'teal', 11, 3)
    elif k in ('hub', 'sw1', 'sw2'): F.box(x - 30, y - 13, 60, 26, {'hub': '集线器', 'sw1': '交换机', 'sw2': '交换机'}[k], 'blue', 11, 3)
    else: F.ellipse(x, y, 16, 8, '', 'teal')
F.text(300, 44, '默认网关 IP6', 10.5, color=INK2); F.text(400, 112, 'MAC6 MAC7', 9.5, color=MUTED); F.text(470, 50, 'MAC8 MAC9', 9.5, color=MUTED)
F.cells(370, 122, ['IP1', 'IP5', 'MAC7', 'MAC8'], 44, 22, {2: 'green', 3: 'green'}, size=10.5)
F.box(30, 108, 140, 34, 'ARP 高速缓存\n（IP 地址与 MAC 地址的映射）', 'white', 9.5, 4)
labs = [('应用层', 210), ('传输层', 236), ('网络层', 262), ('数据链路层', 288), ('物理层', 314)]
for t, y in labs: F.box(40, y, 80, 26, t, 'amber', 11, 0)
F.cells(130, 210, ['1'], 26, 22, {0: 'red'}); F.cells(130, 236, ['1', '2', '3'], 26, 22, size=10.5)
F.cells(130, 262, ['1', 'IP1', 'IP5'], [0] and 0, 0) if False else F.cells(130, 262, ['1', 'IP1', 'IP5'], 36, 22, size=10.5)
F.cells(130, 288, ['FCS', '1', 'IP1', 'IP5', 'MAC1', 'MAC6'], 40, 22, {0: 'green', 4: 'green', 5: 'green'}, size=10)
F.path('M130 325' + 'h6v-8h6v8' * 14, INK2, 1)
F.text(560, 214, '广播 ARP 请求分组 →', 10.5, color=INK2)
F.cells(460, 226, ['IP1', 'IP6', 'MAC1', 'FF-FF-FF-FF-FF-FF'], [0] and 0, 0) if False else (F.box(460, 226, 40, 24, 'IP1', 'white', 10.5, 0), F.box(500, 226, 40, 24, 'IP6', 'white', 10.5, 0), F.box(540, 226, 50, 24, 'MAC1', 'green', 10.5, 0), F.box(590, 226, 150, 24, 'FF-FF-FF-FF-FF-FF', 'green', 10.5, 0, True))
F.text(560, 276, '← 单播 ARP 响应分组', 10.5, color=INK2)
F.box(460, 288, 40, 24, 'IP6', 'white', 10.5, 0); F.box(500, 288, 50, 24, 'MAC6', 'green', 10.5, 0)
F.text(410, 362, 'B 不在本网：A 用 ARP 得到默认网关（IP6）的 MAC6，帧的目的 MAC 写 MAC6；之后逐跳更换 MAC', 11, color=MUTED)
