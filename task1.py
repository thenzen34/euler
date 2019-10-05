import time

start = time.time()  # Получаем начальное время в секундах от начала времен
'''
a = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
print(sum(a))
# 0.00016570091247558594
'''
sums = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sums += i

print(sums)
# 0.00024008750915527344

print(time.time() - start)  # Получаем конечное время
