def min_max(numeros): 
    menor = numeros[0]
    mayor = numeros[0]

    for n in numeros:
        if n <menor:
            menor = n

        if n > mayor:
            mayor = n

    return menor, mayor

datos = [9, 3, 2, 13, 0, 23, 8, 7]        

print(min_max(datos))

