n = int(input())

for i in range(0, n):
    palavra = input()
    casasPuladas = int(input())
    lNova = ''
    for j in palavra:
        posicao = ord(j)-casasPuladas
        if posicao < 65:
            lNova += chr(91-(65 - posicao))                   
        else:
            lNova += chr(ord(j) - casasPuladas)
    print(lNova)