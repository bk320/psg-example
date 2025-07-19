# Ejercicio 5

usuarios = {
    "Juan Perez": "+59112345678",
    "Mark Smith": "+59198765432"
}
nombre_usuario = input("Ingrese el nombre del usuario: ")
numero_telefono = input("Ingrese el número de teléfono: ")

if 12 == len(numero_telefono) and numero_telefono.startswith("+591"):
    if nombre_usuario:
        usuarios[nombre_usuario] = numero_telefono
        print("Contacto guardado")
    else:
        print("Datos incorrectos")
else:
    print("Datos incorrectos")