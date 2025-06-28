# Ejercicio 4

lista_productos = ['filipitos', 'club social', 'Chizitos', 'yogueta', \
    'Oreo', 'barra de granola', 'helado delizia', \
    'bon o bon', 'bon bon bum']
lista_precios = [21, 3.5, 11, 2, 4, 7, 8, 1.5, 2.5]
# Agregamos dos productos
lista_productos.append('Galleta Mabel Rosquita')
lista_productos.append('chicles topline')
lista_precios.append(13)
lista_precios.append(4.5)
# Eliminamos un producto
indice_bon_bun = lista_productos.index('bon bon bum')
lista_productos.remove('bon bon bum')
lista_precios.pop(indice_bon_bun)
# Cuanto cuesta un producto
indice_oreo = lista_productos.index('Oreo')
print(f'Precio de Oreo: {lista_precios[indice_oreo]}')
indice_chizitos = lista_productos.index('Chizitos')
print(f'Precio de Chizitos: {lista_precios[indice_chizitos]}')
# Producto más caro y más barato
indice_caro = lista_precios.index(max(lista_precios))
indice_barato = lista_precios.index(min(lista_precios))
print(f'Producto más caro:  {lista_productos[indice_caro]} \
    - Precio: {lista_precios[indice_caro]}')
print(f'Producto más barato:  {lista_productos[indice_barato]} \
    - Precio: {lista_precios[indice_barato]}')
# Cuantos productos hay en la lista
cantidad_productos = len(lista_productos)
print(f'Existen: {cantidad_productos} productos en la lista.\n')
# Cuanto cuestan todos los productos
total_precio = sum(lista_precios)
print(f'El total de los precios es: {total_precio} \n')
# Ordenar los productos del mas caro al mas barato
pares = [
    (lista_precios[0], lista_productos[0]),
    (lista_precios[1], lista_productos[1]),
    (lista_precios[2], lista_productos[2]),
    (lista_precios[3], lista_productos[3]),
    (lista_precios[4], lista_productos[4]),
    (lista_precios[5], lista_productos[5]),
    (lista_precios[6], lista_productos[6]),
    (lista_precios[7], lista_productos[7]),
    (lista_precios[8], lista_productos[8]),
    (lista_precios[9], lista_productos[9])
]
pares.sort()
print("Productos ordenados de menor a mayor precio:")
print(f'{pares[0][1]} - Bs {pares[0][0]}')
print(f'{pares[1][1]} - Bs {pares[1][0]}')
print(f'{pares[2][1]} - Bs {pares[2][0]}')
print(f'{pares[3][1]} - Bs {pares[3][0]}')
print(f'{pares[4][1]} - Bs {pares[4][0]}')
print(f'{pares[5][1]} - Bs {pares[5][0]}')
print(f'{pares[6][1]} - Bs {pares[6][0]}')
print(f'{pares[7][1]} - Bs {pares[7][0]}')
print(f'{pares[8][1]} - Bs {pares[8][0]}')
print(f'{pares[9][1]} - Bs {pares[9][0]}')
# Eliminar todos los productos y precios de las listas
lista_productos.clear()
lista_precios.clear()
print(f'Lista de productos: {lista_productos}')
print(f'Lista de precios: {lista_precios}')