# Ejercicio 5
# casilla blanca -> #
# casilla negra -> *
for fila in range(1, 9):
    for columna in range(1, 9):
        if (fila + columna) % 2 == 0:
            print(" # ", end="")
        else:
            print(" * ", end="")
    print()