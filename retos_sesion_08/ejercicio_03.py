# Ejercicio 3
pregunta = str(input("Realiza una pregunta: "))
pregunta = pregunta.capitalize() 
tupla_pre = (pregunta, )
pregunta_completa = ('¿', ) + tupla_pre + ('?', )
print(f"Pregunta completa: {pregunta_completa}")
tupla_repetida = pregunta_completa * 2
print(f"Tupla repetida: {tupla_repetida}")