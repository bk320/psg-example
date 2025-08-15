# Ejercicio 5

animales = {"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}

# Añade al arca 3 especies más usando update()
animales.update({"🐼" : 2, "🕊️" : 2, "🐮" : 2})

# Toma lista de los animales en el arca iterando el diccionario
iterador = iter(animales.items())
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)

# Existe en el arca la especie 'dragon' 🐲?
respuestas = {
    False: "No, no existe la especie 'dragon' 🐲 en el arca",
    True: "Si, existe la especie 'dragon' 🐲 en el arca"
}
existe = "🐲" in animales
print("\nExiste en el arca la especie 'dragon' 🐲?")
print(respuestas[existe])

# Elimina la especie unicornio del arca
unicornio = animales.pop("🦄")

# Modifica el valor de la especie jirafa por 2
animales["🦒"] = 2

print(f'\nEl arca actualmente tiene los siguientes animales: \n{animales}\n')
# Vacía el arca después del diluvio
animales.clear()
print(f'lista vacia: {animales}\n')