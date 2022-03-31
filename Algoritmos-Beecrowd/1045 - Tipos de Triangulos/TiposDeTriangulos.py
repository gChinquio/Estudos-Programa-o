x = input().split()
a,b,c = x

a = float(a)
b = float(b)
c = float(c)

if(a < b):
    x = b
    b = a
    a = x
elif(b < c):
    x = b
    b = c
    c = x



if(a >= b+c):
    print("NAO FORMA TRIANGULO")
else:
    if pow(a,2) == (pow(b,2) + pow(c,2)):
        print("TRIANGULO RETANGULO")
    else: 
        if pow(a,2) > (pow(b,2) + pow(c,2)):
            print("TRIANGULO OBTUSANGULO")
        else:
            if pow(a,2) < (pow(b,2) + pow(c,2)):
                print("TRIANGULO ACUTANGULO")            
            if(a==b and b==c and a==c):
                print("TRIANGULO EQUILATERO")
            else:
                if(a==b or b==c):
                    print("TRIANGULO ISOSCELES")