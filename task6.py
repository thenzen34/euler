import time

start = time.time()  # Получаем начальное время в секундах от начала времен


sums_sqrt = 0
sums = 0
for x in range(1, 100+1):
    sums_sqrt += x*x
    sums += x

print(sums*sums - sums_sqrt)

# 25164150
# 4.792213439941406e-05

print(time.time() - start)  # Получаем конечное время
