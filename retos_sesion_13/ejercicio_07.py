# Ejercicio 7

for i in range(1, 101):
    divisible_5 = i % 5 == 0
    divisible_7 = i % 7 == 0
    if divisible_5 and divisible_7:
        print(f"{i} FizzBuzz")
    elif divisible_5:
        print(f"{i} Fizz")
    elif divisible_7:
        print(f"{i} Buzz")