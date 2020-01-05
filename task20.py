import math
import time

start = time.time()  # Получаем начальное время в секундах от начала времен

string_100_cat = math.factorial(100)
sums = 0
for x in str(string_100_cat):
    sums += int(x)

print(sums)

# 648
# 0.0001461505889892578

print(time.time() - start)  # Получаем конечное время
