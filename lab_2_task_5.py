a = int(input())
b = int(input())

if b == 0:
    print("Делитель не может быть равным нулю")
else:
    print("Делится" if a%b==0 else "Не делится")
    print(a//b, a%b if a%b!=0 else "")