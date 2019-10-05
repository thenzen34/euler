import time

start = time.time()  # Получаем начальное время в секундах от начала времен

last1 = 1
last2 = 2
nmb = 2
sums = 2

while last2 < 4000000:
    item = last2 + last1
    last1 = last2
    last2 = item
    if item % 2 == 0:
        sums += item

# 3.2901763916015625e-05

'''
f = [1, 2]
nmb = 2
sums = 2

while f[1] < 4000000:
    item = f[0] + f[1]
    f = [f[1], item]
    if item % 2 == 0:
        sums += item

# 3.552436828613281e-05
'''

# 4613732
# print(sums)

print(time.time() - start)  # Получаем конечное время
