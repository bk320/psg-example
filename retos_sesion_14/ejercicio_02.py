# Ejercicio 2

def calcular(numero1, numero2, operador):
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    else:
        resultado = None
    return resultado

print(calcular(10, 5, "+"))
print(calcular(15, 10, "*"))
print(calcular(2025, 1995, "-"))