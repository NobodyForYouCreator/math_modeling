import numpy as np
from lab_3_task_4 import make_it

c1 = 2
c2 = 3
N = 4
M = 5
a = make_it(N, M)

print(a)
for i in range(len(a)):
    for l in range(len(a[i])):
        if l == c1:
            a[i][c1], a[i][c2] = a[i][c2], a[i][c1]
print(a)