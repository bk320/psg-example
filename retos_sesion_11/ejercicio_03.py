# Ejercicio 3

tupla = (('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))
diccionario = dict(tupla)

# Del diccionario obtén y elimina el valor de la clave 'aves'
aves = diccionario.pop("aves")
print(aves)

# Modifica el valor de la clave 'felino' por '🐈'
diccionario["felino"] = "🐈"

# Cambia la clave canino por caninos y su valor por ['🐶','🐕']
diccionario["caninos"] = diccionario["canino"]
del diccionario["canino"]
diccionario["caninos"] = ['🐶', '🐕']

print(diccionario)