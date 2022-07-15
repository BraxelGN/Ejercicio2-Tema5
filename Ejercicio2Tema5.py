def esPrimo(num):
    i = 2
    for i in range (2,num,1):
        if(num%i) == 0:
            return False
    return True

num = int (input("Ingrese un numero para saber si es primo: "))
print("Es primo: ",esPrimo(num))
