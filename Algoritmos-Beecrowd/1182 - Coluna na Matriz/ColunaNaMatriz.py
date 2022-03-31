c = int(input())
op = input()

matriz = []#linhas
soma = 0
media = 0

for i in range(12):
    matriz.append([])#criando as colunas [linha[colunas]]


for i in range(12):
    for j in range(12):
        v = float(input())
        matriz[i].append(v)

for k in range (12):
    soma = soma + matriz[k][c]
    
media = soma/12
if('S' == op):
    print(soma)
else:
    print(str("{:0.1f}").format(media))