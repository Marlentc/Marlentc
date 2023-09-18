def maximo(valores):
    mayor = valores[0]

    for i in range(1, len (valores)):
        if valores[i] > mayor:
            mayor = valores[i]

    return mayor
        
numeros = [8, 10, 3, 5, 7, 15, 20]

print(maximo(numeros))