import random


def Great_lotto(n):
    for _ in range(n):
        a = random.sample(range(1, 36), 5)
        b = random.sample(range(1, 13), 2)
        a.sort()
        b.sort()
        for i in range(len(a)):
            if a[i] < 10:
                a[i] = str(a[i]).zfill(2)
        for i in range(len(b)):
            if b[i] < 10:
                b[i] = str(b[i]).zfill(2)
        print('%s %s %s %s %s   %s %s' % (a[0], a[1], a[2], a[3], a[4], b[0], b[1]))