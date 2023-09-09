import math

class Distribution:
    # События
    def __init__(self, p, n):
        self.__current_sum = 0
        self.__points = []
        self.__m = 0
        self.__p = p
        self.__n = n
        self.__points.append(self.__binomial_distribution())
        self.__current_sum = sum(self.__points)

    def __str__(self):
        return str(self.__points)

    # Методы
    # 
    def get_current_sum(self):
        return self.__current_sum

    # 
    def get_last(self):
        return self.__points[self.__m]

    # 
    def get_index_of_interval(self, gamma):
        for index, value in enumerate(self.__points):
            if gamma <= value:
                return index

        # Если не удалось попасть в текущих инетравале
        while self.__m < self.__n:
            self.__add_point()
            if gamma <= self.get_last():
                return self.__m

    # 
    def __add_point(self):
        if self.__m >= self.__n:
            return
        else:
            new_point = (((self.__n - self.__m) * self.__p) / ((self.__m + 1) * (1 - self.__p))) * self.get_last()
            self.__current_sum += new_point
            self.__points.append(self.__current_sum)
            self.__m += 1

    # 
    def __binomial_distribution(self):
        return math.comb(self.__n, self.__m) * (self.__p**self.__m) * ((1 - self.__p)**(self.__n - self.__m))

