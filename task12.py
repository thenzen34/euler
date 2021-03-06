import math
import time

start = time.time()  # Получаем начальное время в секундах от начала времен


def get_divisions(nmbr, self=True):
    lst = [1]
    n = 1
    if self:
        lst.append(nmbr)
        n += 1
    for x in range(2, math.ceil(math.sqrt(nmbr)) + 1):
        if nmbr % x == 0:
            if lst.count(x) == 0:
                lst.append(x)
                n += 1
            if nmbr // x != x:
                if lst.count(nmbr // x) == 0:
                    lst.append(nmbr // x)
                    n += 1

    c = lst.count(nmbr)
    if c > 0 and not self:
        lst.remove(nmbr)
        n -= c
    # print(n, nmbr, lst)
    return len(lst)


i = 1
sums = 0

while True:
    sums += i  # текущий треугольник
    if get_divisions(sums) > 500:
        break
    i += 1

print(sums)
# 76576500
# 7.100525856018066

print(time.time() - start)  # Получаем конечное время
