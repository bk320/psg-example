# Ejercicio 6

datos = input('Ingrese la operacion separada por espacios o comas (ejm. 10, 5, +) :')
datos_separados = datos.replace(',', ' ').split()
if datos_separados[0].isdigit() and datos_separados[1].isdigit():
    numero_1 = int(datos_separados[0])
    numero_2 = int(datos_separados[1])
    operador = datos_separados[2].strip()
    if numero_1 and numero_2:
        if operador == '+':
            print('resultado:', numero_1 + numero_2)
    elif operador == '-':
        print('resultado:', numero_1 - numero_2)
    elif operador == '*':
        print('resultado:', numero_1 * numero_2)
    elif operador == '/':
        if numero_2 != 0:
            print('resultado:', numero_1 / numero_2)
        else:
            print("No se puede dividir entre cero")
    else:
        print("Operador no válido")
else:
    print("Datos de entrada no válidos recuerde el formato (ejm. 10, 5, +)")