x=[]
for i in range (0, 10):
    n = int(input())
    if(n == 0 or n < 0):
        x.insert(i, 1)
    else:
        x.insert(i, n)
    

for i in range (0, 10):
    print(f'X[{i}] = {x[i]}')