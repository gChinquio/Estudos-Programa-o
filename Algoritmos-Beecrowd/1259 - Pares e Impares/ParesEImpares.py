n = int(input())
lista = []
listaPar = []
listaImpar = []
for i in range(n):
    v = int(input())
    if(v%2 == 0):
        listaPar.append(v)
    else:
        listaImpar.append(v)    

listaPar.sort()
#print(listaPar)
listaImpar.sort(reverse=True)
#print(listaImpar)
lista = listaPar+listaImpar
for i in range(n):
    print(lista[i])
