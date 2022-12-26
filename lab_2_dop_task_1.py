import math
a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c
x2 = ""
if D < 0:
    print("Корней нет")
else:
    x1 = (-1*b+D**(1/2))/(2*a)
    if D != 0:
        x2 = (-1*b-D**(1/2))/(2*a)
    print(x1, x2)