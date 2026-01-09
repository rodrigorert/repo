#Crear un programa calculadora que permita sumar, restar, multiplicar y dividir dos numeros
#ejecutar el programa y muestra el resultado de las operaciones
#debe repetirse hasta que el usuario escriba "salir"
   
# Crear una funcion para sumar dos numeros
def sumar(a, b):
    return a + b
# Crear una funcion para restar dos numeros
def restar(a, b):
    return a - b
# Crear una funcion para multiplicar dos numeros
def multiplicar(a, b):
    return a * b
# Crear una funcion para dividir dos numeros
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: No se puede dividir por cero")
    return a / b



while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        print("Sumar")
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        resultado = sumar(a, b)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        print("Restar")
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        resultado = restar(a, b)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        print("Multiplicar")
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        resultado = multiplicar(a, b)
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == "4":
        print("Dividir")
        try:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            resultado = dividir(a, b)
            print(f"El resultado de la division es: {resultado}")
        except ZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(f"Error: Ingrese un numero valido. {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    elif opcion == "5":
        print("Salir")
        break
    else:
        print("Opcion no valida")

 
    