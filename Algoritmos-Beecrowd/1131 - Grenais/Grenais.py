qtdJogos = 0
nvI = 0
nvG = 0
empate = 0
temjogo = 1
while(temjogo == 1):
    x = input().split()
    i, g = x
    i = int(i)
    g = int(g)

    qtdJogos = qtdJogos + 1

    if(i > g):
        nvI = nvI +1
    elif(g > i):
        nvG = nvG +1
    else:
        empate = empate +1
    print("Novo grenal (1-sim 2-nao)")
    temjogo = int(input())
    if(temjogo == 2):
        break

print(qtdJogos, "grenais")
print("Inter:%d" %(nvI))
print("Gremio:%d" %(nvG))
print("Empates:%d"%(empate))
if(nvI > nvG):
    print("Inter venceu mais")
elif(nvG > nvI):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")