n = int(input())

lista = []

cont = 0

lista = input().split()

for i in range(n):
    if lista[i] == "1":
        cont+= 1
print(cont)

#for i in range (n):
#    v = int(input())
#    lista.append(v)

#for i in range (n):
#    if lista[i] == 1:
#        cont+= 1
#print(cont)