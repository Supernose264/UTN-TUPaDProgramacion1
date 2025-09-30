import os
import platform
import time
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)

print("actividad 1:Funcion Hola Mundo")
print("actividad 2:Funcion Saludar Usuario")
print("actividad 3:Funcion Informacion Personal")
print("actividad 4:Funciones Area y Perimetro de un Circulo")
print("actividad 5:Funcion Segundos a Horas")
print("actividad 6:Funcion Tabla de Multiplicar")
print("actividad 7:Funcion Operaciones Basicas")
print("actividad 8:Funcion Calcular IMC")
print("actividad 9:Funcion Celsius a Fahrenheit")
print("actividad 10:Funcion Calcular Promedio")
decision=int(input("Que actividad deseas ver: "))
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
match decision:
    case 1:
        #Crear una función llamada imprimir_hola_mundo que imprima por
        #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
        #programa principal

        #deficion de funciones
        def imprimir_hola_mundo():
            #imprime hola mundo
            return print("Hola Mundo!")
        
        def imagen_del_mundo():
            #imprime una imagen del mundo en codigo ascii
            imprimir_hola_mundo()
            input("Presiones enter para continuar...")
            CLEAR = "cls" if platform.system() == "Windows" else "clear"
            os.system(CLEAR)
            print("               _v->#H#P? ':o<>\_    ")
            print("          .,dP` `''  \"'-o.+H6&MMMHo_    ")
            print("        oHMH9'         `?&bHMHMMMMMMHo.    ")
            print("      oMP"' '           "ooMP*&HMMMMMMM?.    ")
            print("    ,M*          -     `*MSdob//`^&##MMMH\    ")
            print("   d*'                .,MMMMMMH#o>#ooMMMMMb    ")
            print("  HM-                :HMMMMMMMMMMMMMMM&HM[R\    ")
            print(" d"".                9MMMMMMMMMMMMMMMMM[HMM|:    ")
            print("-H    -              MMMMMMMMMMMMMMMMMMMbMP' :    ")
            print(":??Mb#               `9MMMMMMMMMMMMMMMMMMH#! .    ")
            print(": MMMMH#,              """"""""HMMMMMMMMMMH  -    ")
            print("||MMMMMM6\.                    {MMMMMMMMMH'  :    ")
            print(":|MMMMMMMMMMHo                 `9MMMMMMMM'   .    ")
            print(". HMMMMMMMMMMP'                 !MMMMMMMM    `    ")
            print("- `#MMMMMMMMM                   HMMMMMMM*,/  :    ")
            print(" :  ?MMMMMMMF                   HMMMMMM',P' :    ")
            print("  .  HMMMMR'                    {MMMMP' ^' -    ")
            print("   : `HMMMT                     iMMH'     .'    ")
            print("    -.`HMH                               .    ")
            print("      -:*H                            . '    ")
            print("        -`\,,    .                  .-    ")
            print("          ' .  _                 .-`    ")
            print("              '`~\.__,obb#q==~'''    ")

        #Programa principal
        imagen_del_mundo()

    case 2:
        import time
        #Crear una función llamada saludar_usuario(nombre) que reciba
        #como parámetro un nombre y devuelva un saludo personalizado.
        #Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
        #principal solicitando el nombre al usuario.

        #definicion de funciones
        def saludar_usuario(nombre):
            #saluda al usuario
            return print(f"Hola {nombre}!")
        
        def reconociendo_al_usuario(nombre_usuario):
            #reconoce al usuario
            saludar_usuario(nombre_usuario)
            time.sleep(2)
            for i in range(2):
                print("emm... let me see.")
                time.sleep(1)
                CLEAR = "cls" if platform.system() == "Windows" else "clear"
                os.system(CLEAR)
                print("emm... let me see..")
                time.sleep(1)
                CLEAR = "cls" if platform.system() == "Windows" else "clear"
                os.system(CLEAR)
                print("emm... let me see...")
                time.sleep(1)
                CLEAR = "cls" if platform.system() == "Windows" else "clear"
                os.system(CLEAR)
            print("¿vos no sos ese que...")
            time.sleep(2)
            print("emm...")
            time.sleep(2)
            print("No, nada, perdon")
            time.sleep(1)
            print(f"bueno, encantado de conocerte {nombre}, adios")

        #Programa principal
        nombre=input("¡HELLO! ¿What is your name? ")
        reconociendo_al_usuario(nombre)
    case 3:
        #Crear una función llamada informacion_personal(nombre, apellido,
        #edad, residencia) que reciba cuatro parámetros e imprima: “Soy
        #[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

        #definicion de funciones
        def informacion_personal(nombre, apellido, edad, residencia):
            #imprime la informacion personal del usuario
            return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
        
        def recopilando_datos():
            #recopila los datos del usuario
            nombre=input("Cual es tu nombre? ")
            apellido=input("Cual es tu apellido? ")
            edad =input("Cuantos años tienes? ")
            while not edad.isdigit():
                print("Por favor, ingresa un número válido para la edad.")
                edad =input("Cuantos años tienes? ")
            residencia=input("Donde vives? ")
            informacion_personal(nombre, apellido, edad, residencia)

        #Programa principal
        recopilando_datos()

    case 4:
        #Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
        #calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
        # Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
        from math import pi

        #definicion de funciones
        def calcular_area_circulo(radio):
            #calcula el area del circulo
            return pi * radio ** 2
        
        def calcular_perimetro_circulo(radio):
            #calcula el perimetro del circulo
            return 2* pi * radio
        
        def Solicitar_radio():
            #solicita el radio al usuario
            radio=float(input("Dime cual es el radio del circulo: "))
            print(f"El area del circulo es: {calcular_area_circulo(radio)}")
            print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")  
        
        #Programa principal
        Solicitar_radio()
    
    case 5:
        #Crear una función llamada segundos_a_horas(segundos) que reciba
        #una cantidad de segundos como parámetro y devuelva la cantidad
        #de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
        
        #definicion de funciones
        def segundos_a_horas(segundos):
            #convierte segundos a horas, minutos y segundos
            return segundos / 3600
        
        def segundos_a_minutos(segundos):
            #convierte segundos a minutos y segundos
            return segundos / 60
        
        def Solicitar_segundos():
            #solicita los segundos al usuario
            segundos=int(input("Dime cuantos segundos quieres convertir: "))
            print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas")
            print(f"{segundos} segundos son {segundos_a_minutos(segundos)} minutos")

        #Programa principal
        Solicitar_segundos()

    case 6:
        #Crear una función llamada tabla_multiplicar(numero) que reciba un
        #número como parámetro y imprima la tabla de multiplicar de ese
        #número del 1 al 10. Pedir al usuario el número y llamar a la función.

        #definicion de funciones
        def tabla_multiplicar(numero):
            #imprime la tabla de multiplica del numero ingresado
            print(f"Tabla de multiplicar del numero {numero}")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")

        def Solicitar_numero():
            #solicita un numero al usuario
            numero=int(input("Dime un numero y te dare su tabla de multiplicar: "))
            tabla_multiplicar(numero)

        #Programa principal
        Solicitar_numero()

    case 7:

        #definicion de funciones
        def operaciones_basicas(a, b):
            #realiza operaciones basicas entre dos numeros
            suma = a + b
            resta = a - b
            multiplicacion = a * b
            division = a / b if b != 0 else "Indefinida (division por cero)"
            return suma, resta, multiplicacion, division
        
        def Solicitar_numeros():
            #solicita dos numeros al usuario
            a=float(input("Dime el primer numero: "))
            b=float(input("Dime el segundo numero: "))
            print(f"Suma: {a} + {b} = {operaciones_basicas(a, b)[0]}")
            print(f"Resta: {a} - {b} = {operaciones_basicas(a, b)[1]}")
            print(f"Multiplicacion: {a} * {b} = {operaciones_basicas(a, b)[2]}")
            print(f"Division: {a} / {b} = {operaciones_basicas(a, b)[3]}")
            
        #Programa principal
        Solicitar_numeros()

    case 8:
        #Crear una función llamada calcular_imc(peso, altura) que reciba el
        #peso en kilogramos y la altura en metros, y devuelva el índice de
        #masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

        #definicion de funciones
        def calcular_imc(peso, altura):
            #calcula el indice de masa corporal
            return peso / (altura ** 2)
        
        def solicitar_datos():
            #solicita peso en kilogramos y altura en metros
            peso=float(input("Dime el peso en kilogramos: "))
            altura=float(input("Dime la altura en metros: "))
            print(f"El indice de masa corporal es: {calcular_imc(peso, altura)}")

        #Programa principal
        solicitar_datos()

    case 9:
        #Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
        #una temperatura en grados Celsius y devuelva su equivalente en
        #Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
        #resultado usando la función.

        #definicion de funciones
        def celsius_a_fahrenheit(celsius):
            #convierte celsius a fahrenheit
            return (celsius * 9/5) + 32
        
        def celsius_a_kelvin(celsius):
            #convierte celsius a kelvin
            return celsius + 273.15
        
        def solicitar_temperatura():
            #solicita la temperatura en celsius al usuario
            celsius=float(input("Dime la temperatura en grados celsius: "))
            print(f"{celsius} grados celsius son {celsius_a_fahrenheit(celsius)} grados fahrenheit")
            print(f"{celsius} grados celsius son {celsius_a_kelvin(celsius)} grados kelvin")

        #Programa principal
        solicitar_temperatura()

    case 10:
        #Crear una función llamada calcular_promedio(a, b, c) que reciba
        #tres números como parámetros y devuelva el promedio de ellos.
        #Solicitar los números al usuario y mostrar el resultado usando esta función.

        #definicion de funciones
        def calcular_promedio(a, b, c):
            #calcula el promedio de tres numeros
            return (a + b + c) / 3
        
        def solicitar_numeros():
            #solicita tres numeros al usuario
            a=float(input("Dime el primer numero: "))
            b=float(input("Dime el segundo numero: "))
            c=float(input("Dime el tercer numero: "))
            print(f"El promedio de {a}, {b} y {c} es: {calcular_promedio(a, b, c)}")

        #Programa principal 
        solicitar_numeros()