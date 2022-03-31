n = int(input())

comando = ''
contA = 0
for i in range(0, n):
    comando = input()
    for j in range(0, len(comando)):
        if(comando[j] == 'a'):
            contA += 1
        elif(comando[j] == 'm'):
            break
    if(contA == 1):
        print("ka")
        contA = 0
    else:
        print("k",end="")
        for k in range(0, contA*2):
            print("a", end="")
        contA = 0
        print()
