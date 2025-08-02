# Ejercicio 5
# Crear una función que reciba una cadena y devuelva la cantidad de 
# vocales que tiene. recursivamente

def contar_vocales(cadena):
    if not cadena:
        return 0
    else:
        if cadena[0].lower() in 'aeiou':
            return 1 + contar_vocales(cadena[1:])
        else:
            return contar_vocales(cadena[1:])

print(contar_vocales("Hola Mundo")) # 4
print(contar_vocales("Prueba de vocales")) # 7
print(contar_vocales("Richard Choquerive Ramos")) # 9
    