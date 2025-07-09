# Tabla de verdad ejercicio 3

print("Operador XOR")
a = True
b = True
print(f"Tarjeta = {a}, Huella = {b} \
    ->  Puerta abierta? = {(a or b) and not (a and b)}")
a = True
b = False
print(f"Tarjeta = {a}, Huella = {b} \
    ->  Puerta abierta? = {(a or b) and not (a and b)}")
a = False
b = True
print(f"Tarjeta = {a}, Huella = {b} \
    ->  Puerta abierta? = {(a or b) and not (a and b)}")
a = False
b = False
print(f"Tarjeta = {a}, Huella = {b} \
    ->  Puerta abierta? = {(a or b) and not (a and b)}")