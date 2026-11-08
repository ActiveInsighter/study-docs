from common import bus_slash
LABEL = '三态门：1 bit 控制信号决定输入是否送到输出'
F = Fig(420, 320)
F.items.append('<path d="M150 110L196 196H104Z" fill="#e8effc" stroke="#3b6fd4" stroke-width="1.6" stroke-linejoin="round"/>')
F.line(150, 270, 150, 198, INK2, 1.6, arrow='end'); bus_slash(F, 150, 236)
F.line(150, 110, 150, 46, INK2, 1.6, arrow='end'); bus_slash(F, 150, 80)
F.line(330, 160, 182, 160, ACCENT['blue'], 1.4, dash='5 4', arrow='end'); bus_slash(F, 260, 160, '1', vertical=False)
F.text(150, 32, '单个输出（n bit）', 13, color=ACCENT['red'], weight=600)
F.text(150, 296, '单个输入（n bit）', 13, color=ACCENT['red'], weight=600)
F.text(340, 140, '控制信号 1 bit', 13, 'end', ACCENT['blue'], 600)
F.text(340, 190, '有效：输出 = 输入\n无效：高阻态（断开）', 12, 'end', MUTED, lh=1.5)
