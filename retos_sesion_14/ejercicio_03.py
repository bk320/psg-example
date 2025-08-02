# Ejercicio 3

def serie_de_lucas(n_esimo):
    if n_esimo == 0:
        return 2
    elif n_esimo == 1:
        return 1
    else:
        return serie_de_lucas(n_esimo - 1) + serie_de_lucas(n_esimo - 2)

print(serie_de_lucas(2))
print(serie_de_lucas(3))
print(serie_de_lucas(4))
print(serie_de_lucas(5))
print(serie_de_lucas(6))