import time

start = time.time()  # Получаем начальное время в секундах от начала времен

result = 0
diff = 10
p = diff
while result == 0:
    for n in range(1, p):
        for m in range(n, p + 1):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if a + b + c == 1000:
                result = a * b * c
                break
        if result > 0:
            break
    p += diff
print(result)

# 31875000
# 0.0001308917999267578

print(time.time() - start)  # Получаем конечное время
