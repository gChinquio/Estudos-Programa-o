n = int(input())
cont = 0

for i in range (n):
    v = float(input())
    while v > 1:
        v = v/2
        cont+= 1
    print(cont,("dias"))
    cont = 0