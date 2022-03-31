while True:
    try:
        n = int(input())
        lista = []
        for i in range(n):
            lista.append(input())

        listaOrdenada = sorted(lista)

        for i in range(n):
            print(listaOrdenada[i])
    except EOFError:
        break