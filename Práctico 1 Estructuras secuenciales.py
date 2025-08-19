import math
print("Práctico 1: Estructuras secuenciales")
opcion =int(input("Que actividad desea ver "))
if opcion == 1:
        print("hola mundo")
elif opcion == 2:
    #Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
    # el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
    # por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
    # realizar la impresión por pantalla.
        nombre=input("¿Cual es tu nombre? ")
        print(f"Hola {nombre}")
elif opcion == 3:
    #Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
    # imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
    # “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
    # años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
        nombre=input("¿Cual es tu nombre? ")
        edad=int(input("¿Cuantos años tienes? "))
        residencia=input("¿En que pais reside ahora mismo? ")
        print(f"hola soy {nombre} tengo {edad} años y vivo en {residencia}")
elif opcion == 4:
    #Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
    #su perímetro.
        pi = math.pi
        radio=int(input("escribe el radio de un circulo. "))
        perimetro=2*pi*radio
        area=pi*radio**2
        print(f"el perimetro del circulo es {perimetro} y el area es {area}")
elif opcion == 5:
    #Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
    #cuántas horas equivale.
        segundos=int(input("escribe una cantidad de segundos "))
        horas=segundos/3600
        print(f"{segundos} segundos equivale a {horas} horas ")
elif opcion == 6:
    # Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
        num=int(input("Ingrese un numero. "))
        for i in range (1,11):
            resultado = num * i
            print(f"{num} x {i} = {resultado}")
elif opcion == 7:
    #  Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre 
    #  por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
        numero1=int(input("escribe el primer numero (debe de ser diferente a 0):"))
        numero2=int(input("escribe el segundo numero (debe de ser diferente a 0):"))
        if numero1 == 0 or numero2 == 0:
            print("!!!ERROR¡¡¡: Ningún número debe ser cero.")
        else:
            suma = numero1 + numero2
            resta = numero1 - numero2
            multiplicacion = numero1 * numero2
            division = numero1 / numero2
            print(f"Suma entre {numero1} y {numero2}: {suma}")
            print(f"Resta entre {numero1} y {numero2}: {resta}")
            print(f"Multiplicación entre {numero1} y {numero2}: {multiplicacion}")
            print(f"División entre {numero1} y {numero2}: {division}")
elif opcion == 8:
    #Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
    # Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC= peso en kg/(altura en m)**2
        print("calculadora de indice de masa corporal")
        peso_kg=int(input("ingrese su peso en kilogramos:"))
        altura_m=int(input("ingrese su altura en metros:"))
        IMC=peso_kg/(altura_m)**2
        print(f"su indice de masa corporal es {IMC}")
elif opcion == 9:
    # Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
    # pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
    # 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
        celsius=int(input("ingrese una temperatura en grado celsius(°C):"))
        fahrenheit=(9/5)*celsius+32
        print(f"{celsius}°C son {fahrenheit}°F")
elif opcion == 10:
    #Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
    #dichos números.
        numero1=int(input("ingrese el primer numero:"))
        numero2=int(input("ingrese el segundo numero:"))
        numero3=int(input("ingrese el tercer numero:"))
        promedio=(numero1+numero2+numero3)/3
        print(f"el promedio de esos numeros es {promedio}")
else:
    print("Hasta luego")

