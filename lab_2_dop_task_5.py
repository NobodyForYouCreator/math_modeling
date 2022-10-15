n = int(input())
i=2
multps = []
while i<=n:
    while n%i==0:
        multps.append(str(int(i)))
        n/=i
    i+=1
if n>1:
    multps.append(str(int(n)))
print(", ".join(set(multps)))