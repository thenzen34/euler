import time

start = time.time()  # Получаем начальное время в секундах от начала времен

in_file = 'task13.data'

f = open(in_file, 'r')
sums = sum([int(line) for line in f])
f.close()

print(str(sums)[0:10])
# 5537376230390876637302048746832985971773659831892672
# 5537376230

print(time.time() - start)  # Получаем конечное время
