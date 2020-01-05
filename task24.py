# https://en.wikipedia.org/wiki/Factorial_number_system
# кол-во перестановок цифер длинной n = n!
import math
import time

start = time.time()  # Получаем начальное время в секундах от начала времен

# кол-во совершенных словарных перестановок
fac = [math.factorial(x) for x in range(10)]
# доступные элементы
digits = [x for x in range(10)]
result = []

n = 1000000 - 1
i = len(digits) - 1
while i >= 0:
    ix = n // fac[i]
    n %= fac[i]
    result.append(digits[ix])
    digits.pop(ix)
    i -= 1

print(result)

print(time.time() - start)  # Получаем конечное время
# [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
# 6.318092346191406e-05
