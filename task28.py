import time

start = time.time()  # Получаем начальное время в секундах от начала времен

n = 1001
'''
sum = 1
i = n
k = n ** 2

while i > 1:
    for j in range(4):
        sum += k 
        k -= i - 1
    i -= 2
print(sum)
'''

sum = 1
i = n
k = n ** 2
while i > 1:
    sum += k * 4
    k -= i * 4 - 1
    i -= 2
print(sum)

print(time.time() - start)  # Получаем конечное время