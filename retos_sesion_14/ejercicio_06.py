# Ejercicio 6

def separador_pares_impares(lista_numeros):
    pares = []
    impares = []
    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

pares, impares = separador_pares_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Lista de pares:", pares)
print("Lista de impares:", impares)