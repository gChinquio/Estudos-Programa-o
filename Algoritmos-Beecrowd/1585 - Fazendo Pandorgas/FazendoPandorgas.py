n = int(input())

for i in range(n):
    v = input().split()
    x, y = v
    x = int(x)
    y = int(y)

    #print(str("{:0.0f} cm2").format((x*y)/2))
    print("%d cm2"%((x*y)/2))