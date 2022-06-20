import random
import numpy as np


def main():
    data = []
    for i in range(21):
        x_i = -2 + 0.2 * i
        line = []
        for j in range(21):
            x_j = -2 + 0.2 * j
            v = (x_i, x_j)
            line.append(v)
        data.append(line)

    data = np.array(data)
    print(type(data))
    print(data)


def f(x1, x2):
    p = pow(x1, 2) + pow(x2, 2)
    if p <= 1:
        return 1
    else:
        return -1


def gaussainKernel(X, vertex, sigma):
    x_i, x_j = X
    x_1, x_2 = vertex
    euclidean = -(pow((x_i - x_1), 2) + pow((x_j - x_2), 2))

    return np.exp(euclidean / (2 * pow(sigma, 2)))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
