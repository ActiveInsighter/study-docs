LABEL = '二叉排序树的平均查找长度（查找成功）'
F = Fig(860, 400, '二叉排序树 ASL（查找成功）')
nil = False
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
F.tree(20, 90, uniq(T(good)), unit=44, levelh=56, r=15, size=12, mono=True, tones={k: 'blue' for k in ['50','26','66','21','30','60','70','68']})
F.tree(430, 90, uniq(T(bad)), unit=40, levelh=40, r=14, size=11, mono=True, tones={k: 'blue' for k in ['50','26','66','21','30','60','70','68']})
F.text(30, 380, 'ASL = (1×1 + 2×2 + 3×4 + 4×1) / 8 = 2.625', 13.5, 'start', INK2, mono=True)
F.text(440, 380, 'ASL = (1+2×2+3+4+5+6+7) / 8 = 3.75', 13.5, 'start', INK2, mono=True)
F.text(30, 356, '查找长度：查找时与关键字比较的次数', 12, 'start', MUTED)
