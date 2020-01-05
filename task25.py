import time

start = time.time()  # Получаем начальное время в секундах от начала времен
'''
data = {1: 1, 2: 1}


def get_fib(n):
    length = len(data)
    while n > length:
        data[length + 1] = data[length] + data[length - 1]
        length += 1

    return data[n]


print(get_fib(12), data)
'''

n = 12
last_fib = 89
cur_fib = 144

while len(str(cur_fib)) < 1000:
    last_fib, cur_fib = cur_fib, cur_fib + last_fib
    n += 1

print(n)


print(time.time() - start)  # Получаем конечное время
