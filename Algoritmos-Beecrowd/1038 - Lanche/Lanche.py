x = input().split()

coditem, qtditem = x

coditem = int(coditem)
qtditem = int(qtditem)

if(coditem == 1):
    total = qtditem * 4
elif (coditem == 2):
    total = qtditem * 4.50
elif (coditem == 3):
    total = qtditem * 5.00
elif (coditem == 4):
    total = qtditem * 2.00
else:
    total = qtditem * 1.50

print(str("Total: R$ {:0.2f}".format(total)))