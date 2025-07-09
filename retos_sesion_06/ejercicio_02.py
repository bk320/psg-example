print("Operador XNOR")
a = True
b = True
print(f"a = {a}, b = {b} -> a XNOR b = {not ((a or b) and not (a and b))}")
a = True
b = False
print(f"a = {a}, b = {b} -> a XNOR b = {not ((a or b) and not (a and b))}")
a = False
b = True
print(f"a = {a}, b = {b} -> a XNOR b = {not ((a or b) and not (a and b))}")
a = False
b = False
print(f"a = {a}, b = {b} -> a XNOR b = {not ((a or b) and not (a and b))}")