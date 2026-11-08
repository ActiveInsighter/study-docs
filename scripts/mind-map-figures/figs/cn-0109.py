LABEL = 'IPv4 数据报格式：20 B 固定首部 + 可变部分'
F = Fig(820, 420, 'IPv4 数据报格式')
X, W = 120, 620
for t, xx in (('0', 0), ('4', 0.125), ('8', 0.25), ('16', 0.5), ('19', 0.59), ('24', 0.75), ('31', 1)): F.text(X + W * xx, 60, t, 10.5, color=MUTED, mono=True)
def r(y, cells):
    x = X
    for t, w, tone in cells:
        F.box(x, y, W * w, 30, t, tone, 11, 0); x += W * w
r(68, [('版本\nIPv4', 0.125, 'white'), ('首部长度\n（4 B 为单位）', 0.125, 'amber'), ('区分服务', 0.25, 'white'), ('总长度（单位 1 B，≤ MTU）', 0.5, 'amber')])
r(98, [('标识（分片用：同一数据报的分片相同）', 0.5, 'white'), ('标志\nMF DF', 0.09, 'white'), ('片偏移（8 B 为单位）', 0.41, 'amber')])
r(128, [('生存时间 TTL', 0.25, 'white'), ('协议\nTCP 6 / UDP 17', 0.25, 'white'), ('首部校验和（只校验首部）', 0.5, 'white')])
r(158, [('源地址（IPv4，4 B）', 1, 'blue')]); r(188, [('目的地址（IPv4，4 B）', 1, 'blue')])
r(218, [('可选字段（长度可变，0 ~ 40 B）', 0.8, 'light'), ('填充', 0.2, 'light')])
F.box(X, 248, W, 60, '数据部分', 'green', 12.5, 0)
F.vbrace(X - 6, 68, 218, '固定部分\n20 B', right=False, size=11); F.vbrace(X - 70, 68, 248, '首部', right=False, size=11)
F.box(250, 340, 100, 30, '首部', 'white', 12, 0); F.box(350, 340, 300, 30, '数据部分（来自传输层）', 'white', 12, 0)
F.line(250, 384, 650, 384, INK2, 1, arrow='both'); F.text(450, 400, 'IP 数据报（首部先发送）', 11, color=INK2)
F.text(780, 83, '最大\n65535', 10, 'middle', MUTED, lh=1.2, valign='middle')
