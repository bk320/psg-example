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
            print("resultado de la suma: ", resultado_suma)
            resultado_resta = num1 - num2
            print("resultado de la resta: ", resultado_resta)
            resultado_multiplicacion = num1 * num2
            print("resultado de la multiplicacion: ", resultado_multiplicacion)                      
            try:
                resultado_division = num1 / num2 
                print("resultado de la division: ", resultado_division)
            except ZeroDivisionError:
                print("Error: Division por cero no permitida.")
        except ValueError:
            print("Error: Por favor ingrese dos numeros validos.")
        except Exception as e:
            print("Error inesperado:", e)



