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
    return lst


def d(n):
    lst = get_divisions(n, False)
    # print(lst)
    return sum(lst)


def gen_friendlys(n):
    lst = []
    for x in range(1, n):
        tmp = d(x)
        if tmp != x and d(tmp) == x:
            lst.append(x)

    return lst


res = gen_friendlys(10000)
print(len(res), sum(res))

print(time.time() - start)  # Получаем конечное время
