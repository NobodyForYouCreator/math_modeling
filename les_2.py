import matplotlib.pyplot as plt
import numpy as np

def parabola(x_min, x_max, N, *args):
    x = np.arange(x_min, x_max, N)
    y = args[0]*x**2+args[1]*x+args[2]
    plt.plot(x, y, color="black", marker=".", ms=0.2)
    plt.xlabel('coord: x')
    plt.ylabel('coord: y')
    plt.grid()
    plt.title("parabola")
    plt.axis('equal')
    plt.show()

parabola(-20, 10, 0.1, 1, 3, 6)