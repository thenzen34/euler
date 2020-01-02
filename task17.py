import time

start = time.time()  # Получаем начальное время в секундах от начала времен


class Nums:
    data = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        15: 'fifteen',
        18: 'eighteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }

    @staticmethod
    def gen_num(n):
        string = str(n)
        if __class__.data.get(n, False):
            return __class__.data[n]
        elif n < 20:
            return __class__.data[int(string[1])] + 'teen'
        elif n < 100:
            tmp = n - int(string[1])
            return __class__.data[tmp] + '-' + __class__.data[int(string[1])]
        elif n < 1000:
            if string[1:3] == '00':
                return __class__.data[int(string[0])] + ' hundred'
            else:
                return __class__.data[int(string[0])] + ' hundred and ' + __class__.gen_num(int(string[1:3]))
        elif n < 1000000:
            length = len(string)
            return __class__.gen_num(int(string[0:length - 3])) + ' thousand ' + __class__.gen_num(
                int(string[length - 3:length]))

    @staticmethod
    def cut_gen_num(n):
        return __class__.gen_num(n).replace(' ', '').replace('-', '')


s = 0
for i in range(1, 1001):
    s += len(Nums.cut_gen_num(i))
print(s)

print(time.time() - start)  # Получаем конечное время
