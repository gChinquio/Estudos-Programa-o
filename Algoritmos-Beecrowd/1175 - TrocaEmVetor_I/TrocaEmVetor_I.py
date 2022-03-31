vetor = []

n = 19
aux = 0
first = 0

for i in range(0, 20):
    vetor.insert(i, int(input()))

for i in range(0, 10, 1):
    aux = vetor[i]# aux pega 1º valor
    first = vetor[n]# first pega ultimo valor
    vetor[n] = aux# ultima posição recebe 1º
    vetor[i] = first# primeira posicao recebe ultimo
    n = n-1
    
for i in range (0, 20):
      print(f"N[{i}] = {vetor[i]}")
