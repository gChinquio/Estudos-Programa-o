x = input().split()
n, m = x

n = int(n)
m = int(m)
lista = []
listaV = []
listaD = []

for i in range (n):  
    p = input().split()
    for pro in p:
        # dados: n+l - indice [0][1], [0][1]
        if pro[1] == 'V':
            listaV.append(pro)
        elif pro[1] == 'D':
            listaD.append(pro)
    
listaV.sort(reverse=True)
listaD.sort(reverse=True)

for i in range (len(listaV)):
    print(listaV[i])
for i in range (len(listaD)):
    print(listaD[i])