x = float(input())
n = []

total = x
n.append(float(x))
for i in range(1, 100):

    total = total - (total/2)
    
    n.append(float(total))

for i in range(0, 100):
    print(str("N[{}] = {:0.4f}").format(i,n[i]))