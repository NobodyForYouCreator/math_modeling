n = int(input())
a, b = 0, 1
end = ", "
for i in range(n):
    if i+1 == n:
        end = "."
    print(b, sep=", ", end=end)
    a, b = b, a+b