tomada = input().split()
plug = input().split()
result = ''
cont = 0
for i in range (5):
    if tomada[i] == plug[i]:        
        result = True
if result == True:
    print("N")
else:
    print("Y")
