# Ejercicio 2

alimentos = {"carne": ["gato", "perro"], "zanahoria": ["conejo"]}

#Añade al diccionario 4 alimentos más, usando update(clave=valor)
alimentos.update({"maiz": ["gallina", "pato"], 
                  "queso":["raton", "gato", "perro"],
                  "pescado": ["gato", "perro"],
                  "manzana": ["conejo", "loro", "perro"]})

#Existe en el diccionario de alimentos la comida 'trigo'?
respuestas = {False: "No existe trigo en el diccionario de alimentos",
             True: "Existe trigo en el diccionario de alimentos"}
existe = "trigo" in alimentos
print("Existe en el diccionario de alimentos la comida 'trigo'?")
print(respuestas[existe])

#Elimina la comida 'zanahoria' del diccionario de alimentos
zanahoria = alimentos.pop("zanahoria")