# Ejercicio 5

usuarios = {
    "Juan Perez": "+59112345678",
    "Mark Smith": "+59198765432"
}
nombre_usuario = input("Ingrese el nombre del usuario: ")
numero_telefono = input("Ingrese el número de teléfono: ")
# Para obtener el numero valido de 11 digitos, si es que tiene el prefijo o no
# Que al guardar el contacto se une al numero
numero_valido = numero_telefono[1:] if numero_telefono.startswith("+") \
    else numero_telefono
if nombre_usuario and numero_valido.isdigit() and len(numero_valido) == 11:
    usuarios[nombre_usuario] = "+" + numero_valido
    print("Contacto guardado")
else:
    print("Datos incorrectos")
print(usuarios)