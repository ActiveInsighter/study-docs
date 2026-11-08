from common import threads_model
LABEL = '多线程模型：多对一、一对一、多对多'
F = Fig(760, 300, '多线程模型')
threads_model(F, 'user', 20, 0, '多对一模型')
threads_model(F, 'kernel', 270, 0, '一对一模型')
threads_model(F, 'combo', 520, 0, '多对多模型')
F.rect(16, 66, 728, 140, 'none', ACCENT['red'], 1.3, 8, dash='6 4')
F.text(380, 290, '红框：用户级线程到内核级线程的映射关系', 11.5, color=MUTED)
