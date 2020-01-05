import math
import time

start = time.time()  # Получаем начальное время в секундах от начала времен

'''
class Factorials:
    data = []

    @staticmethod
    def get(nmbr):
        calc_f_cnt = len(__class__.data)  # посчитанные
        if calc_f_cnt < 1:
            result = 1
            calc_f_cnt = 1
            __class__.data.append(result)
        elif calc_f_cnt >= nmbr + 1:
            return __class__.data[nmbr]
        else:
            result = __class__.data[calc_f_cnt - 1]

        while calc_f_cnt <= nmbr:
            result *= calc_f_cnt
            calc_f_cnt += 1
            __class__.data.append(result)

        return result
'''


def cnt_sochet(cn, cm):
    return int(math.factorial(cn) / (math.factorial(cn - cm) * math.factorial(cm)))


# https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA_%D0%9F%D0%B0%D1%81%D0%BA%D0%B0%D0%BB%D1%8F
# треугольник паскаля
# https://oeis.org/
def calc_cnt(n):
    """
    p_start = 0, 0
    p_end = n, n

    variants = []
    variants.append(p_start)

    cnt = 0
    while len(variants) > 0:
        p_cur = variants.pop()
        if p_cur == p_end:
            cnt += 1
        x, y = p_cur
        if x < n:
            variants.append((x + 1, y))
        if y < n:
            variants.append((x, y + 1))
    return cnt
    """
    return cnt_sochet(2 * n, n + 1 - 1)


print(calc_cnt(20))

print(time.time() - start)  # Получаем конечное время
# 137846528820
# 5.745887756347656e-05
