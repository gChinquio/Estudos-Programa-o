#codpeca = int(input())
#npecaUm = int(input())
#valorUnitUm = float(input())

#codpecaDois = int(input())
#npecaDois = int(input())
#valorUnitDois = float(input())
x = input().split()

codpeca, npecaUm, valorUnitUm = x

codpeca = int(codpeca)
npecaUm = int(npecaUm)
valorUnitUm = float(valorUnitUm)

y = input().split()

codpecaDois, npecaDois, valorUnitDois = y

codpecaDois, npecaDois, valorUnitDois = y
codpecaDois = int(codpecaDois)
npecaDois = int(npecaDois)
valorUnitDois = float(valorUnitDois)

total = (npecaUm * valorUnitUm) + (npecaDois * valorUnitDois)
print(str("VALOR A PAGAR: " + str("R$ {:.02f}".format(total))))