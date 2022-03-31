while(1):
    try:
        p = int(input())
        listP = []
        tp = input().split()#tp = total participantes
        for i in range (0, p):
            listP.append(int(tp[i]))
        maior = listP[0]

        for i in range(0, p):
            if listP[i] > maior:
                maior = listP[i]

        if(maior < 10):
            print(1)
        elif(maior <= 19):
            print(2)
        elif(maior >= 20):
            print(3)
    except EOFError:
        break