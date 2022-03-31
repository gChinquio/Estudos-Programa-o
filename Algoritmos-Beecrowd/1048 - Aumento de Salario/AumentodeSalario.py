salario = float(input())

if(salario <= 400.00):
    print(str("Novo salario: {:0.2f}".format(salario + (salario*0.15))))
    print(str("Reajuste ganho: {:0.2f}".format(salario * 0.15)))
    print(str("Em percentual: 15 %"))
elif(salario >= 400.01 and salario <= 800.00):
    print(str("Novo salario: {:0.2f}".format(salario + (salario*0.12))))
    print(str("Reajuste ganho: {:0.2f}".format(salario * 0.12)))
    print(str("Em percentual: 12 %"))
elif(salario >= 800.01 and salario <= 1200.00):
    print(str("Novo salario: {:0.2f}".format(salario + (salario*0.10))))
    print(str("Reajuste ganho: {:0.2f}".format(salario * 0.10)))
    print(str("Em percentual: 10 %"))
elif(salario >= 1200.01 and salario <= 2000.00):
    print(str("Novo salario: {:0.2f}".format(salario + (salario*0.07))))
    print(str("Reajuste ganho: {:0.2f}".format(salario * 0.07)))
    print(str("Em percentual: 7 %"))
else:
    print(str("Novo salario: {:0.2f}".format(salario + (salario*0.04))))
    print(str("Reajuste ganho: {:0.2f}".format(salario * 0.04)))
    print(str("Em percentual: 4 %"))