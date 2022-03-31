n = int(input())
soma = 0
cont = 0
for i in range(n):
    j = input().split()
    x, y = j
    x = int(x)
    y = int(y)
    
    while(True):
        if(x%2 > 0 or x%2 < 0):
            soma += x            
            cont+=1  
        x += 1      
        if(cont == y):
            break
    print(soma)
    soma = 0
    cont = 0