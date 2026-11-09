LABEL = '基于接口的 VLAN：交换机端口划分 VLAN，不同 VLAN 通信需要路由器或三层交换机'
F = Fig(760, 300, '基于接口的 VLAN')
F.rect(60, 54, 220, 50, 'none', INK2, 1.2, 0); F.text(170, 70, '交换机', 12, color=INK2)
for i, (n, t) in enumerate((('1', 'amber'), ('2', 'amber'), ('3', 'dark'), ('4', 'dark'))): F.box(110 + i * 34 + (20 if i > 1 else 0), 92, 28, 20, n, t, 11, 0)
F.rect(20, 80, 164, 170, 'none', ACCENT['amber'], 1.4, 12); F.rect(190, 80, 140, 170, 'none', INK, 1.4, 12)
for i, (n, x, port) in enumerate((('A', 60, 124), ('B', 120, 158), ('C', 220, 212), ('D', 280, 246))):
    F.box(x - 14, 180, 28, 24, n, 'amber' if i < 2 else 'gray', 12, 3); F.line(x, 180, port, 112, INK2, 1.2)
F.pill(50, 256, 'VLAN1', 'amber', 11); F.pill(222, 256, 'VLAN2', 'dark' if False else 'gray', 11)
F.text(352, 60, '交换机上生成的各 VLAN 互不相通，若想实现通信，\n需要借助：① 路由器　② 三层交换机', 11.5, 'start', INK2, lh=1.5)
F.text(440, 124, '交换机的转发表', 12, color=ACCENT['blue'])
F.table(370, 134, [['MAC 地址', '端口'], ['A', '1'], ['B', '2'], ['C', '3'], ['D', '4']], [80, 60], 26, size=11.5, head_tone='blue')
F.text(640, 124, '交换机的 VLAN 表', 12, color=ACCENT['blue'])
F.table(570, 134, [['VLAN ID', '端口'], ['1', '1'], ['1', '2'], ['2', '3'], ['2', '4']], [80, 60], 26, size=11.5, head_tone='blue')
