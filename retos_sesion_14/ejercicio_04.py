# Ejercicio 4
def valor_absoluto( numero):
    resultado = (numero*numero)**0.5
    # No me parece correcto devolver un float si el resultado es un entero
    if isinstance(numero, int) and resultado.is_integer():
        return int(resultado)
    return resultado

print(valor_absoluto(-5))
print(valor_absoluto(23))
print(valor_absoluto(5.2))