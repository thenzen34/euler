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


abundant_numbers = []
max_n = 28123
length = 0
all_sums = {}
all_2abundant = []
for i in range(1, max_n + 1):  # 28123
    # print(i, length)
    if all_sums.get(i, 0) == 0:  # если вариант не возможен
        all_2abundant.append(i)
    if sum(get_divisions(i, False)) > i:  # если избыточное
        abundant_numbers.append(i)  # добавляем
        for j in abundant_numbers:  # добавляем возможные суммы
            if max_n >= j + i and all_sums.get(j + i, 0) == 0:
                all_sums[j + i] = j + i
                length += 1
# print(all_sums, abundant_numbers)
# print(all_sums, all_2abundant, abundant_numbers, sum(all_2abundant))
print(sum(all_2abundant))


# 4179871
# 6.770277976989746

print(time.time() - start)  # Получаем конечное время
