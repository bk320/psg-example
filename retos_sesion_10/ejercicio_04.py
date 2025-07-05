# Ejercicio 4

jane = {"Lemon Pie", "Brownie", "Tarta de Manzana",\
    "Helado de Chocolate", "Flan"}
jhon = {"Carrot Cake", "Croissant de Chocolate",\
    "Lemon Pie", "Tarta de Manzana", "Pudding"}

# Si la cantidad de postres que tienen en común es mayor al 50%
# entonces son compatibles, de lo contrario quieren replantear su relación
platos_comunes = jane & jhon
platos_union = jane | jhon
porcentaje_comun = len(platos_comunes) / len(platos_union) * 100
respuestas = ("Deberían replantear su relación 💔", "¡Son compatibles! 💕")
respuesta = porcentaje_comun > 50
print(f"Porcentaje de platos en común: {porcentaje_comun} %")
# Lo planteo de esta forma para utilizar el booleano como índice
print(respuestas[respuesta])