n = int(input())

b = 1
v = 1
for i in range (0, n):
    for j in range (0, 3):
        b = v*v
    print(v*1, b, b*v)
    v += 1
    b = 0 


     	

#1 1 1
#2 4 8
#3 9 27
#4 16 64
#5 25 125