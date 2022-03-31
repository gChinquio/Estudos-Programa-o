n = int(input())
soma = 0
for i in range(0, n):
    x = input().split()
    a, b = x
    a = int(a)
    b = int(b)
    #ordem crescente de maior valor
    if(a > b):
        for j in range (b+1, a):
            if(j % 2 > 0 or j %2 < 0):
                soma = soma + j
    else:
        for j in range (a+1, b):
            if(j % 2 > 0 or j %2 < 0):
                soma = soma + j
    print(soma)
    soma = 0