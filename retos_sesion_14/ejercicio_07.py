# Ejercicio 7

def print_tablero(tablero):
    print("\n" * 30)
    print("\n¡Bienvenido al juego Tres en Raya!\n")
    print("     0    1    2")
    for i, fila in enumerate(tablero):
        print(f"{i}  {fila}")
    print()

def ganador(tablero, jugador):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def marcar_casilla(tablero, jugador, fila, columna):
    if 0 <= fila <= 2 and 0 <= columna <= 2:
        if tablero[fila][columna] == '_':
            tablero[fila][columna] = jugador
            return True
        else:
            print("\n" * 30)
            print("🚫  ¡POSICIÓN OCUPADA! INTENTA DE NUEVO.")
            return False
    else:
        print("\n" * 30)
        print("❌ Coordenadas fuera de rango. Intenta con valores entre 0 y 2.")
        return False   
    
def analizar_turno(tablero, jugador, simbolo):
    while True:
        print_tablero(tablero)
        print("Turno de", simbolo)
        pocision_x = (input("Ingrese fila (0-2) para " + jugador + ": "))
        pocision_y = (input("Ingrese columna (0-2) para " + jugador + ": "))
        if pocision_x.isdigit() and pocision_y.isdigit():
            pocision_x = int(pocision_x)
            pocision_y = int(pocision_y)
            if marcar_casilla(tablero, jugador, pocision_x, pocision_y):
                break 
        else:
            print("\n" * 30)
            print("❌ Coordenadas inválidas. Intenta con valores entre 0 y 2.")
            
def juego_terminado(tablero):
    for fila in tablero:
        if '_' in fila:
            return False
    return True

    
def verificar_fin_juego(tablero, jugador):
    """Verifica si el juego terminó y devuelve el estado"""
    if ganador(tablero, jugador):
        print_tablero(tablero)
        print("🎉 ¡Felicidades! 🎉")
        print(f"🏆 El jugador '{jugador}' ha ganado el juego. ¡Bien hecho! 🥇")
        return True
    
    if juego_terminado(tablero):
        print_tablero(tablero)
        print("¡Es un empate! 🤝")
        return True
    
    return False

def juego_tres_en_raya():
    tablero = [['_' for columna in range(3)] for fila in range(3)]
    jugadores = [('X', '❌'), ('O', '⭕')]
    turno = 0
    
    while True:
        jugador, simbolo = jugadores[turno % 2]
        analizar_turno(tablero, jugador, simbolo)
        if verificar_fin_juego(tablero, jugador):
            return
        turno += 1

juego_tres_en_raya()            