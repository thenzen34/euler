import time

start = time.time()  # Получаем начальное время в секундах от начала времен

in_file = 'task22.data'


def get_score(s):
    letter_score = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                    'X': 24, 'Y': 25, 'Z': 26}
    score = 0
    for l in s:
        score += letter_score[l]
    return score


data = []
f = open(in_file, 'r')
for line in f:
    value = [x.replace('"', '') for x in line.split(',')]
    data += value
f.close()

data.sort()

scores = []
i = 1
for name in data:
    scores.append(get_score(name) * i)
    i += 1

print(sum(scores))

# 324536
# 0.013267755508422852

print(time.time() - start)  # Получаем конечное время
