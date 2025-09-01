#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
nombre=input("Ingresa tu nombre: ")
num=input("Elige una opción ""(1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): ")
if num == '1':
    print(nombre.upper())
elif num == '2':
    print(nombre.lower())
elif num == '3':
    print(nombre.title())
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")