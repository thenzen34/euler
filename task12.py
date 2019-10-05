import math
import time

start = time.time()  # Получаем начальное время в секундах от начала времен


def is_square(nmbr):
    x = math.ceil(math.sqrt(nmbr))
    return x ** 2 == nmbr


def get_divisions(nmbr):
    lst = [1, nmbr]
    n = 2
    # for x in range(2, math.ceil(nmbr / 2) + 1):
    for x in range(2, math.ceil(math.sqrt(nmbr))):
        if nmbr % x == 0:
            if is_square(x):
                n -= 1
            else:
                n += 2

            lst.append(x)
            lst.append(nmbr // x)

    # print(n, nmbr, lst)
    return n  # len(lst)


i = 1
sums = 0

while True:
    sums += i  # текущий треугольник
    if get_divisions(sums) > 500:
        break
    i += 1

print(sums)
# 76576500
# 7.311601400375366

print(time.time() - start)  # Получаем конечное время
