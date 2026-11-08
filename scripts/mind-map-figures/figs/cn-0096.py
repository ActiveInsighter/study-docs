from common import frame
LABEL = '802.11 MAC 帧头：四个地址字段的含义取决于 To DS、From DS'
F = Fig(780, 340, '802.11 帧头')
frame(F, 100, 70, [('帧控制', 80, 'white', 2), ('持续期', 80, 'white', 2), ('地址 1', 90, 'blue', 6), ('地址 2', 90, 'blue', 6), ('地址 3', 90, 'blue', 6), ('序列控制', 90, 'white', 2), ('地址 4', 90, 'blue', 6)])
F.text(305, 122, 'RA 接收端', 10.5, color=INK2); F.text(395, 122, 'TA 发送端', 10.5, color=INK2)
rows = [['功能', 'To DS', 'From DS', 'Address1（接收端）', 'Address2（发送端）', 'Address3', 'Address4'],
        ['IBSS', '0', '0', 'DA', 'SA', 'BSSID', '未使用'], ['To AP（基础结构型）', '1', '0', 'BSSID', 'SA', 'DA', '未使用'],
        ['From AP（基础结构型）', '0', '1', 'DA', 'BSSID', 'SA', '未使用'], ['WDS（无线分布式系统）', '1', '1', 'RA', 'TA', 'DA', 'SA']]
F.table(30, 150, rows, [160, 60, 70, 130, 130, 90, 80], 30, size=11.5, head_tone='amber')
