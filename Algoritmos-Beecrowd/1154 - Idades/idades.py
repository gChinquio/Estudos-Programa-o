cont = 0
soma = 0
while (1):
    x = int(input())
    if(x > 0):
        cont = cont +1
        soma = soma + x
    else:
        break
print(str("{:0.2f}".format(soma/cont)))