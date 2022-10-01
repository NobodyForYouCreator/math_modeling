from math import sqrt


def first_opr(x):
  return (sqrt(x**3) / (x**3 + 3 / x)) * (
    4 * x**7 - x**5) + 80 * sqrt(27 * x**4 + 12 * x**3 - 5 * x**2 + 10)


def second_opr(x):
  return ((3 % 2) + ((16.7 * 4.32) // 1)) / (14.5 + (31 % 12) - (x**3.4) / 1)


x = 3
print(first_opr(x), second_opr(x))
