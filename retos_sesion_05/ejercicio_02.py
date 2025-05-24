# Escribe un programa en Python que convierta las siguientes temperaturas 
# de grados Fahrenheit a grados Celsius:
print("Bienvenido a la calculadora de temperatura")
temp_far_1 = 25
temp_far_2 = 300
temp_far_3 = 76
temp_cel_1 = (temp_far_1-32)*5/9
temp_cel_2 = (temp_far_2-32)*5/9
temp_cel_3 = (temp_far_3-32)*5/9
print(temp_far_1, "grados Fahrenheit son", round(temp_cel_1, 2), "grados Celsius")
print(temp_far_2, "grados Fahrenheit son", round(temp_cel_2, 2), "grados Celsius")
print(temp_far_3, "grados Fahrenheit son", round(temp_cel_3, 2), "grados Celsius")