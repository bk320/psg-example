# Ejercicio 4

while True:
    frase = input("Introduce una frase: ")
    frase_minusculas = frase.lower()
    if "salir" in frase_minusculas:
        break
    else:
        frase_limpia = frase_minusculas.replace(" ", "")
        frase_invertida = frase_limpia[::-1]
        palindromo = frase_limpia == frase_invertida
        if palindromo:
            print("La frase es un palíndromo")
        else:
            print("La frase NO es un palíndromo")