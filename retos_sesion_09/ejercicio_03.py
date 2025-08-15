# Ejercicio 3

lista_nombres = ['Ana', 'Luis', 'Pedro', 'José', 'Juan', 'Laura', 'Carlos', \
    'Marta', 'Javier', 'Lucía']
sub_lista = lista_nombres[5:10:2]
print(f'Sublista de 5 a 9 con saltos de 2: {sub_lista}')
posicion_jose = lista_nombres.index('José')
print(f'Posición de "José": {posicion_jose}')
lista_nombres.sort()
print(f'Lista ordenada: {lista_nombres}')
lista_nombres.reverse()
print(f'Lista invertida: {lista_nombres}')
