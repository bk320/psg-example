#print("Tipos de datos booleanos")
#print (True)
#print (False)
## Operaciones aritméticas con booleanos
#print (True + True)
#print (True * True)
#print (True * False)
#print (False + False)
#print (False * False)

#print ("Números y booleanos")
#print (10 + True)
#print (10 + False)
#print (10 * True)
#print (10 * False)

#print ("Declarar variables booleanas")
#var_booleana = True
#print (var_booleana)
#print (type(var_booleana))
#var_booleana = False
#print (var_booleana)
#print (type(var_booleana))

#print ("Declarar mediante función bool()")
#var_booleana = bool(1)
#print (var_booleana)
#print (type(var_booleana))
#var_booleana = bool(0)
#print (var_booleana)
#print (type(var_booleana))
#var_booleana = bool(15)
#print (var_booleana)
#print (type(var_booleana))

#print ("Operadores de comparación")
#print (10 == 10)
#print (10 != 10)
#print (10 < 10)
#print (10 > 10)
#print (10 <= 10)
#print (10 >= 10)
#print (10 is 10)
#print (10 is not 10)

#print ("Asignación de variables")
#x = 10
#mayor_que_cero = x > 0
#print (mayor_que_cero)
#diferente_de_10 = x != 10
#print (diferente_de_10)

#print ("Operadores lógicos")
#print (True and True)
#print (True and False)
#print (False or True)
#print (False or False)
#print (not True)
#print (not False)

#print("Operadores lógicos y prioridad")
#print(False and False or True)
#print(False and (False or True))
#print(not True and False or True)
#print(not (True and False or False))
#print(not True and (False or False))
#print(not True and False or False)

#print ("Operador AND")
#print (11>10 and 5>0)
#print (11>10 and 5<0)
#print (5<0 and 11>10)
#print (5<0 and 5<0)

#print ("Operador OR")
#print (10 != 0 or 10 != 0)
#print (10 != 0 or 3 + 5 > 10)
#print (3 + 5 > 10 or 10 != 0)
#print (3 + 5 > 10 or 3 + 5 > 10)

#print ("Operador NOT")
#print (not 10 - 10)
#print (not 17**2)

#print ("Operador NAND")
#print (not (True and True))
#print (not (True and False))
#print (not (False and True))
#print (not (False and False))

#print ("Operador NOR")
#print (not (True or True))
#print (not (True or False))
#print (not (False or True))
#print (not (False or False))

#print ("Operador XOR")
#a = True
#b = False
#print ((a or b) and not (a and b))
#a = True
#b = True
#print ((a or b) and not (a and b))

#print ("Ejemplo de uso Sensor y Batería")
#sensor = True
#bateria = True
#print (sensor, "and", bateria, "=", sensor and bateria)
#sensor = True
#bateria = False
#print (sensor, "and", bateria, "=", sensor and bateria)
#sensor = False
#bateria = True
#print (sensor, "and", bateria, "=", sensor and bateria)
#sensor = False
#bateria = False
#print (sensor, "and", bateria, "=", sensor and bateria)

# ejercicio 1
#num_eval = 20
#lim_inf = 0
#lim_sup = 100
#print(num_eval >= lim_inf and num_eval <= lim_sup)

#ejercico 2
#nota_1 = 15
#nota_2 = 20
#nota_3 = 16
#sumatoria = nota_1 + nota_2 + nota_3
#promedio = sumatoria / 3
#nota_aprobatoria = 51
#print(promedio > nota_aprobatoria)

#numero_eval = 15
#divisor_1 = 3
#divisor_2 = 5
#divisor_3 = 2
#print(numero_eval % divisor_1 == 0 
#      and numero_eval % divisor_2 == 0 
#      and not(numero_eval % divisor_3 == 0)
#      )

#print ("Cortocircuito con operador and")
#x = 3 + 5
#y = 0
#print (x > 2 and (x/y) > 2)
#print (x > 0 and (x/y) > 0)

print ("Cortocircuito con operador or")
x = 1
y = 0
print (x > 0 or (x/y) > 0)
print (x > 2 or (x/y) > 2)