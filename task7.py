import time
import math

start = time.time()  # Получаем начальное время в секундах от начала времен


def isSimple(nmbr):
    for x in range(2, math.ceil(math.sqrt(nmbr))+1):
        if nmbr % x == 0:
            return False
    return True

nmbr = 13
cnt = 6

while cnt < 10001:
    nmbr += 2
    if isSimple(nmbr):
        cnt += 1

print(nmbr)

# 104743
# 0.3656938076019287

print(time.time() - start)  # Получаем конечное время
