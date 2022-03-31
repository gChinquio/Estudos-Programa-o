nome = input()
salariof = float(input())
#total de vendas efetuadas
tve = float(input())

total = salariof + (tve * 0.15)

print(str("TOTAL = ") + str("R$ {:0.2f}".format(total)))