# Ejercicio 2
class FrutaError(Exception):
    pass

frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
canasta = []
while True:
    try:
        fruta = input("Ingrese una fruta (o 'salir' para terminar): ")
        if fruta == "salir":
            break
        if fruta not in frutas_permitidas:
            raise FrutaError("Fruta no permitida")
        canasta.append(fruta)
    except FrutaError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Fruta agregada")
    finally:
        print("Canasta:", canasta)