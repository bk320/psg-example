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
print(f'Lista de productos: \n{lista_productos} \n')

# Eliminamos un producto
indice_bon_bun = lista_productos.index('bon bon bum')
lista_productos.remove('bon bon bum')
lista_precios.pop(indice_bon_bun)
print(f'Lista de productos: \n{lista_productos} \n')

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
print(f'Precio total de los productos es: {total_precio} \n')

# Ordenar los productos del mas caro al mas barato
indices_mayor_a_menor = sorted(range(len(lista_precios)), \
    key=lambda i: lista_precios[i], reverse=True)
productos_ordenados = [lista_productos[i] for i in indices_mayor_a_menor]
precios_ordenados = [lista_precios[i] for i in indices_mayor_a_menor]
print(f'Productos ordenados de mayor a menor precio: \n{productos_ordenados}\n')
print(f'Precios ordenados de mayor a menor precio: \n{precios_ordenados}')

# Eliminar todos los productos y precios de las listas
lista_productos.clear()
lista_precios.clear()
print('\n Productos y precios eliminados.')
print(f'Lista de productos: {lista_productos}')
print(f'Lista de precios: {lista_precios}')