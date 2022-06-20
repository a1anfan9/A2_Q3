import random
import numpy as np


def main():
    data = []
    for i in range(21):
        x_i = -2 + 0.2 * i
        for j in range(21):
            x_j = -2 + 0.2 * j
            v = (x_i, x_j)
            data.append(v)

    data = np.array(data)
    print(len(data))
    # print(data)

    sigma = 0.2

    G_ = G(data, sigma)
    G_intermediate = np.matmul(G_, np.transpose(G_))
    G_plus = np.matmul(np.power(G_intermediate, -1), np.transpose(G_))
    print(G_plus.shape)    
    print(G_plus)




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

def G(data, sigma):
    G = []
    for v in data:
        line = []
        for x in data:
            g = gaussainKernel(x, v, sigma)
            line.append(g)
        G.append(line)
    G = np.array(G)
    print(G.shape)

    return G







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
