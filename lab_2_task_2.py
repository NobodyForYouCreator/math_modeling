a = int(input())
q = int(input())
n = int(input())

end = ", "
print(a, end=end)
for i in range(n):
    a*=q
    if i+1 == n:
        end = "."
    print(a, end=end)