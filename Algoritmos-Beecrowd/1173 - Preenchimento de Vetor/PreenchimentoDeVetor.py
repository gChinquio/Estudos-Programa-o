x = int(input())

lista = [10]

for i in range(0, 10):
    lista.insert(i, x)
    x = x*2
    print(f'N[{i}] = {lista[i]}')