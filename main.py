import random
import pandas
import matplotlib.pyplot as plt
from distribution import Distribution
from files import FileWrire

def main():
    count = 100
    # n = int(input("Введите количество испытаний: ")) #13
    # p = float(input("Введите значение вероятности: ")) #0.82
    n = 13
    p = 0.82

    if p < 0 or p > 1:
        raise Exception("Значение вероятности введено некорректно. Значение должно находится в промежутке [0; 1]")

    test_statistics = [0 for _ in range(n + 1)]

    d = Distribution(p, n)

    input_data = [random.random() for _ in range(count)]

    FileWrire.write_in_file("input/input_data.txt", "\n".join([str(element) for element in input_data]))

    for value in input_data:
        index = d.get_index_of_interval(value)
        test_statistics[index] += 1

    for i in range(len(test_statistics)):
        test_statistics[i] /= 100

    print(test_statistics)

    plt.bar([index for index in range(n+1)], test_statistics, 0.9)
    plt.title('Гистограмма распределения')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

main()