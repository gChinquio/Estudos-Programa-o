a = [100]

for i in range (0, 100):
    x = float(input())
    a.insert(i,x)

for i in range (0, 100):
    if(a[i] <= 10):
        print(str("A[{}] = {:0.1f}").format(i,a[i]))