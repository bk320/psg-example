# Ejercicio 6

numero_1 = int(input("Ingrese el primer numero entero: "))
numero_2 = int(input("Ingrese el segundo numero entero: "))
operador = input("Ingrese el operador (+, -, *, /): ")

if operador == "+":
    resultado = numero_1 + numero_2
elif operador == "-":
    resultado = numero_1 - numero_2
elif operador == "*":
    resultado = numero_1 * numero_2
elif operador == "/":
    resultado = numero_1 / numero_2
else:
    resultado = None

if resultado:
    print("El resultado es:", resultado)
else:
    print("Operador no válido")