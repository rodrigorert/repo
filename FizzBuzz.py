#juego FizzBuzz que recorre numeros del 1 al 50 y dice si es divisible por 3, 5 o 3 y 5
#si es divisible por 3, dice "Fizz"
#si es divisible por 5, dice "Buzz"
#si es divisible por 3 y 5, dice "FizzBuzz"
#si no es divisible por 3 ni 5, dice el numero

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
