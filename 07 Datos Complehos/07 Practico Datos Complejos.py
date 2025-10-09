import os
import platform
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)

print("actividad 1,2,3:Diccionario precios_frutas")

decision=int(input("Que actividad deseas ver: "))
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
if decision==1 or decision==2 or decision==3:
    #1) Dado el diccionario precios_frutas
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
    1450}
    #Añadir las siguientes frutas con sus respectivos precios:
    #● Naranja = 1200
    #● Manzana = 1500
    #● Pera = 2300
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    
    print("lista con los frutas añadidas\n", precios_frutas ,"\n____________________________________________________________")

    #2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
    #desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
    #● Banana = 1330
    #● Manzana = 1700
    #● Melón = 2800
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    print("Lista con los precios Actualizados\n", precios_frutas ,"\n____________________________________________________________")

    #3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
    #desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
    print("Lista con solo las fritas sin los precios\n", list(precios_frutas.keys()))
elif decision==4:
    #4) Escribí un programa que permita almacenar y consultar números telefónicos.
    #• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
    #• Luego, pedí un nombre y mostrale el número asociado, si existe.
    contactos={}
    #Carga de contactos
    for i in range(5):
        nombre=input("ingrese el nombre del contacto: ")
        #Verifica que el contacto no exista
        while nombre in contactos:
            print("El contacto ya existe, ingrese otro")
            nombre=input("ingrese el nombre del contacto: ")
        numero=int(input("ingrese el numero del contacto(debe tener 8 digitos):"))
        #Verifica que el numero tenga 8 digitos
        while len(str(numero))!=8:
            print("El numero debe tener 8 digitos, ingrese otro")
            numero=int(input("ingrese el numero del contacto(debe tener 8 digitos):"))
        #Verifica que el numero no exista
        while numero in contactos.values():
            print("El numero ya existe, ingrese otro")
            numero=int(input("ingrese el numero del contacto(debe tener 8 digitos):"))
        #Agrega el contacto al diccionario
        contactos[nombre]=numero
    print("Contactos cargados")
    print(contactos)
