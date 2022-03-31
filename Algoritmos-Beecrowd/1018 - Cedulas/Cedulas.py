n = int(input())

#notas100 = 0
#notas50 = 0
#notas20 = 0
#notas10 = 0
#notas5 = 0
#notas2 = 0
#notas1 = 0
#resto100 = 0
#resto50 = 0
#resto20 = 0
#resto10 = 0
#resto5 = 0
#resto2 = 0
#rest1 = 0

resto = 0


#notas100 = n/100
#resto100 = n%100

#notas50 = resto100/50
#resto50 = resto100%50

#notas20 = resto50/20
#resto20 = resto50%20

#notas10 = resto20/10
#resto10 = resto20%10

#notas5 = resto10/5
#resto5 = resto10%5

#notas2 = resto5/2
#resto2 = resto5%2

#notas1 = resto2/1
#resto1 = resto2%1
print(n)
print("{} nota(s) de R$ 100,00".format(int(n/100)))
resto = n%100
print("{} nota(s) de R$ 50,00".format(int(resto/50)))
resto = resto%50
print("{} nota(s) de R$ 20,00".format(int(resto/20)))
resto = resto%20
print("{} nota(s) de R$ 10,00".format(int(resto/10)))
resto = resto%10
print("{} nota(s) de R$ 5,00".format(int(resto/5)))
resto = resto%5
print("{} nota(s) de R$ 2,00".format(int(resto/2)))
resto = resto%2
print("{} nota(s) de R$ 1,00".format(int(resto/1)))
