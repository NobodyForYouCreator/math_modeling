n = int(input())
multps = []
for i in range(1, n+1):
    smth = []
    if n%i==0:
        for q in range(2, i+1):
            if i%q==0:
                smth.append(q)
        if len(smth)<=2:
            multps.append(i)
if 4 in multps:
    multps.remove(4)
if 25 in multps:
    multps.remove(25)
print(multps)