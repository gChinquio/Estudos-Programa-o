while(1):
    maior = 0
    menor = 0
    soma = 0

    v = input().split()
    x, y = v
    
    x = int(x)
    y = int(y)
    
    if(x == 0 or y == 0 or x < 0 or y < 0):
        break
    
    
    if(y > x):
        maior = y
        menor = x
    else:
        menor = y
        maior = x

    for i in range(menor, maior+1):
        soma += i
    
    for i in range(menor, maior+1):
        print(i, end=" ")          
        if i == maior:
            break
    print(str("Sum={}".format(soma)))