cAlcool = 0
cGasol = 0
cDisel = 0
while 1:

    x = int(input())
    if(x == 4):
        break
    elif(x == 1):
        cAlcool += 1
    elif(x == 2):
        cGasol += 1
    elif(x == 3):
        cDisel += 1

print("MUITO OBRIGADO")
print("Alcool:", cAlcool)
print("Gasolina:", cGasol)
print("Diesel:", cDisel)