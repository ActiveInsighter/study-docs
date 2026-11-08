from common import frame
LABEL = 'HDLC 的帧格式：标志、地址、控制、信息、FCS、标志'
F = Fig(760, 240, 'HDLC 的帧格式')
frame(F, 60, 90, [('标志 F', 80, 'blue', 8), ('地址 A', 80, 'blue', 8), ('控制 C', 80, 'blue', 8), ('信息 Info', 220, 'green', '可变'), ('帧检验序列 FCS', 140, 'blue', 16), ('标志 F', 80, 'blue', 8)])
F.text(40, 82, '比特数', 11, 'end', MUTED)
F.text(100, 144, '0111 1110', 11, color=ACCENT['blue'], mono=True); F.text(680, 144, '0111 1110', 11, color=ACCENT['blue'], mono=True)
F.line(140, 160, 600, 160, INK2, 1, arrow='both'); F.text(370, 176, 'FCS 检验区间', 11, color=INK2, halo=True)
F.line(140, 196, 680, 196, INK2, 1, arrow='both'); F.text(410, 212, '透明传输区间（零比特填充）', 11, color=INK2, halo=True)
F.text(140, 62, '非平衡：从站地址；平衡：应答站地址', 10.5, color=ACCENT['blue']); F.text(300, 62, '无编号、监督、信息帧', 10.5, 'start', ACCENT['green'])
