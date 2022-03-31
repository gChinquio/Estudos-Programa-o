contA = 0
contB = 0
while True:
    n = int(input())
    if(n == 0):
        break
    for i in range(n):
        x = input().split()
        a, b = x
        a = int(a)
        b = int(b)

        if(a > b):
            contA+= 1
        elif(b > a):
            contB+= 1
        
            
    print(contA, contB)
    contA = 0
    contB = 0