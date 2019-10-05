import time

start = time.time()  # Получаем начальное время в секундах от начала времен

result = 0
while result == 0:
    for n in range(1, 1000):
        for m in range(n, 1000+1):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if a + b + c == 1000:
                result = a * b * c
                break
        if result > 0:
            break

print(result)

# 31875000
# 0.0030775070190429688

print(time.time() - start)  # Получаем конечное время
