LABEL = '满二叉树：每层结点数都达到最大'
F = Fig(600, 280, '满二叉树（h = 4，n = 2⁴ − 1 = 15）')
def T(i):
    return str(i) if i >= 8 else (str(i), [T(2 * i), T(2 * i + 1)])
F.tree(28, 80, T(1), unit=34, levelh=56, r=14, size=12, tones={str(i): 'blue' for i in range(1, 16)})
F.text(300, 264, '按层序从 1 开始编号：结点 i 的孩子为 2i、2i + 1', 12.5, color=MUTED)
