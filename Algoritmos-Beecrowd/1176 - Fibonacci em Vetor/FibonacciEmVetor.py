lista = []
a = 0
b = 1
soma = 0

for i in range (70):
        lista.append(a)
        soma = a+b
        a = b
        b = soma

n = int(input())
for i in range (n):
    v = int(input())
    print('Fib(%d) = %d' %(v,lista[v]))