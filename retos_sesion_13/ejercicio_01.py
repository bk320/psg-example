# Ejercicio 1
print("Serie de Lucas")
l_0 = 2
l_1 = 1
print("L (0)",l_0)
print("L (1)",l_1)
for i in range(3, 21):
    l_n = l_0 + l_1
    print("L "+"("+str(i-1)+")", l_n)
    l_0 = l_1
    l_1 = l_n