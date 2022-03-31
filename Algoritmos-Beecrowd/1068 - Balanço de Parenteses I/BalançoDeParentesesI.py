lista = []

while(True):
    try:
        lista = input()

        #contador parenteses +1 Fecha | -1 Abre | final == 0 (abriu e fechou todos)
        contP = 0

        tamanho = len(lista) -1
        for i in range (tamanho, -1,-1):  
            if (ord(lista[i]) == 40 and i == tamanho):
                contP = -1
                break
            elif (ord(lista[i]) == 41):        
                contP+= 1
            elif (ord(lista[i]) == 40):        
                contP-= 1

        if(contP == 0):
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break