def validaNota(nota):
    if(nota >= 0 and nota <= 10):
        return 1
    else:
        return 0

#variavelglobal
notasVal = 2
nota1 = 0
nota2 = 0


while(notasVal > 0):
    if(notasVal > 0):
        nota = float(input())
        valida = validaNota(nota)

    if(valida == 1 and notasVal == 2):
        nota1 = nota
        notasVal = notasVal - 1
    elif(valida == 1 and notasVal == 1):
        nota2 = nota
        notasVal = notasVal - 1
    else:
        print("nota invalida")
    
print(str("media = {:0.2f}".format((nota1+nota2)/2)))