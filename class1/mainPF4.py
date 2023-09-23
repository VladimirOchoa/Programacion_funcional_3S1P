def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "No se puede dividir entre cero"

def mi_calculadora(opcion, num1, num2):
    return (
        suma(num1, num2) if opcion == '1'
        else resta(num1, num2) if opcion == '2'
        else multiplicacion(num1, num2) if opcion == '3'
        else division(num1, num2) if opcion == '4' and num2 != 0
        else "Opción no válida"
    )

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