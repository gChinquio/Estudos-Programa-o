class Churras:    
    def __init__(self, carne, preco) -> None:
        self.Carne = carne
        self.Preco = preco    
        


#churras = Churras("Alcatra", 20)
#print(churras.Carne)
n = int(input())
lista = []
for i in range (0, n):
    x = input().split()
    c, p = x
    p = int(p)
    
    churras = Churras(c, p)
    lista.append(churras)
    
    
