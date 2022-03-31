x = input().split()

n1, n2, n3, n4 = x

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1))/10

if(media >=5.0 and media <= 6.9):
    ne = float(input())
    mf = (media+ne)/2

print(str("Media: {:0.1f}".format(media)))
if(media >= 7.0):
    print("Aluno aprovado.")
elif(media < 5.0):
    print("Aluno reprovado.")
elif(media >=5.0 and media <= 6.9):
    print("Aluno em exame.")
    if(mf >= 5.0):
        print(str("Nota do exame: {:0.1f}".format(ne)))
        print("Aluno aprovado.")
        print(str("Media final: {:0.1f}".format(mf)))
    else:
        print("Aluno reprovado.")
        print(str("Media final: {:0.1f}".format(mf)))