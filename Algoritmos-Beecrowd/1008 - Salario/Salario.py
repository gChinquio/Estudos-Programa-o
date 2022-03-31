#numero do funcionario
nfunc = int(input())
#qtd horas trabalhadas
qth = int(input())
#valor de horas trabalhadas
vht = float(input())

salario = qth * vht

print(str("NUMBER = ") + str(nfunc))
print(str("SALARY = U$ ") + str("{:0.2f}".format(salario)))