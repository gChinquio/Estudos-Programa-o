#n = int(input())
#n1 = 0
#n2 = 1
#soma = 0
#for i in range (0, n):
#    print (n1)
#    soma = n1+n2
#    n1 = n2
#    n2 = soma

n = int(input())
n1 = 0
n2 = 1
soma = 0
for i in range (0, n):
    if(i == n-1):
        print(n1)
        break
    print(n1, end=" ")
    soma = n1+n2
    n1 = n2
    n2 = soma