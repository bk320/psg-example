# Agregar 5 Ejemplos con otras funciones no vistas en la sesión

print ("\n 1.- Funcion Center")
cadena = "Python"
resultado = cadena.center(20, '*')
print (cadena)
print (resultado)

print ("\n 2.- Funcion Endswith")
cadena = "Hola Mundo"
resultado = cadena.endswith("ndo")
print (cadena)
print (resultado)

print ("\n 3.- Funcion Expandtabs")
cadena = "Python\t es un lenguaje de programacion"
resultado = cadena.expandtabs(33)
print (cadena)
print (resultado)

print ("\n 4.- Funcion Removeprefix")
cadena = "Python es genial"
resultado = cadena.removeprefix("Python")
print (cadena)
print (resultado)

print ("\n 5.- Funcion Translate")
cadena = "Las vocales son a, e, i, o, u, son utilizadas en muchos idiomas."
tabla_traduccion = str.maketrans("aeiou", "12345")
resultado = cadena.translate(tabla_traduccion)
print (cadena)
print (resultado)