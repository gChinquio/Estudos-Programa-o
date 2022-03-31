n = float(input())



print (imposto%2)

if n <= 2000.00:
    print("Isento")
elif n >= 2000.01 and n <= 3000.00:
    print("R$ ", n * 0.8 + (n%2) * 0.8)
elif n >= 3000.01 and n <= 4500.00:
    imposto = n - 2000.00

    print("R$ ", imposto * 0.8 + (n%2) * 0.18)
elif n >= 4500.00:
    print("R$ ", (n * 0.28))