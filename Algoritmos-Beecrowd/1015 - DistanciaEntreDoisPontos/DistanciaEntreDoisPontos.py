import math

x = input().split()
x1, y1 = x

x1 = float(x1)
y1 = float(y1)

y = input().split()
x2, y2 = y

x2 = float(x2)
y2 = float(y2)

distancia = math.sqrt((pow(x2-x1,2)+pow(y2-y1,2)))

print("{:0.4f}".format(distancia))


