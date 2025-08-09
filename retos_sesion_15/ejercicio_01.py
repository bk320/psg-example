# Ejercicio 1

while True:
    cadena = input("Ingrese dos numeros separados por espacio \
(o 'salir' para terminar): ")
    if cadena == "salir":
        print("Saliendo de la calculadora.")
        break
    else:
        cadena = cadena.split()
        try:
            num1 = float(cadena[0])
            num2 = float(cadena[1])
            resultado_suma = num1 + num2
            resultado_resta = num1 - num2
            resultado_division = num1 / num2
            resultado_multiplicacion = num1 * num2
            print("resultado de la suma: ", resultado_suma)
            print("resultado de la resta: ", resultado_resta)
            print("resultado de la multiplicacion: ", resultado_multiplicacion)
            print("resultado de la division: ", resultado_division)
        except ValueError:
            print("Error: Por favor ingrese dos numeros validos.")
        except ZeroDivisionError:
            print("Error: Division por cero no permitida.")
        except Exception as e:
            print("Error inesperado:", e)



