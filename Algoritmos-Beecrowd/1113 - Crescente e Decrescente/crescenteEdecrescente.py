while(1):
    n = input().split()

    x, y = n
    x = int(x)
    y = int(y)
    
    if(x == y):
        break
    elif(x > y):
        print("Decrescente")
    elif(x < y):
        print("Crescente")
