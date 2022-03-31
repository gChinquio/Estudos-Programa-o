import math

x = input().split()
a, b, c = x

a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b))/2
maiorABC = (maiorAB+c+(abs(maiorAB-c)))/2
print(str("{:0.0f}".format(maiorABC)) + str(" eh o maior"))