import numpy as np

g = 9.87
x0 = 0
y0 = 0
alpha = 30
V = 15
V0x = V*np.sin(np.pi / 180 * alpha)
V0y = V*np.cos(np.pi / 180 * alpha)

t = np.arange(0, 5, 0.1)
x = x0 + V0x * t
y = y0 + V0y * t - g * t**2 / 2

coords_time = np.zeros((len(t), 3))
for i in range(len(t)):
    coords_time[i, 0] = t[i]
    coords_time[i, 1] = x[i]
    coords_time[i, 2] = y[i]

print(coords_time)
