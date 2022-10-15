a = int(input())
b = int(input())
c = int(input())

if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        tr = "равносторонний"
    elif a==c or a==b or c==b:
        tr = "равнобедренный"
    else:
        tr = "разносторонний"
    print(f"Существует, он {tr}")

else:
    print("Не существует")