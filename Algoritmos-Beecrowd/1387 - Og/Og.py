while True:
    n = input().split()
    a, b = n
    a = int(a)
    b = int(b)
    if(a == 0 and b == 0):
        break
    else:
        print(a+b)