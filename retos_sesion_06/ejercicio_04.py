# La resta de los números 17 y 9 es un número par?
numero_1 = 17
numero_2 = 9
resultado = numero_1 - numero_2
# Si la respuesta es 0 (numero par), not(0) es True 
# si la respuesta es cualquier otro número, not(1,2,3,...) es False
respuesta = not(resultado % 2)
print(f"resultado = {resultado}, ¿es par? -> {respuesta}")