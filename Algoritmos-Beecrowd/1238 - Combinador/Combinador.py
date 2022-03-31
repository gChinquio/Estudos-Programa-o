from re import T


entrada = int(input())
primeira = 0
segunda = 0
novaPalavra = ''
p1 = ''
p2 = ''
tamanhof = 0
for i in range(0,entrada):
    palavra = input().split()
    p1 = palavra[0]
    p2 = palavra[1]
    
    tamanhof = len(palavra[1]) - len(palavra)
    #tamanho = len(palavra[0]+palavra[1])
    if(int(len(palavra[0])) < int(len(palavra[1]))):
        tamanho = len(palavra[0])
    else:
        tamanho = len(palavra[1])

    for j in range(0, tamanho):        
        novaPalavra+=p1[j]
        novaPalavra+=p2[j]
    
    print(novaPalavra)