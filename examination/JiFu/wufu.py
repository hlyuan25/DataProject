from examination.JiFu import ji_fu, five_blessings, print_all

print('——————开始集福啦——————')

while not five_blessings():
    if input('按下<Enter>键获取五福') == '':
        fu = ji_fu()
        print('获取到：%s' % fu)
        print('当前拥有的福：')
        print_all()

print('恭喜您集成五福！！！')
