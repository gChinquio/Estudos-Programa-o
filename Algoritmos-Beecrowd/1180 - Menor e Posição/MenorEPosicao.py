x = int(input())

v = []

valor = input().split()
dmenor = int(valor[0])
posi = 0

for i in range(0, x):
    #dado = int(input())    
    v.append(int(valor[i]))
    #v.insert(i,v)

for i in range (0, x):
    if(v[i] < dmenor or v[i] == dmenor):
        dmenor = v[i]
        posi = i

print("Menor valor:", dmenor)
print("Posicao:", posi)