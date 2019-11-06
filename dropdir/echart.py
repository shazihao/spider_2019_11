from pyecharts import Bar, Line, Overlap
#effect_scale=8顶端闪烁,要EffectScatter
att = ['重庆', '天津', '北京', '上海', '巴黎', '东京']
v3 = [126, 57, 57, 55, 15, 9]
# v4 = [1, 4, 3, 5, 2, 3]

bar = Bar("主要城市平均停电时间（单位：分钟）")
bar.add('bar', att, v3)
# line = Line()
# line.add('line', att, v4)

# overlap = Overlap()
# bar.add(bar)
# overlap.add(line)
bar.show_config()
bar.render('./柱形图-折线图.html')