# Ejercicio 4

habitats_en_peligro = {"polo norte" : {
                            "especies": {"oso polar", "morsa", "ballena"}
                        }, "amazonas" : {
                                "especies": {"tigre", "mono", "guacamayo"}
                        }
                    }
# Añade al diccionario 2 habitats más usando update() con 2 especies cada uno
habitats_en_peligro.update({
    "sabana": {
        "especies": {"elefante", "guepardo", "león", "rinoceronte"}
    },
    "océano": {
        "especies": {"vaquita marina", "delfín", "totoaba", "delfín"}
    }
})

# Existe en el diccionario el habitat 'amazonas'?
respuestas = {
    False: "No, no existe el hábitat 'amazonas' en el diccionario de hábitats en peligro",
    True: "Si, existe el hábitat 'amazonas' en el diccionario de hábitats en peligro"
}
existe = "amazonas" in habitats_en_peligro
print("\nExiste en el diccionario el habitat 'amazonas'?")
print(respuestas[existe])

# Añade al amazonas la especie 'anaconda'
habitats_en_peligro["amazonas"]["especies"].add("anaconda")
print(f'\nhabitats_en_peligro: \n{habitats_en_peligro} \n')