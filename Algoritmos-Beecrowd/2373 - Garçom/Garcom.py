n = int(input())
soma = 0
for i in range(n):
    x = input().split()
    l, c = x
    l = int(l)
    c = int(c)
    if(l > c):
        soma += c
print(soma)    