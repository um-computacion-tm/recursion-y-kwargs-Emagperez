def factorial(value):
    #Condicion de corte siempre primero en recursividad
    if value in(0,1):

        return 1
    
    return value * factorial(value-1)


resultado = factorial(990)
print(resultado)