x = int(input())
y = int(input())

maior = 0
menor = 0
if(x > y):
    maior = x
    menor = y
else:
    maior = y
    menor = x

soma = 0

for i in range (menor+1, maior,1):
    if(i%2 > 0) or (i%2 < 0):
        soma = soma + i
print(soma)