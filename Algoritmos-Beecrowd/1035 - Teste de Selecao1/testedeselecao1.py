
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())

## Para entrada de dados -TODAS DE UMA VEZ-
x = input().split()
a, b, c ,d = x
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (b>c and d>a):
    if (c + d) > (a + b):
        if(c > 0) and (d > 0):
            if((a % 2) == 0):
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")