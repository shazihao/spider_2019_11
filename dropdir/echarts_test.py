from pyecharts import Bar, Line, Overlap,EffectScatter

att = ['重庆', '天津', '北京', '上海', '巴黎', '东京']
v3 = [126, 57, 57, 55, 15, 9]
v4 = [100, 45, 33, 52, 69, 80]

bar = Bar("柱形-折线")
# bar.add('bar', att, v3,area_color='#0AC4B6',item_color='#39B25A',liquid_color='#FFDB51',label_color='#FD793C')
bar.add('bar', att, v3,label_color=['#1CA261'])
line = Line()
line.add('line', att, v4)

es=EffectScatter()
es.add('',att,v4,effect_scale=8)

overlap = Overlap()
overlap.add(bar)
overlap.add(line)
overlap.add(es)
overlap.show_config()
overlap.render('./柱.html')