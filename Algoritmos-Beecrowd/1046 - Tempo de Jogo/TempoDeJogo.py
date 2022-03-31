n = input().split()

i, f = n

i = int(i)
f = int(f)

if(f > i):
    print(str("O JOGO DUROU {} HORA(S)").format(f-i))
elif(i > f):
    print(str("O JOGO DUROU {} HORA(S)").format((24 - i) + f))
else:
    print("O JOGO DUROU 24 HORA(S)")