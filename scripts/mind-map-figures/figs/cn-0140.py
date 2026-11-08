from common import switch_net
LABEL = '虚电路建立：A 发送呼叫请求，沿途交换设备用路由选择算法逐跳转发'
F = Fig(640, 280, '虚电路：建立连接（呼叫请求）')
switch_net(F, ['A', 'SA', 'SB', 'SC', 'SD', 'B'], ACCENT['amber'])
F.text(320, 268, '每台交换设备记录转发方向，形成一条逻辑连接（虚电路）', 11, color=MUTED)
