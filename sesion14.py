# def nombre_funcion():
#     print ("Bloque de código")

# nombre_funcion()

# nombre_funcion()

# def nombre_funcion():
#     print ("Bloque de código")

# def funcion():
#     print ("Bloque de código")

# funcion()

# print ("Ejemplo 1")
# print ("1. Definir función")
# def imprimir_pares():
#     pares = [i for i in range(0, 21, 2)]
#     print (pares)
# print ("2. Llamar función")
# imprimir_pares()
# imprimir_pares()

# mensajes = {"Bienvenido al Python Study Group 🐍",
# "¡Hola y bienvenido al Python Study Group! ✨",
# "Hola, aprendamos Python juntos 🐍"}
# def bienvenida():
#     mensajes = {"Bienvenido al Python Study Group 🐍",
#     "¡Hola y bienvenido al Python Study Group! ✨",
#     "Hola, aprendamos Python juntos 🐍"}
#     print (mensajes.pop())

# bienvenida()

# def funcion():
#     return "Bloque de código"
#
# resultado = funcion()
# print (resultado)

# print ("Ejemplo 2")
# print ("1. Definir función")
# def saludo():
#     saludos = {"Hola", "Hello", "Bonjour", "Ciao"}
#     return saludos.pop()

# print ("2. Llamar función")
# resultado = saludo()
# print (resultado)

# frutas = {'🍅','🍌','🍎','🍇','🍉'}
# def devolver_fruta():
#     frutas = {'🍅','🍌','🍎','🍇','🍉'}
#     return frutas.pop()

# fruta = devolver_fruta()
# print (fruta)

# def funcion():
#     return "Bloque", "de", "código"

# resultado = funcion()
# print (resultado)

# print ("Ejemplo 3")
# print ("1. Definir función")
# def saludo():
#     saludos_es = {"Hola", "Holi", "Buenos días"}
#     saludos_en = {"Hello", "Hi", "Good morning"}
#     return saludos_es.pop(), saludos_en.pop()

# print ("2. Llamar función")
# resultado = saludo()
# print (resultado)

# frutas = {'🍅','🍌','🍎','🍇','🍉'}
# colores = {'🔴','🟠','🟡','🟢','🔵'}
# def devolver_fruta_color():
#     frutas = {'🍅','🍌','🍎','🍇','🍉'}
#     colores = {'🔴','🟠','🟡','🟢','🔵'}
#     return frutas.pop(), colores.pop()

# fruta, color = devolver_fruta_color()
# print (fruta, color)

# def funcion(parametro):
#     print (parametro)

# funcion("Bloque de código") #1 Argumento

# print ("Ejemplo 4")
# print ("1. Definir función")
# def cuadrado(numero):
#     print (numero**2)

# print ("2. Llamar función")
# cuadrado(5)
# cuadrado(10)

# mensajes = {"es":"Bienvenido al Python Study Group 🐍",
# "en": "Hello and welcome to the Python Study Group! ✨",
# }
# def bienvenida(idioma):
#     mensajes = {
#         "es":"Bienvenido al Python Study Group 🐍",
#         "en": "Hello and welcome to the Python Study Group! ✨",
#     }
#     print (mensajes.get(idioma, "¡Hola!"))

# bienvenida("es")
# bienvenida("en")
# bienvenida("fr")

# def funcion(param1, param2, ...,  paramN):
#     print (param1, param2, ..., paramN)

# funcion("Bloque", "de", "código")

# print ("Ejemplo 5")
# print ("1. Definir función")
# def repetir(cadena, veces):
#     print (cadena*veces)

# print ("2. Llamar función")
# repetir("✨🎉", 10)

# # Entrada
# animales = ['🐶','🐱','🐭','🐹','🐰']
# # Salida
# animales = ['🐶🐶🐶', '🐱🐱🐱', '🐭🐭🐭', '🐹🐹🐹', '🐰🐰🐰']
# def repetir_animales(animales, veces):
#     lista = [animal*veces for animal in animales]
#     print (lista)

# animales = ['🐶','🐱','🐭','🐹','🐰']
# repetir_animales(animales, 3)

