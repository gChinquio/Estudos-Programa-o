x = int(input())
y = int(input())

maior = 0
menor = 0
soma = 0

if(y > x):
    maior = y
    menor = x
else:
    maior = x
    menor = y

for i in range (menor, maior+1):
    if(i%13 > 0):
        soma += i

print(soma)