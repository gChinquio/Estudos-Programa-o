etiqueta = []
pessoas = []

eti = {}
pe = {}

n = int(input())

for i in range (n):
   
   lingua = input()
   exp = input()
   eti.update({lingua: exp})

m = int(input())
for j in range (m):
   nome = input()
   lingua = input()
   #pe.update({nome: lingua})
   print(nome)
   print(eti[lingua])
   print()
 
