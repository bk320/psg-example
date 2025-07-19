# Ejercicio 4

edad_cliente = int(input("Introduce la edad del cliente: "))
monto_compra = int(input("Introduce el importe de la compra: "))

rebaja_caso1 = edad_cliente > 60 and monto_compra > 1000
rebaja_caso2 = edad_cliente > 18 and edad_cliente <= 60 and monto_compra > 500

if rebaja_caso1:
    monto_final = round(monto_compra * 0.8, 2)
    print("Se aplica una rebaja del 20%, monto a pagar:", monto_final)
elif rebaja_caso2:
    monto_final = round(monto_compra * 0.9, 2)
    print("Se aplica una rebaja del 10%, monto a pagar:", monto_final)
else:
    monto_final = round(monto_compra * 0.98, 2)
    print("Rebaja del 2%, monto a pagar:", monto_final)