maior = 0
posi = 0
for i in range(1, 101):
    x = int(input())
    if(x > maior):
        maior = x
        posi = i
print(maior)
print(posi)