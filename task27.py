def update_progress(progress):
    print('\r[{0:50s}] {1:.3f}%'.format('#' * int(progress * 50 / 100), progress), end='', flush=True)
    if progress >= 100:
        print()


import math
import time

start = time.time()  # Получаем начальное время в секундах от начала времен


def is_simple(nmbr):
    if nmbr < 0:
        return False
    for x in range(2, math.ceil(math.sqrt(nmbr)) + 1):
        if nmbr % x == 0:
            return False
    return True


def func(a, b, n):
    return n ** 2 + a * n + b


max_a = max_b = max_n = 0
for b in range(-1000, 1000 + 1):
    for a in range(-b - 1, 1000):  # n^2 + an + b >=0 !!! ==>> a >= -b
        n = 0
        while is_simple(func(a, b, n)):
            n += 1

        if max_n < n:
            max_a, max_b, max_n = a, b, n

    update_progress(((b + 1000) / 2000) * 100)

print(max_a, max_b, max_n, max_a * max_b)
print(time.time() - start)  # Получаем конечное время
