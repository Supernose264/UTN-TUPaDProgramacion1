import os
import platform
import random
from statistics import mode, median, mean
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)
decision=int(input("Que actividad deseas ver\n1)¿Eres Mayor de edad?\n2)Nota del usuario\n3)numero par o impar\n4)Categorias de edad\n5)Contraseñas de 8 a 14 caracteres\n6)¿hay sesgo? calculo de numeros aleatorios\n7)frases con o sin vocales\n8)Mayusculas y Minusculas\n9)Magnitudes de terremotos\n10)hemisferios y estaciones\n"))
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
if decision == 1:
    #Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
    #deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
    edad=int(input("ingrese su edad: "))
    if edad>18:
        print("usted es mayor de edad")
elif decision == 2:
    #Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
    #mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
    #mensaje “Desaprobado”.
    calificacion=int(input("ingrese su nota(del 1 al 10): "))
    if calificacion>=6 and calificacion <=10:
        print("Aprobado")
    elif calificacion<6 and calificacion>1:
        print("Desaprobado")
    else:
        print("ingrese un numero del 1 al 10")
elif decision == 3:
    #Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
    #número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
    #contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
    #operador de módulo (%) en Python para evaluar si un número es par o impar.
    numero=float(input("ingrese un numero: "))
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
elif decision == 4:
    # Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
    #siguientes categorías pertenece:
    #● Niño/a: menor de 12 años.
    #● Adolescente: mayor o igual que 12 años y menor que 18 años.
    #● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    #● Adulto/a: mayor o igual que 30 años.
    edad=int(input("Por favor, ingrese su edad: "))
    if edad<12 and edad>0:
        print("Usted es un Niño")
    elif edad>=12 and edad<18:
        print ("Usted es un Adolescente")
    elif edad>=18 and edad<30:
        print("usted es un Adulto Joven")
    elif edad>=30 and edad<120:
        print ("usted es un adulto mayor")
    else:
        print("Por favor,ingrese una edad valida")
elif decision == 5:
    #Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
    #(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
    #pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
    #pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
    #de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
    #como una lista o un string.
    contraseña=input("Introduzca una contraseña,por favor: ")
    if 8<= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
elif decision == 6:
    #escribir un programa que tome la lista
    #numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
    #hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    media = mean(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    moda = mode(numeros_aleatorios)
    if media > mediana > moda:
        sesgo = "positivo"
    elif media < mediana < moda:
        sesgo = "negativo"
    else:
        sesgo = "no hay sesgo"
    print(f"Lista de números aleatorios: {numeros_aleatorios}")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"El sesgo es: {sesgo}")
elif decision == 7:
    #Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
    #termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
    #pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
    #pantalla.
    frase=input("escribe una palabra o una frase: ")
    vocales="AEIOUaeiou"
    if frase and frase[-1] in vocales:
        frase += "!"
    print (frase)
elif decision == 8:
    #Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
    #dependiendo de la opción que desee:
    #1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    #2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    #3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
    nombre=input("Ingresa tu nombre: ")
    num=input("Elige una opción ""\n1: mayúsculas, \n2: minúsculas, \n3: primera letra mayúscula\n")
    if num == '1':
        print(nombre.upper())
    elif num == '2':
        print(nombre.lower())
    elif num == '3':
        print(nombre.title())
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
elif decision == 9:
    #Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
    #magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
    #por pantalla:
    #● Menor que 3: "Muy leve" (imperceptible).
    #● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    #● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
    #generalmente no causa daños).
    #● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
    #débiles
    # #● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    #● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
    magnitud = float(input("Introduce la magnitud del terremoto según la escala de Richter: "))
    if magnitud < 3.0:
        categoria = "Muy leve"
    elif magnitud < 4.0:
        categoria = "Leve"
    elif magnitud < 5.0:
        categoria = "Moderado"
    elif magnitud < 6.0:
        categoria = "Fuerte"
    elif magnitud < 7.0:
        categoria = "Muy Fuerte"
    elif magnitud >= 7.0:
        categoria = "Extremo"
    print(f"La magnitud {magnitud} se clasifica como: {categoria}")
elif decision == 10:
    #Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
    #del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
    #si el usuario se encuentra en otoño, invierno, primavera o verano.
    hemisferio=input("En Cual hemisterio te encuentras""Norte(N) o Sur (S)").upper()
    mes=int(input("Ingresa el número del mes (1-12): "))
    dia=int(input("Ingresa el día del mes: "))
    estacion = ""
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            estacion = "invierno"
        elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            estacion = "primavera"
        elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            estacion = "verano"
        elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
            estacion = "otoño"
    elif hemisferio == 'S':
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            estacion = "verano"
        elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            estacion = "otoño"
        elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            estacion = "invierno"
        elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
            estacion = "primavera"
    print(f"Te encuentras en {estacion}.")
else:
    print("ingrese solo los numeros del 1 al 10")