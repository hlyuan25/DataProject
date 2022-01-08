print('——————身份证信息——————')
id_card = input('请输入身份证信息：')

year = id_card[6:10]
month = int(id_card[10:12])
day = int(id_card[12:14])
n = int(id_card[16])

if n % 2 == 0:
    gender = '女'
else:
    gender = '男'

print('您的生日是:\n')
print('%s年%s月%s日' % (year, month, day))
print('您的性别是：%s' % gender)
