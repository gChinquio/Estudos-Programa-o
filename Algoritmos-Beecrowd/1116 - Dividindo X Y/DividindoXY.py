# e = entrada
e = int(input())
while (e > 0):
    x = input().split()
    # n = numerador, d = denominador
    n, d = x

    n = int(n)
    d = int(d)

    if(d == 0):
        print("divisao impossivel")
    else:
        print(n/d)
    e = e-1