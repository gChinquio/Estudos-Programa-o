x = int(input())
y = int(input())

maior = 0
menor = 0

if(y > x):
    maior = y
    menor = x
else:
    maior = x
    menor = y

for i in range(menor+1, maior):
    if(i%5 == 2 or i%5 == 3):
        print(i)