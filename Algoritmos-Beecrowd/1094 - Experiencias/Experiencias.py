n = int(input())
qtd = 0
tipo = ''
totalC = 0
totalR = 0
totalS = 0
total = 0
for i in range (0, n):
    x = input().split()
    qtd, tipo = x
    qtd = int(qtd)

    if tipo == 'C':
        totalC += qtd
    elif tipo == 'R':
        totalR += qtd
    elif tipo == 'S':
        totalS +=qtd

total = totalC + totalR + totalS

print("Total: %d"% total, "cobaias")
print("Total de coelhos: %d"% totalC)
print("Total de ratos: %d"% totalR)
print("Total de sapos: %d"% totalS)
print(str("Percentual de coelhos: {:0.2f} %").format((totalC/total)*100))
print(str("Percentual de ratos: {:0.2f} %").format((totalR/total)*100))
print(str("Percentual de sapos: {:0.2f} %").format((totalS/total)*100))

#Percentual de coelhos: 31.52 %
#Percentual de ratos: 43.48 %
#Percentual de sapos: 25.00 %