import time

# https://en.wikipedia.org/wiki/Full_reptend_prime

start = time.time()  # Получаем начальное время в секундах от начала времен
'''
1/2	    = 	0.5
1/3	    = 	0.(3)
1/4	    = 	0.25
1/5	    = 	0.2
1/6	    = 	0.1(6)
1/7	    = 	0.(142857)
1/8 	= 	0.125
1/9     = 	0.(1)
1/10	= 	0.1
'''


def get_rep_part(in_d):
    a = 1
    # d = 7
    result = []
    repeat_part = []

    i = 100

    base = 1
    length_base = 0

    while base < in_d:
        base *= 10
        length_base += 1

    while True:
        a *= base
        t = a // in_d
        if result.count(t) > 0:
            repeat = True
            break
        a %= in_d
        result.append(t)
        i -= 1

    if repeat:
        start_part = result.index(t)
        end_part = len(result)
        repeat_part = result[start_part:end_part]
        result = result[0:start_part]
    return length_base, result, repeat_part


d = mx = len_base = 0
mx_res = []
mx_rep_part = []
for x in range(1, 1000):
    len_base, tmp, rep_part = get_rep_part(x)
    length = len(rep_part)
    if length > mx:
        mx = length
        d = x
        mx_res = tmp
        mx_rep_part = rep_part

print(d)

# len_base, mx_res, mx_rep_part = get_rep_part(13)

format_str = ':0{}d'.format(len_base)
format_str = '{' + format_str + '}'
print('0.' + ''.join([format_str.format(x) for x in mx_res]) + '(' + ''.join(
    [format_str.format(x) for x in mx_rep_part]) + ')')

print(time.time() - start)  # Получаем конечное время
