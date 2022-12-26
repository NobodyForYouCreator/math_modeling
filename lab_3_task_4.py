import numpy as np


def make_it(N, M):
    a = np.zeros((N, M))

    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                a[i, j] = np.sin(N * (i + 1) + M * (j + 1))
            else:
                a[i, j] = np.sin(N * i + M * j)
    for i in range(len(a)):
        for k, j in enumerate(a[i]):
            if j < 0:
                a[i][k] = 0

    return a
