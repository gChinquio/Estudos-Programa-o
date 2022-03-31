from re import X


x = input().split()

a, b, c = x

a = int(a)
b = int(b)
c = int (c)
maior = 0
menor = 0
aux = 0
if(a > b and a > c):
    maior = a
    if(b > c):
        aux = b
        menor = c
    else:
        aux = c
        menor = b

if(b > a and b > c):
    maior = b
    if(a > c):
        aux = a
        menor = c
    else:
        aux = c
        menor = a
if(c > a and c > b):
    maior = c
    if(b > a):
        aux = b
        menor = a
    else:
        aux = a
        menor = b

print(menor)
print(aux)
print(maior)
print()
print(a)
print(b)
print(c)