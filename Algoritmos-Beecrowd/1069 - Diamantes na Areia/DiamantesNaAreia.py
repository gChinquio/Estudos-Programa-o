n = int(input())

for i in range(n):
    pilha = input()
    tamanho = len(pilha) - 1
    contd = 0    
    par = 0
    for i in range (tamanho,-1, -1 ):
        if(pilha[i] == '>'):
            contd+= 1
        if(pilha[i]== '<'and contd > 0):
            par+= 1
            contd-=1
    print(par)            