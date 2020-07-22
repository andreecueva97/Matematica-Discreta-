##Ejemplo de funcion recursiva
def recursiveFunction(k):
    
    if(k == 0):
        return 0
    else:
        return recursiveFunction(k-1) + k - 1

n = 20
print(recursiveFunction(n))
print((n*(n-1))/2)