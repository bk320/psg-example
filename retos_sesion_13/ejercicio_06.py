# Ejercicio 6

while True:
    numero = int(input("Introduce un numero entero (0 para salir): "))
    if numero == 0:
        break
    elif numero % 7 == 0:
        print("El numero es multiplo de 7")
    else:
        print("El numero NO es multiplo de 7")