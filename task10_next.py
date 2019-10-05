import time

start = time.time()  # Получаем начальное время в секундах от начала времен

n = 2000000
t = list(range(n + 1))
t[1] = 0
lst = []

i = 2
while i < n:
    if t[i] != 0:
        lst.append(t[i])
        for x in range(i, n + 1, i):
            t[x] = 0
    i += 1

print(sum(lst))

# 142913828922
# 1.5520775318145752

print(time.time() - start)  # Получаем конечное время
