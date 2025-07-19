# Ejercicio 1

numero = int(input("Introduce un numero entero: "))
respuestas = {
    True: "El número es múltiplo de 5.",
    False: "El número No es múltiplo de 5."
}

es_multiplo_5 = True if numero % 5 == 0 else False
print(respuestas[es_multiplo_5])