import math

x = int(input())
for i in range (1, x+1):
    if(i %2 == 0):
        #print(i,"^",i," = ", pow(i,2))
        print(str("{:}".format(i)+"^2"+" = {:}".format(pow(i,2))))