def obtener_aleatorio(nombre_jugador):
    numeros = list(range(1, 101))
    #para simular la aleatoriedad y no utilizar librerias externas, se 
    #utilizara el nombre del jugador
    suma_letras = sum(ord(c) for c in nombre_jugador)
    indice = suma_letras % len(numeros)
    secreto = numeros[indice]
    return secreto

def adivina(secreto):
        intentos = 0
        print ("Que número estoy pensando? (1-100)")
        while True:
            try:
                intento = int(input(f"Intento N°: {intentos+1}: "))
                if intento == secreto:
                    print ("Felicidades! Has adivinado el número!")
                    break
                elif intento < secreto:
                    print ("El número es mayor.")
                else:
                    print ("El número es menor.")
            except ValueError:
                print ("Por favor, ingresa un número válido.")
            finally:
                intentos += 1
        print (f"Has adivinado el número en {intentos} intentos.\n")

def jugar():
    while True:
        print ("Bienvenido al juego de adivinanzas! del Python Study Group 2025")
        print ("="*63)
        nombre_jugador = input("¿Cuál es tu nombre?: ")
        print (f"Bienvenido, {nombre_jugador}!")
        print ("="*63)
        print ()
        opcion = input("Quieres jugar? (s/n): ")
        if opcion.upper() != 'S':
            break
        secreto = obtener_aleatorio(nombre_jugador)
        adivina(secreto)
    print ("Gracias por participar!")
    print (f"🐍 Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2025! 🐍")

jugar()