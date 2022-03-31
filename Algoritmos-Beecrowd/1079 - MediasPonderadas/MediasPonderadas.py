entrada = int(input())

while (entrada > 0):
    x = input().split()

    a , b, c = x

    a = float(a)
    b = float(b)
    c = float(c)

    media = ((a * 2) + (b * 3) + (c * 5))/10

    print(str("{:0.1f}".format(media)))


    entrada = entrada -1