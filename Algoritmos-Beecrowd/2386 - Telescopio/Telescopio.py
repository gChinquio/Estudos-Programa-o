f = int(input())

n = int(input())

cont = 0
for i in range(n):
    s = int(input())
    if (s*f >= 40000000):
        cont+= 1
    
print(cont)