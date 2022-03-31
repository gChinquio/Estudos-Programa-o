while True:
    n = int(input())
    if(n == 0):
        break
    com = input()
    direcao = 'N'
    for i in range (n):
        if com[i] == 'D' and direcao == 'N':
            direcao = 'L'
        elif com[i] == 'D' and direcao == 'L':
            direcao = 'S'
        elif com[i] == 'D' and direcao == 'S':
            direcao = 'O'
        elif com[i] == 'D' and direcao == 'O':
            direcao = 'N'
        elif com[i] == 'E'and direcao == 'N':
            direcao = 'O'
        elif com[i] == 'E' and direcao == 'O':
            direcao = 'S'
        elif com[i] == 'E' and direcao == 'S':
            direcao = 'L'
        elif com[i] == 'E' and direcao == 'L':
            direcao = 'N'
    print(direcao)
    direcao = 'N'