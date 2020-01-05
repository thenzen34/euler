import time

start = time.time()  # Получаем начальное время в секундах от начала времен


class Answer:
    months_day = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    def __init__(self):
        self.c_day = 7
        self.c_month = 1
        self.c_year = 1900

    def prev_sunday(self):
        self.c_day -= 7
        while self.c_day < 1:
            self.c_month -= 1
            while self.c_month < 1:
                self.c_month += 12
                self.c_year -= 1
            self.c_day += self.get_cur_month_day()

    def next_sunday(self):
        self.c_day += 7
        while self.c_day > self.get_cur_month_day():
            self.c_day -= self.get_cur_month_day()
            self.c_month += 1
            while self.c_month > 12:
                self.c_month -= 12
                self.c_year += 1

    def is_cur_year_visok(self):
        if self.c_year % 100 == 0:
            return self.c_year % 400 == 0
        return self.c_year % 4 == 0

    def get_cur_month_day(self):
        if self.c_month != 2:
            return self.months_day[self.c_month]
        elif self.is_cur_year_visok():
            return 29
        else:
            return 28

    def goto_first_sunday_1901(self):
        while self.c_year < 1901:
            self.next_sunday()

    def get_count_all_sunday_2001(self):
        cnt = 0
        while self.c_year < 2001:
            if self.c_day == 1:
                self.next_sunday()
            while self.c_day != 1:
                self.next_sunday()
            cnt += 1
        else:
            while self.c_day != 1:
                self.prev_sunday()
            cnt -= 1

        return cnt

    def __str__(self):
        return '{:02d}-{:02d}-{:02d}'.format(self.c_day, self.c_month, self.c_year)


obj = Answer()
obj.goto_first_sunday_1901()
print(obj.get_count_all_sunday_2001())
print(obj)
print(time.time() - start)  # Получаем конечное время

# 5217
# 31-12-2000
# 0.005741119384765625
