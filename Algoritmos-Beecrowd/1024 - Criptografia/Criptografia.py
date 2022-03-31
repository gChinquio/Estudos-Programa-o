#def segundaPassagem(palavra):    
#    tamanho = len(palavra)-1
#    textoc = []
#    for i in range (0, len(palavra)):
#        textoc[i] = palavra[tamanho]
#        tamanho -= 1
#    return textoc

n = int(input())

for i in range(0, n):
    texto = input()
    textoCripto = ''
    #primeira passagem
    for j in range (0, len(texto)):
        posicao = ord(texto[j]) + 3
        textoCripto += chr(posicao)
        print(textoCripto)
    
    #textoCripto = segundaPassagem(textoCripto)
    print(textoCripto)
    textoCriptSegu = []
    tamanho = len(textoCripto) - 1
    k = 0
    for l in range (len(textoCripto), 0, -1):
        textoCriptSegu[k] = chr(ord(textoCripto[l]))
        k += 1
    #for j in range(0, len(textoCripto)):
    print(textoCripto)

