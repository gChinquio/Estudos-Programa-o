x = input().split()
y = input().split()

a, b, c = x

a = int(a)
b = int(b)
c = int(c)

d, f, g = y

d = int(d)
f = int(f)
g = int(g)

soma = 0

if(d > a):
    soma += d - a
if(f > b):
    soma+= f - b
if (g > c):
    soma+= g - c

print(soma)