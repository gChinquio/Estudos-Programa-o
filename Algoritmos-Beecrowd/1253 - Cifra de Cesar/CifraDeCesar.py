alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tAlfabeto = (len(alfabeto))
posi = 0
letraV = 0 
n = int(input())
casasPuladas = 0
palavra = ''
for i in range(0, n):
    palavra = input()
    casasPuladas = int(input())
    for j in range (0, len(palavra)):
        for k in range(0,26):
            if palavra[j]== alfabeto[k]:
                #print(alfabeto[k-2], end="")
                print("posicao - Letra", k, alfabeto[k])
                posifinal = k - casasPuladas
                print("Posicao trocada - Letra trocada",posifinal, alfabeto[posifinal])
            
                
                #if(posifinal < 0):
                    
                 #   posifinal = 25 - posifinal
                  #  print("posifinal:",posifinal)
                #print("posifinal:",posifinal)
