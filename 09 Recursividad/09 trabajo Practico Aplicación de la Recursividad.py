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
#Ejemplo:
#Convertir el número 10 a binario:
#10 ÷ 2 = 5 resto: 0
#5 ÷ 2 = 2 resto: 1
#2 ÷ 2 = 1 resto: 0
#1 ÷ 2 = 0 resto: 1
#Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

# funcion recursiva para convertir decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return str(decimal_a_binario(n // 2)) + str(n % 2)
    
#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

# funcion recursiva para verificar si una palabra es palindromo
def es_palindromo(palabra): 
    if len(palabra) <= 1:
        return True

    # Si los extremos son distintos, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False

    # Llamada recursiva sobre la subcadena sin los extremos
    return es_palindromo(palabra[1:-1])


#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        # Llamada recursiva sumando el dígito menos significativo
        return (n % 10) + suma_digitos(n // 10)
    
#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
#Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


# funcion del menu principal
def menu():
    while True:
        os.system(CLEAR)
        print("== Menu del trabajo Practico ==")
        print("1. Calcular factoriales")
        print("2. Mostrar serie de Fibonacci")
        print("3. Calcular potencia")
        print("4. Convertir decimal a binario")
        print("5. Verificar palíndromo")
        print("6. Sumar dígitos de un número")
        print("7. Contar bloques para pirámide")
        print("8. Salir")
        opcion = input("Seleccione una opción (1-6): ").strip()
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
                palabra = input("Ingrese una palabra sin espacios ni tildes: ").strip()
                if es_palindromo(palabra):
                    print(f'"{palabra}" es un palíndromo.')
                else:
                    print(f'"{palabra}" no es un palíndromo.')
                input("\nPresione Enter para continuar...")
            case "6":
                numero_usuario = int(input("ingrese un numero entero positivo:"))
                suma = suma_digitos(numero_usuario)
                print(f"La suma de los dígitos de {numero_usuario} es: {suma}")
                input("\nPresione Enter para continuar...")
            case "7":
                numero_usuario = int(input("ingrese un numero entero positivo:"))
                total_bloques = contar_bloques(numero_usuario)
                print(f"El total de bloques necesarios para una pirámide con {numero_usuario} bloques en la base es: {total_bloques}")
                input("\nPresione Enter para continuar...")
            case "8":
                print("Saliendo.")
                break

menu()