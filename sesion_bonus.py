# sesion_bonus.py
def suma(a, b):
    c = a + b
    return c

def resta(a, b):
    return a - b

def multiplicacion(x, y):
    z = x * y
    return z

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
        return 0

a = 10
b = 5
print(suma(a, b))
print(resta(a, b))
print(multiplicacion(-a, b))
print(multiplicacion(a, b))
print(division(a, b))