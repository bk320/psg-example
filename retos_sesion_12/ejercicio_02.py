# Ejercicio 2

usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

nombre_usuario = input("Introduce tu nombre de usuario: ")
contrasenia = input("Introduce tu contraseña: ")

if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasenia:
    print("Acceso Aprobado")
else:
    print("Acceso Denegado") 