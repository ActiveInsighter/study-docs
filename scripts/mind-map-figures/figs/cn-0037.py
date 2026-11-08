LABEL = '域名解析：递归查询与递归 + 迭代相结合的查询'
F = Fig(860, 360, '域名解析的两种查询方式')
def server(x, y, name, sub):
    F.box(x - 20, y - 18, 40, 36, '', 'blue', rx=4); F.text(x, y + 30, f'{name}\n{sub}', 10, color=INK2, lh=1.25)
for k, x0 in enumerate((20, 450)):
    P = {'root': (x0 + 80, 80), 'top': (x0 + 300, 80), 'local': (x0 + 80, 190), 'auth': (x0 + 300, 190)}
    server(*P['root'], '根域名服务器', ''); server(*P['top'], '顶级域名服务器', 'dns.com'); server(*P['local'], '本地域名服务器', 'dns.xyz.com'); server(*P['auth'], '权限域名服务器', 'dns.abc.com')
    F.box(x0 + 60, 280, 40, 26, '', 'white', rx=3); F.text(x0 + 80, 322, 'm.xyz.com', 10, color=INK2)
    F.text(x0 + 110, 290, '需要查找 y.abc.com 的 IP 地址', 10, 'start', INK2)
    F.line(x0 + 74, 278, x0 + 74, 222, INK2, 1.2, arrow='end'); F.line(x0 + 86, 222, x0 + 86, 278, INK2, 1.2, arrow='end')
    if k == 0:
        F.line(x0 + 74, 172, x0 + 74, 100, INK2, 1.2, arrow='end'); F.line(x0 + 86, 100, x0 + 86, 172, INK2, 1.2, arrow='end')
        F.line(x0 + 102, 74, x0 + 278, 74, INK2, 1.2, arrow='end'); F.line(x0 + 278, 86, x0 + 102, 86, INK2, 1.2, arrow='end')
        F.line(x0 + 294, 100, x0 + 294, 172, INK2, 1.2, arrow='end'); F.line(x0 + 306, 172, x0 + 306, 100, INK2, 1.2, arrow='end')
        F.text(x0 + 190, 66, '递归查询', 10.5, color=INK2); F.text(x0 + 190, 344, '(a) 递归查询（比较少用）', 12, color=INK, weight=600)
    else:
        F.line(x0 + 74, 172, x0 + 74, 100, INK2, 1.2, arrow='end'); F.line(x0 + 86, 100, x0 + 86, 172, INK2, 1.2, arrow='end')
        F.line(x0 + 102, 176, x0 + 278, 96, INK2, 1.2, arrow='end'); F.line(x0 + 278, 106, x0 + 102, 186, INK2, 1.2, arrow='end')
        F.line(x0 + 102, 190, x0 + 278, 190, INK2, 1.2, arrow='end'); F.line(x0 + 278, 200, x0 + 102, 200, INK2, 1.2, arrow='end')
        F.text(x0 + 190, 128, '迭代查询', 10.5, color=INK2); F.text(x0 + 190, 344, '(b) 递归与迭代相结合（常用）', 12, color=INK, weight=600)
    F.text(x0 + 50, 250, '递归查询', 10, 'end', INK2)
