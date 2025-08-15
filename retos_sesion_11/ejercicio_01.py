# Ejercicio 1

animal_marino = {
    "especie": "Tortuga marina",
    "habitat": "Océano",
    "dieta": "Algas, medusas, crustáceos",
    "estado_de_salud": "Buena condición",
    "edad": 15,
    "nombres_responsables": {"Juan", "María", "Carlos"}
}
print(f'especie: {animal_marino["especie"]}')
print(f'habitat: {animal_marino["habitat"]}')
print(f'dieta: {animal_marino["dieta"]}')
print(f'estado de salud: {animal_marino["estado_de_salud"]}')
print(f'edad: {animal_marino["edad"]}')
print(f'nombres responsables: {", ".join(animal_marino["nombres_responsables"])}')