n = int(input())

soma = 0
for i in range(n):
    x = input().split()
    t, v = x
    t = int(t)
    v = int(v)
    
    soma += t*v
print(soma)