import time
import math

start = time.time()  # Получаем начальное время в секундах от начала времен


def isSimple(nmbr):
    for x in range(2, math.ceil(math.sqrt(nmbr))+1):
        if nmbr % x == 0:
            return False
    return True

nmbr = 7
cnt = 4
sums = 17

while nmbr < 2000000:
    nmbr += 2
    if isSimple(nmbr):
        sums += nmbr

print(sums)

# 142913828922
# 23.75131392478943

print(time.time() - start)  # Получаем конечное время
