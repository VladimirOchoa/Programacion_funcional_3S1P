def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def mi_calculadora(opcion, num1, num2):
    if opcion == '1':
        return suma(num1, num2)
    elif opcion == '2':
        return resta(num1, num2)
    elif opcion == '3':
        return multiplicacion(num1, num2)
    elif opcion == '4' and num2 != 0:
        return division(num1, num2)
    else:
        return "Opción no válida"

while True:
    print("\nMi Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '5':
        print("¡Gracias por usar Mi Calculadora!")
        break
    elif opcion < '1' or opcion > '5':
        print("Opción no válida")
    else:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = mi_calculadora(opcion, num1, num2)
        print("Resultado:", resultado)