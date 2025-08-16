# Ejercicio 2

def calcular(numero1, numero2, operador):
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            return "Error: División entre cero no permitida"
    else:
        resultado = None
    return resultado

print(calcular(10, 5, "+"))
print(calcular(15, 10, "*"))
print(calcular(2025, 1995, "-"))
print(calcular(15, 3, "/"))
print(calcular(15, 0, "/"))