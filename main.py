import random
import pandas
import matplotlib.pyplot as plt
from distribution import Distribution

def binomial_distribution(p, n, m):
    return math.comb(n, m) * (p**m) * ((1 - p)**(n-m))

def new_point(p, n, m):
    return (((n - m) * p) / ((m + 1) * (1 - p))) * binomial_distribution(p, n, m)

count = 100
# n = int(input("Введите количество испытаний: ")) #13
# p = float(input("Введите значение вероятности: ")) #0.82

n = 13
p = 0.82

if p < 0 or p > 1:
    raise Exception("Значение вероятности введено некорректно. Значение должно находится в промежутке [0; 1]")

test_statistics = [0 for _ in range(n + 1)]

d = Distribution(p, n)

for i in range(count):
    gamma = random.random()
    index = d.get_index_of_interval(gamma)
    test_statistics[index] += 1

for i in range(len(test_statistics)):
    test_statistics[i] /= 100

# data = pandas.Series(test_statistics)
print(test_statistics)

plt.bar([index for index in range(n+1)], test_statistics)
plt.title('Гистограмма распределения')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()