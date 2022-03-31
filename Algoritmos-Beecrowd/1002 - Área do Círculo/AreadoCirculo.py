import math

n = 3.14159
raio = float(input())
area = n * (math.pow(raio,2))
print(str("A=") + str("{:0.4f}".format(area)))
