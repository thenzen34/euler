import time

start = time.time()  # Получаем начальное время в секундах от начала времен


def isFind(nmbr, divlst):
    for x in divlst:
        if nmbr % x > 0:
            return False
    return True


nmbr = 2520
divlst = [x for x in range(2, 20 + 1)]
step = 19

while not isFind(nmbr, [step]):
    nmbr += 1

while not isFind(nmbr, divlst):
    nmbr += step

print(nmbr)

# 232792560
# 6.0765910148620605

print(time.time() - start)  # Получаем конечное время
