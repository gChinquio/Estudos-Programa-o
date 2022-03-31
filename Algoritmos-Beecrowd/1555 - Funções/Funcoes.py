n = int(input())

def funcaoRafael(x,y):
    resultado = pow((3*x),2) + pow(y,2)
    return resultado

def funcaoBeto(x, y):
    resultado = (2*(pow(x,2))) + pow((5*y),2)
    return resultado

def funcaoCarlos(x, y):
    resultado = (-100*x) + pow(y,3)
    return resultado

for i in range(n):
    v = input().split()
    x, y = v
    x = int(x)
    y = int(y)

    resultRafa = funcaoRafael(x, y)
    resultBeto = funcaoBeto(x, y)
    resultCarlos = funcaoCarlos(x, y)

    if(resultRafa > resultBeto and resultRafa > resultCarlos):
        print("Rafael ganhou")
    elif(resultBeto > resultRafa and resultBeto > resultCarlos):
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
