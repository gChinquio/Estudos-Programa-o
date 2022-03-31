segundos = int(input())

hora = int(segundos/3600)
minutos = int((segundos -(hora*3600))/60)
tS = int((segundos-(3600*hora) - (minutos*60)))

print("{}:{}:{}".format(hora,minutos,tS))
