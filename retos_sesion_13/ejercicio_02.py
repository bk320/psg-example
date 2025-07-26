# Ejercicio 2

contador = 1
# Sin contar 0
numero = 1
while contador <= 20:
    divisible_por_2 = numero % 2 == 0
    divisible_por_5 = numero % 5 == 0
    if divisible_por_2 and divisible_por_5:
        print(numero)
        contador += 1
    numero += 1