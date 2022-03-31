while True:
    try:
        churras = {}

        n = int(input())

        for i in range (n):
            x = input().split()
            carne, valor = x
            valor = int(valor)
            churras.update({carne : valor})

        nChurrras = len(churras)
        cont = 0
        #Ordena pelos valores no dicionario - Sorted(dicionario) ordenar pelas chaves
        for j in sorted(churras, key=churras.get):
            if cont == nChurrras-1:
                print(j)    
                break
            cont+= 1
            print(j, end=" ")

        #print()
    except EOFError:
        break
