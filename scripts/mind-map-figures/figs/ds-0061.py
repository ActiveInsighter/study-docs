LABEL = '完全二叉树：编号与满二叉树一一对应'
F = Fig(600, 300, '完全二叉树（n = 12）')
def T(i, n=12):
    if i > n: return None
    l, r = T(2 * i), T(2 * i + 1)
    if l is None and r is None: return str(i)
    return (str(i), [l, r] if r is not None else [l, None])
F.tree(28, 80, T(1), unit=34, levelh=56, r=14, size=12, tones={str(i): 'blue' for i in range(1, 13)})
F.text(300, 288, '只有最后一层可以不满，且结点都靠左排列', 12.5, color=MUTED)
