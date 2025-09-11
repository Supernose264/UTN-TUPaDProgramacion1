import os
import platform
import random
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
decision=int(input("Que actividad deseas ver"))
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
if decision == 1:
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
    for i in range (0,100 + 1):
        print(i) 
elif decision == 2:
    #Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
    #dígitos que contiene.
    numero=float(input("escribe un numero"))
    contador = 0
    while numero != 0:
        contador += 1
        numero = numero // 10
    print(f"El número tiene {contador} dígitos")   
elif decision == 3:
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores
    numero_1=int(input("Escribe un primer valor"))
    numero_2=int(input("Escribe un segundo valor"))
    suma = 0
    for i in range (numero_1 + 1,numero_2 ):
        suma = suma + i
    print(f"El resultado de la suma entre los dos valores(Excluyendo ambos valores) es {suma}"  )
elif decision == 4:
#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
    resultado = 0
    numero=int(input("Ingrese un numero:"))
    while numero != 0:
        resultado += numero
        numero=int(input("Ingrese un numero:"))
        print (f"{resultado} + {numero} = {resultado + numero}" )
    print (f"el resultado total es {resultado}")
elif decision == 5:
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
    print("Adivida el numero")
    numero_aleatorio=random.randint(0, 9)
    intentos=0
    while True: 
        intento = int(input("Adivina el número (entre 0 y 9): "))
        intentos += 1
        if intento < numero_aleatorio:
            print("El número es más alto.")
        elif intento > numero_aleatorio:
            print("El número es más bajo.")
        else:
            print(f"¡Felicidades! Lo adivinaste en {intentos} intentos.")
            break
elif decision == 6:
    for i in range (100, -1, -2):
        print (i) 
elif decision == 7:
    print("SUMA ENTRE VALORES")
    numero = int(input("Escriba un número entero positivo: "))
    if numero <= 0:
        print("¡escribi un numero positivo!")
    else:
        suma = 0
        for i in range(0, numero + 1):
            suma = suma + i
        print(f"La suma de los números desde 0 hasta {numero} es {suma}")
else:

    print("ingrese solo los numeros del 1 al 10")
