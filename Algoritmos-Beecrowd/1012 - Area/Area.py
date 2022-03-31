import math

#a = float(input())
#b = float(input())
#c = float(input())
x = input().split()
a, b, c = x

a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

triangulo = (a*c)/2 #a = base, c = altura
circulo = pow(c,2) * pi #c = raio
trapezio = ((a+b)/2) * c #a, b = base, c = altura
quadrado = (b*b) #b = lado
retangulo = (a*b) #a, b = lado

print(str("TRIANGULO: ") + str("{:0.3f}".format(triangulo)))
print(str("CIRCULO: ") + str("{:0.3f}".format(circulo)))
print(str("TRAPEZIO: ") + str("{:0.3f}".format(trapezio)))
print(str("QUADRADO: ") + str("{:0.3f}".format(quadrado)))
print(str("RETANGULO: ") + str("{:0.3f}".format(retangulo)))