LABEL = 'HTTP 响应报文的结构'
F = Fig(620, 430, '响应报文')
X = 40
for i, t in enumerate(['版本', '状态码', '短语']):
    F.box(X + i * 125, 80, 120, 34, t, 'green' if True else 'blue', 12.5, 0)
F.box(X + 375, 80, 100, 34, 'CRLF', 'white', 12, 0)
F.text(X + 490, 97, '状态行', 12.5, 'start', ACCENT['green'] if True else ACCENT['blue'], 700, valign='middle')
for r, y in enumerate((120, 160, 200)):
    if r == 1:
        F.box(X, y, 300, 40, '⋮', 'white', 13, 0); continue
    F.box(X, y, 140, 40, '首部字段名', 'white', 12, 0); F.box(X + 140, y, 20, 40, ':', 'white', 12, 0); F.box(X + 160, y, 60, 40, '值', 'white', 12, 0); F.box(X + 220, y, 80, 40, 'CRLF', 'white', 12, 0)
F.vbrace(X + 306, 120, 240, '首部行')
F.box(X, 246, 100, 36, 'CRLF', 'white', 12, 0)
F.box(X, 288, 475, 80, '实体主体\n（有些响应报文不用实体主体）', 'green' if True else 'blue', 12.5, 0)
F.text(X + 237, 394, '响应报文', 12.5, color=INK2)
F.text(X + 240, 72, '1xx 通知信息　2xx 成功　3xx 重定向　4xx 客户端错误（404）　5xx 服务器错误', 11, color=ACCENT['green'])
