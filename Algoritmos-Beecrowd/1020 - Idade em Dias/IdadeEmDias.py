dias = int(input())

#ano =  int(dias/365)#convertendo dias em ano
#dias -= ano*365 #resto de dias (dia total - dias do total de anos)

#meses = int(dias/30) #convertendo dias em meses
#dias -= meses*30#convertendo meses em dias (dias - total de dias dos meses)

#print("{} ano(s)".format(int(ano)))
#print("{} mes(s)".format(int(meses)))
#print("{} dia(s)".format(int(dias)))

anos = int(dias/365)
dias = dias % 365

qtdMeses = int(dias/30)
dias = dias % 30

print(anos, "ano(s)")
print(qtdMeses, "mes(s)")
print(dias, "dia(s)")