leds = [2,5,5,4,5,6,3,7,6,6]

n = int(input())
soma = 0
for i in range(0, n):
    palavra = input()
    for i in range(0, len(palavra)):
        if palavra[i] == '1':
            soma += leds[0]
        elif(palavra[i] == '2'):
            soma += leds[1]
        elif(palavra[i] == '3'):
            soma += leds[2]
        elif(palavra[i] == '4'):
            soma += leds[3]
        elif(palavra[i] == '5'):
            soma += leds[4]
        elif(palavra[i] == '6'):
            soma += leds[5]
        elif(palavra[i] == '7'):
            soma += leds[6]
        elif(palavra[i] == '8'):
            soma += leds[7]
        elif(palavra[i] == '9'):
            soma += leds[8]
        elif(palavra[i] == '0'):
            soma += leds[9]
    print(soma, "leds")
    soma = 0