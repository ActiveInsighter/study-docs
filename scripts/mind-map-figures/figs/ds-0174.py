LABEL = '二叉排序树的平均查找长度（查找失败）'
F = Fig(860, 400, '二叉排序树 ASL（查找失败）')
nil = True
def T(t):
    if not nil: return t
    def f(n):
        if n is None: return '□'
        if isinstance(n, str): return (n, ['□', '□'])
        return (n[0], [f(k) for k in n[1]])
    return f(t)
good = ('50', [('26', ['21', '30']), ('66', ['60', ('70', [('68', [None, None]) if False else '68', None])])])
good = ('50', [('26', ['21', '30']), ('66', ['60', ('70', ['68', None])])])
bad = ('26', ['21', ('30', [None, ('50', [None, ('60', [None, ('66', [None, ('68', [None, '70'])])])])])])
cnt = [0]
def uniq(n):
    if n == '□':
        cnt[0] += 1; return '□ #' + str(cnt[0])
    if n is None or isinstance(n, str): return n
    return (n[0], [uniq(k) for k in n[1]])
F.tree(20, 90, uniq(T(good)), unit=30, levelh=56, r=15, size=12, mono=True, tones={k: 'blue' for k in ['50','26','66','21','30','60','70','68']})
F.tree(420, 90, uniq(T(bad)), unit=26, levelh=36, r=14, size=11, mono=True, tones={k: 'blue' for k in ['50','26','66','21','30','60','70','68']})
F.text(30, 380, 'ASL = (3×7 + 4×2) / 9 = 3.22', 13.5, 'start', INK2, mono=True)
F.text(440, 380, 'ASL = (2×3 + 3 + 4 + 5 + 6 + 7×2) / 9 = 4.22', 13, 'start', INK2, mono=True)
F.text(30, 356, '方框为失败结点：n 个结点有 n + 1 种失败情况', 12, 'start', MUTED)
