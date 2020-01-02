import time

start = time.time()  # Получаем начальное время в секундах от начала времен

string = str(2 ** 1000)

sums = sum([int(x) for x in string])

print(sums)

print(time.time() - start)  # Получаем конечное время
