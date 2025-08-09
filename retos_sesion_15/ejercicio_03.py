# Ejercicio 3

class FondosInsuficientesError(Exception):
    pass

saldo = 700
while True:
    try:
        monto_retiro = (input("Ingrese el monto a retirar \
(o 'salir' para terminar) :"))
        if monto_retiro == 'salir':
            break
        monto_retiro = float(monto_retiro)
        if monto_retiro > 1000:
            raise Exception("El monto excede el límite permitido por transacción")
        if monto_retiro > saldo:
            raise FondosInsuficientesError("No hay fondos suficientes")
        saldo -= monto_retiro
        print(f"Retiro exitoso.\nSaldo restante: {saldo}")
    except FondosInsuficientesError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)