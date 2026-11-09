from common import frame
LABEL = 'PPP 帧格式：F(7E) A(FF) C(03) 协议 信息 FCS F(7E)'
F = Fig(780, 300, 'PPP 帧格式（面向字节）')
F.box(390, 54, 140, 30, 'IP 数据报', 'green', 12, 0); F.line(460, 86, 460, 118, INK2, 1.2, arrow='end')
end = frame(F, 70, 120, [('F\n7E', 50, 'blue', 1), ('A\nFF', 50, 'blue', 1), ('C\n03', 50, 'blue', 1), ('协议', 80, 'blue', 2), ('信息部分', 200, 'green', '不超过 1500 B'), ('FCS', 80, 'blue', 2), ('F\n7E', 50, 'blue', 1)], 40)
F.brace(70, 300, 112, '首部', down=False); F.brace(500, 630, 112, '尾部', down=False)
F.text(642, 137, '← 定界符 0111 1110', 10, 'start', INK2, mono=True)
F.text(70, 186, '先发送 →', 11, 'start', INK2); F.text(132, 186, 'A、C 字段无实际用途', 11, 'start', ACCENT['red'])
F.text(600, 186, 'FCS：CRC 循环冗余检验（16 bit）', 11, color=ACCENT['red'])
F.text(400, 222, 'PPP 帧', 11.5, color=INK2, halo=True); F.line(70, 222, 680, 222, INK2, 1, arrow='both')
F.text(400, 248, '信息部分中若出现 7E/7D，插入转义字符 7D（字节填充）；比特同步时用零比特填充（连续 5 个 1 后插 0）', 11, color=ACCENT['green'])
F.text(400, 276, 'PPP 不使用 CSMA/CD，因此没有最短帧长限制', 11, color=MUTED)
