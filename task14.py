import time

start = time.time()  # Получаем начальное время в секундах от начала времен


def get_collatz(n):
    qty = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        qty += 1
    return qty


'''
def get_collatz(n, qty=1):
    if n == 1:
        return qty
    if n % 2 == 0:
        return get_collatz(n // 2, qty + 1)
    else:
        return get_collatz(3 * n + 1, qty + 1)
'''
'''
lengths = [get_collatz(x) for x in range(13, 1000000)]

max_length = max(lengths)
ix = lengths.index(max_length) + 13

print(max_length, ix)
'''
# 525 837799
# 25.5299334526062

n = 0
a = 0
for i in range(13, 1000000):
    c = get_collatz(i)
    if c > n:
        a, n = i, c
print(a, n)

print(time.time() - start)  # Получаем конечное время
