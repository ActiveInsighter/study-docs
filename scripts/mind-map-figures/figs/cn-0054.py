from common import switch_net
LABEL = '虚电路释放：与建立连接类似，沿原路发送释放请求'
F = Fig(640, 280, '虚电路：释放连接')
switch_net(F, ['A', 'SA', 'SB', 'SC', 'SD', 'B'], ACCENT['green'])
F.text(320, 268, '释放请求沿同一路径传递，释放沿途资源；最后不再返回', 11, color=MUTED)
