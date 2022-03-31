ini = 7
fim = 4
for i in range (1, 10, 2):
    for j in range (ini, fim, -1): #decremento - 7 até 4 em -1
       print(str("I={} J={}".format(i,j)))
    ini += 2
    fim += 2




#I=1 J=7
#I=1 J=6
#I=1 J=5
#I=3 J=9
#I=3 J=8
#I=3 J=7

#...
#I=9 J=15
#I=9 J=14
#I=9 J=13