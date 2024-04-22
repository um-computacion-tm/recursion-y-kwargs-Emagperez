def sumatoria(value):
    #Condicion de corte siempre primero en recursividad
    if value == 0:

        return 0
    
    return value + sumatoria(value-1)



