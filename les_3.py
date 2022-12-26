from matplotlib import pyplot as plt
import numpy as np


def ellipse(x_max, x_min, N, *args):
    x = np.arange(-2 * args[0], 2 * args[0], N)
    y = np.arange(-2 * args[1], 2 * args[1], N)
    X, Y = np.meshgrid(x, y)

    fxy = (X/args[0]) ** 2 - (Y/args[1]) ** 2 - 1

    plt.contour(X, Y, fxy, levels = [0])

    plt.show()

ellipse(4, -4, 0.01, 4, 7**0.5)