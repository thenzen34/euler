import time

start = time.time()  # Получаем начальное время в секундах от начала времен


def isPalindrom(nmb):
    string = str(nmb)
    revers_nmb = int(string[::-1])
    if nmb == revers_nmb:
        return True
    return False


maxPalindrom = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        result = x * y
        if isPalindrom(result):
            if result > maxPalindrom:
                maxPalindrom = result

print(maxPalindrom)

# 906609
# 0.7896890640258789

print(time.time() - start)  # Получаем конечное время