# print (resultado)

# def funcion(param1, param2, paramN):
#     return param1

# resultado = funcion("Bloque", "de", "código")
# print (resultado)

# print ("Ejemplo 6")
# print ("1. Definir función")
# def operaciones(numero1, numero2):
#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multiplicacion = numero1 * numero2
#     division = numero1 / numero2
#     return [suma, resta, multiplicacion, division]

# print ("2. Llamar función")
# resultado = operaciones(10, 5)
# print (resultado)

# Ejercicio 6, Crear una función que reciba dos enteros y una cadena devolver 
# el resultado de la operación de los números según la cadena puede ser suma, 
# resta, multiplicación o división
# def operacion(numero1, numero2, operacion):
#     if operacion == "suma":
#         return numero1 + numero2
#     elif operacion == "resta":
#         return numero1 - numero2
#     elif operacion == "multiplicacion":
#         return numero1 * numero2
#     elif operacion == "division":
#         return numero1 / numero2
#     else:
#         return "Operación no válida"

# resultado = operacion(10, 5, "suma")
# print (resultado)

# print ("Ejemplo 7")
# print ("1. Definir función")
# def operaciones(numero1, numero2):
#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multiplicacion = numero1 * numero2
#     division = numero1 / numero2
#     return suma, resta, multiplicacion, division

# print ("2. Llamar función")
# suma, resta, multiplicacion, division = operaciones(10, 5)
# print (suma, resta, multiplicacion, division)

# # Ejercicio 7, Crear una juego de piedra papel o tijera, donde reciba dos 
# # jugadas por tecladay devuelva las jugadas y el resultado, si ingresa 
# # salir terminar el juego
# def jugar_piedra_papel_tijera(jugada1, jugada2):
#     if jugada1 == jugada2:
#         resultado = "Empate"
#     elif jugada1 == "piedra" and jugada2 == "tijera":
#         resultado = "Jugador 1 gana"
#     elif jugada1 == "papel" and jugada2 == "piedra":
#         resultado = "Jugador 1 gana"
#     elif jugada1 == "tijera" and jugada2 == "papel":
#         resultado = "Jugador 1 gana"
#     else:
#         resultado = "Jugador 2 gana"
#     return jugada1, jugada2, resultado

# while True:
#     jugador1 = input("Jugador 1: ")
#     if jugador1 == "salir":
#         break
#     jugador2 = input("Jugador 2: ")
#     if jugador2 == "salir":
#         break
#     resultado = jugar_piedra_papel_tijera(jugador1, jugador2)
#     print (resultado)
    
# variable_global = "Variable global"

# def funcion():
#     variable_local = "Variable local"
#     print ("✨",variable_global)
#     print ("✨",variable_local)

# funcion()
# print ("🎈",variable_global)
# print ("🎈",variable_local)

# variable = "Variable global"
# print ('0.',variable)

# def funcion():
#     variable = "Variable local"
#     print ('1.',variable)

# funcion()
# print ('2.',variable)

# numeros = [10, 5, 20, 15, 25, 30] #Global

# def mayor_menor(): #No recibe argumentos
#     mayor = max(numeros) #Local
#     menor = min(numeros) #Local
#     return mayor, menor #Devuelve dos valores

# resultado = mayor_menor()
# print (resultado)

# # Ejercicio 8, De la siguiente cadena global convertir en formato título y 
# # contar las vocales aeiou con una función
# def formato_vocales():
#     titulo = cadena.title()
#     vocales = sum([1 for letra in titulo if letra in "aeiou"])
#     return titulo, vocales

# cadena = "python es un lenguaje de programación"
# resultado = formato_vocales()

# print (resultado)

# def funcion(*args):
#     print (args)
#     print (type(args))

# funcion("Bloque", "de", "código")

# print ("Ejemplo 9")
# print ("1. Definir función")
# def concatenar(numero, *cadenas):
#     concatenado = ""
#     for cadena in cadenas:
#         concatenado += cadena
#     return concatenado*numero

# print ("2. Llamar función")
# resultado = concatenar(3, "🍎", "🍌", "🍍")
# print (resultado)

