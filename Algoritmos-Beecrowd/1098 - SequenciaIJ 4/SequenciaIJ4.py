cont = 0.2
k = 1 #controla inicio do loop
total = 3#controla soma dos valores para aumentar os loops
kFinal = 3#controla os 3 loops

#bloco inicial
jini = 1
contini = 0
for i in range(0, 3):
   print(str("I={:0.1f} J={}".format(contini,jini)))
   jini += 1

#segundo bloco
while (cont <= 2.0):
   
   while(k <= kFinal):     
      print(str("I={:0.1f} J={:0.1f}".format(cont,k)))
      k+= 1
      cont += 0.2
      total += 0.2
   if(total == 4):
      k += 1
      kFinal += 1
   elif(total == 5):
      k+=1
      kFinal += 1
   k=1
   

