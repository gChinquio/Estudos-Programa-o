cont = 0
soma = 0
for i in range(0,6):
    x = float(input())
    if(x > 0):
        soma = soma + x
        cont = cont + 1
print(cont, "valores positivos")
print(str("{:0.1f}".format(soma/cont)))