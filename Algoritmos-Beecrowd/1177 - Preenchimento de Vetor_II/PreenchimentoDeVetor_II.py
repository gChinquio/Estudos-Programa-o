t = int(input())
lista = []
cont = 0
for i in range(1000):
    lista.append(cont)
    cont = cont+1
    if(cont == t):
        cont = 0

for i in range(1000):
    print('N[%d] = %d' %(i, lista[i]))