# # Ejercicio 9, Crear una función que reciba N objetos y genere una tupla y 
# # una lista con los objetos usando *args
# def tupla_lista(*args):
#     tupla = tuple(args)
#     lista = list(args)
#     return tupla, lista

# lista, tupla = tupla_lista(1, 1.1, True, "🍎")

# print (lista)
# print (tupla)

# def funcion(**kwargs):
#     print (kwargs)
#     print (type(kwargs))

# funcion(nombre="Jhon", apellido="Doe", genero="M")

# print ("Ejemplo 10")
# print ("1. Definir función")
# def datos_persona(**datos):
#     mensaje = ""
#     for clave, valor in datos.items():
#         mensaje += f"{str(clave).title()}: {str(valor).upper()}\n"
#     return mensaje
# print ("2. Llamar función")
# resultado = datos_persona(nombre="Jhon", apellido="Doe", edad=20, boliviano=True)
# print (resultado)

# # Ejercicio 10, Crea un simulador de lavar platos con una función que 
# # reciba los objetos a lavar y el tiempo de lavado de cada objeto devuelva un 
# # mensaje con los objetos lavados y el tiempo total de lavado
# def lavar(**objetos):
#     tiempo_total = 0
#     mensaje = ""
#     for objeto, tiempo in objetos.items():
#         tiempo_total += tiempo
#         mensaje += f"{objeto}: {tiempo} minutos\n"
#     mensaje += f"Tiempo total: {tiempo_total} minutos"
#     return mensaje

# resultado = lavar(plato=5, vaso=3, tenedor=1, cuchara=0.5)
# print (resultado)

# def funcion():
#     """
#     Documentación aquí
#     """
#     print ("Bloque de código")
    
# print ("Acceso a la documentación")
# def funcion():
#     """
#     Documentación aquí
#     """
#     print ("Bloque de código")
# print (funcion.__doc__)
# print ("Fin de la ejecución")

# print ("Ejemplo 11")
# print ("1. Definir función Principal")
# def principal(numero):
#     cuadrado = cuadrado_numero(numero)
#     cubo = cubo_numero(numero)
#     return cuadrado, cubo

# print ("2. Definir función Cuadrado")
# def cuadrado_numero(numero):
#     return numero**2

# print ("3. Definir función Cubo")
# def cubo_numero(numero):
#     return numero**3

# print ("4. Llamar función Principal")
# numero = 5
# resultado = principal(numero)
# print (numero, resultado)

# def limpiar_letras(cadena):
#     """
#     Elimina los números de una cadena y espacios
#     """
#     return "".join([letra for letra in cadena if letra.isalpha()])
# def limpiar_mayusculas(cadena):
#     """
#     Convierte una cadena en mayúsculas
#     """
#     return cadena.upper()

# def limpiar(cadena):
#     cadena = limpiar_letras(cadena)
#     cadena = limpiar_mayusculas(cadena)
#     return cadena

# cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2025"
# resultado = limpiar(cadena)
# print (cadena)
# print (resultado)

# def funcion_recursiva(valor):
#     if caso_base:
#         return valor
#     else:
#         return funcion_recursiva(valor)

# print ("Ejemplo 12")
# print ("1. Definir función")
# def numero_par(numero):
#     if numero == 0:
#         return 0
#     else:
#         return numero_par(numero-1) + 2

# print ("2. Llamar función")
# resultado = numero_par(10)
# print (resultado)

# def factorial(numero):
#     if numero == 0:
#         return 1
#     else:
#         return numero*factorial(numero-1)

# resultado = factorial(5)
# print (resultado)

# print ("Ejemplo 13")
# cuadrado = lambda numero: numero**2
# resultado = cuadrado(5)
# print (resultado)
# resultado = cuadrado(10)
# print (resultado)


# Ejercicio 13, Crear una función anónima para obtener de una cadena las 
# letras solo los alfanuméricos y convertir en mayúsculas

cadena = "Python es un lenguaje de programación"
limpiar = lambda cadena: "".join([letra for letra in cadena if letra.isalnum()]).upper()
resultado = limpiar(cadena)
print (cadena)
print (resultado)
