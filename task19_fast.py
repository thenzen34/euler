import time

start = time.time()  # Получаем начальное время в секундах от начала времен

months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 0
dow = 1  # понедельник
day_in_1900 = 365
dow += day_in_1900 % 7

for y in range(1901, 2001):
    months[1] = 29 if (y % 100 == 0 and y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) else 28
    for m in months:
        dow += m % 7  # смещение дня на первое число
        dow %= 7  # текущий день недели
        if dow == 0:  # воскресение
            cnt += 1
print(cnt)
print(time.time() - start)  # Получаем конечное время
