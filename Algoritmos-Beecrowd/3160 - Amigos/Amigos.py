listaAtual = []
listaNova = []
listaAux = []
while True:
    listaAtual = input().split()
    listaNova = input().split()

    #print(listaAtual)
    #entrada amigo indicado
    amigoIndica = input()
    if(amigoIndica == "nao"):
        cont = 0
        tamanho = len(listaAtual)
        for i in listaNova:
            listaAtual.insert(tamanho,listaNova[cont])
            tamanho+=1
            cont+=1
        for x in range (len(listaAtual)):
            if(x == len(listaAtual) - 1):
                print(listaAtual[x])
                break
            print(listaAtual[x], end=" ")
        #print(listaNova)
        break
    #Posicao do amigo indicado na lista
    index = listaAtual.index(amigoIndica)
    #tamanho da lista atual/original
    tamanho = len(listaAtual)
    #lista aux recebe os valores da lista atual a partir da posicao do amigo indicado
    listaAux = listaAtual[index:tamanho]
    #mostra lista aux
    #print(listaAux)
    #Meclando listaAtual + Lista Aux
    cont = 0
    for i in listaNova:
        listaAtual.insert(index,listaNova[cont])
        index+=1
        cont+=1

    #listaAtual.append(listaAux)

    for x in range (len(listaAtual)):
        if(x == len(listaAtual) - 1):
            print(listaAtual[x])
            break
        print(listaAtual[x], end=" ")
        
    #print(listaAtual)
    break