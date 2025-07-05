# Ejercicio 3
tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

fisica = set(tienda_fisica)
online = set(tienda_online)

# a. Quiénes compraron en ambos canales.
clientes_general = fisica & online
print("Clientes que compraron en ambos canales:", clientes_general)

# b. Quiénes compraron solo en la tienda física.
clientes_solo_fisica = fisica.difference(online)
print("Clientes que compraron solo en la tienda física:", clientes_solo_fisica)

# c. Quiénes compraron solo online.
clientes_solo_online = online.difference(fisica)
print("Clientes que compraron solo online:", clientes_solo_online)