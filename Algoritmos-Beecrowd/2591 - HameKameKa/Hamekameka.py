n = int(input())

for i in range(0, n):
    palavra = input().split('me')
    total = palavra[0].count('a')
    total = total * palavra[1].count('a')
    print("k",end="")
    for j in range(0, total):
        print('a',end="")
    print()