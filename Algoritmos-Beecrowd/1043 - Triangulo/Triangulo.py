x = input().split()

a, b, c = x

a = float(a)
b = float(b)
c = float(c)

area = ((a+b)/2)*c

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):    
    print(str("Perimetro = {:0.1f}").format(a+b+c))
else:
    print(str("Area = {:0.1f}").format(area))    