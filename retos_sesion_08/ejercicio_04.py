# Ejercicio 4
tupla = (10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)
suma = sum(tupla)
cantidad = len(tupla)
promedio = suma / cantidad
aprobado = promedio >= 51
print (f"El estudiante Aprobo ? \nR.{aprobado},"+ \
    f" su promedio es de {int(promedio)}")