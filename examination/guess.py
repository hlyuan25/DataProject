import random

print('——————猜数字游戏——————')
x = int(input('请输入1~10之间的任意一个整数：\n'))
target = random.randint(1, 10)
flag = True
while flag:
    if x == 0:
        break
    elif x > target:
        x = int(input('太小，请重新输入：\n'))
    elif x < target:
        x = int(input('太小，请重新输入：\n'))
    else:
        print('恭喜你，你赢了，猜中的数字是：%d' % target)
        flag = False

print('———————游戏结束———————')
