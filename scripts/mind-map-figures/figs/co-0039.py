from common import dmac
LABEL = 'DMA 传送过程：设备写满 DR 后请求，DMAC 接管总线完成一次数据传送'
F = Fig(820, 430)
dmac(F, True)
F.text(410, 400, '① 设备把数据写入 DR　② DR 满后置位 DMA 请求触发器　③ 发 HRQ 请求总线　④ CPU 回 HLDA 交出总线', 11, color=MUTED)
F.text(410, 420, '⑤ DMAC 接管总线传送一个字，并修改 AR、WC　⑥ WC 溢出 → 中断机构向 CPU 发中断请求，表示传送结束', 11, color=MUTED)
