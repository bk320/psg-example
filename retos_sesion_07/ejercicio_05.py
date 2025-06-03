# Escribe un programa que reciba una cadena y retorna verdadero o falso si es 
# palindrome sin importar los espacios, mayúsculas o minúsculas

palabra = input("Ingrese una palabra o frase: ")
palabra_minusculas = palabra.lower()
palabra_sin_espacios = palabra_minusculas.replace(" ", "")
palabra_invertida = palabra_sin_espacios[::-1]
palindromo = palabra_sin_espacios == palabra_invertida
print(f"La palabra o frase '{palabra}' es un palíndromo? R: {palindromo}")
print(f"'{palabra_sin_espacios}' => '{palabra_invertida}'")