import time

start = time.time()  # Получаем начальное время в секундах от начала времен

in_file = 'task67.data'

data = []
f = open(in_file, 'r')
for line in f:
    value = [int(x) for x in line.split()]
    data.append(value)
f.close()

n = len(data)
sums = [[data[y][x] for x in range(y + 1)] for y in range(n)]

for y in range(n-2, -2, -1):
    for x in range(0, y + 1):
        sums[y][x] += max(sums[y + 1][x], sums[y + 1][x + 1])

y = 0
print(sums[0][0])

values = {0: sums[0][0]}


def color_print(string):
    print('\x1b[32m' + string + '\x1b[0m', end=' ')


steps = {x: 0 for x in range(n)}
while y != n and len(values) > 0:
    x = max(values, key=lambda key: values[key])
    steps[y] = x
    y += 1
    # print(x, y)
    values = {}
    if y < n:
        if x >= 0:
            values[x + 1] = sums[y][x + 1]
            # print('\t', values, 1)
        if x <= y:
            values[x] = sums[y][x]
            # print('\t', values, 2)
steps[0] = 0

for y in range(n):
    line = data[y]
    for ix in range(len(line)):
        v = line[ix]
        if steps[y] == ix:
            color_print("{:02d}".format(v))
        else:
            print("{:02d}".format(v), end=' ')
    print('')

print(time.time() - start)  # Получаем конечное время
