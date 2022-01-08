import random

fu_dict = {
    0: '爱国福',
    1: '富强福',
    2: '和谐福',
    3: '友善福',
    4: '敬业福'
}

fu_storage = {
    '爱国福': 0,
    '富强福': 0,
    '和谐福': 0,
    '友善福': 0,
    '敬业福': 0,
}


def ji_fu():
    n = random.randint(0,4)
    fu = fu_dict.get(n)
    fu_storage[fu] = fu_storage.get(fu) + 1
    return fu


def five_blessings():
    full = True
    for i in fu_storage.values():
        if i == 0:
            full = False
            break
    return full


def print_all():
    for k, v in fu_storage.items():
        print('%s: %d' % (k, v))
