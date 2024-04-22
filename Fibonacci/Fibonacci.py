def fibonacci(value):
    anterior, resultado =0,1
    for _ in range (value -1):
        anterior, resultado = resultado, anterior + resultado
    return resultado


resultado_3 = fibonacci(13)

print(resultado_3)