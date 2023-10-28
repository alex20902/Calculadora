# Operación para realizar suma
def sumar(x, y):
    return x + y

# Operación para realizar una resta
def restar(x, y):
    return x - y

# Operación para realizar una multiplicación
def multiplicar(x, y):
    return x * y

# Operación para realizar una división
def dividir(x, y):
    if y == 0:
        return "No se puede dividir por cero"
    return x / y

while True:
    print("Operaciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elija una opción para realizar la operacion (1/2/3/4/5): ")

    if opcion == '5':
        print("¡Adiós!")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", sumar(num1, num2))
    elif opcion == '2':
        print("Resultado:", restar(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opción no válida")
