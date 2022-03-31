def fatorialRe(n):
    if(n == 0):
        return 1
    else:
        return(n*fatorialRe(n-1))

x = int(input())

result = fatorialRe(x)
print(result)