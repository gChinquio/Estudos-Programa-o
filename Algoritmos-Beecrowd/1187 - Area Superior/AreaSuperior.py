m = []
soma = 0
cIni = 1
CFim = 11
v = 0
cont = 0

op = input()

for i in range(12):#criação da matriz
    m.append([])

for i in range(12):#criação da matriz
    for j in range(12):
        v = float(input())
        m[i].append(v)
        [i].append(1)

for i in range(5):
    for j in range(cIni,CFim,1):
        soma = soma + m[i][j]
        cont += 1
    cIni += 1
    CFim -= 1

media = soma/cont

if(op == 'S'):
    print(str("{:0.1f}".format(soma)))
else:
    print(str("{:0.1f}".format(media)))