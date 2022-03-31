from re import X


x = input().split()
a, b = x

a = int(a)
b = int(b)

soma = (b - a + 1)*(a + b)/2

print(str("{:0.0f}").format(soma))