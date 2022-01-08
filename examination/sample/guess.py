from random import randint

print('——————猜数字游戏——————')
random_num = randint(1, 10)
n = int(input('请输入1~10之间的任意一个整数:\n'))
while n != random_num:
    if n == 0:
        break
    if n < random_num:
        print('太小，请重新输入:')
    else:
        print('太大，请重新输入:')
    n = int(input())
if n == random_num:
    print('恭喜你，你赢了，猜中的数字是: ', n)
print('———————游戏结束———————')
