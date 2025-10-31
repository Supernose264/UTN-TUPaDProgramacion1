import os
import platform
# Esto determina el comando de limpieza segun el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"

#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

# función que calcula y muestra factoriales hasta n usando recursividad
def mostrar_factoriales_hasta(n):
    if n < 1:
        print("Ingrese un número entero positivo mayor que 0.")
        return

    def rec(i, prev_fact):
        if i > n:
            return
        if i == 1:
            fact = 1
        else:
            fact = prev_fact * i
        print(f"El factorial de {i} es {fact}")
        rec(i + 1, fact)

    rec(1, 1)


#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

# función recursiva para calcular Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# función que muestra la serie de Fibonacci hasta n usando recursividad
def mostrar_fibonacci_hasta(n):
    if n < 0:
        print("Ingrese un número entero positivo o cero.")
        return

    print("Serie de Fibonacci hasta la posición", n, ":")
    for i in range(n + 1):
        print(f"Posición {i}: {fibonacci(i)}")

#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un algoritmo general.

# funcion recursiva para calcular potencia
def potencia_recursiva(base, exponente):
    # cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Aca aplicamos la fórmula n^m = n * n^(m-1)
    else:
        return base * potencia_recursiva(base, exponente - 1)


#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

# funcion recursiva para convertir decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return 0
    else:
        return str(decimal_a_binario(n // 2)) + str(n % 2)

# funcion del menu principal
def menu():
    while True:
        os.system(CLEAR)
        print("== Menu del trabajo Practico ==")
        print("1. Calcular factoriales")
        print("2. Mostrar serie de Fibonacci")
        print("3. Calcular potencia")
        print("4. Convertir decimal a binario")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ").strip()
        match opcion:
            case "1":
                numero_usuario = int(input("ingrese un numero entero positivo:"))
                mostrar_factoriales_hasta(numero_usuario)
                input("\nPresione Enter para continuar...")
            case "2":
                numero_usuario = int(input("ingrese un numero entero positivo:"))
                mostrar_fibonacci_hasta(numero_usuario)
                input("\nPresione Enter para continuar...")
            case "3":
                base = float(input("Ingrese la base: "))
                exponente = int(input("Ingrese el exponente (entero no negativo): "))
                if exponente < 0:
                    print("El exponente debe ser un entero no negativo.")
                else:
                    resultado= potencia_recursiva(base, exponente)
                    print(f"{base} elevado a la {exponente} es {resultado}")
                input("\nPresione Enter para continuar...")
            case "4":
                numero_usuario = int(input("ingrese un numero entero positivo:"))
                binario = decimal_a_binario(numero_usuario)
                print(f"La representación binaria de {numero_usuario} es: {binario}")
                input("\nPresione Enter para continuar...")
            case "5":
                print("Saliendo.")
                break

menu()