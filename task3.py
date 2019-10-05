import time
import math

start = time.time()  # Получаем начальное время в секундах от начала времен


def issimple(nmbr, divlist):
    for x in divlist:
        if nmbr % x == 0:
            return False

    divlist.append(nmbr)
    return True


nmbr = 600851475143
maxdiv = 0
divlist = []
for x in range(3, math.ceil(math.sqrt(nmbr)), 2):
    if nmbr % x == 0 and issimple(x, divlist):
        if x > maxdiv:
            maxdiv = x

print(maxdiv)
# 6857
# 0.09866189956665039
print(time.time() - start)  # Получаем конечное время
