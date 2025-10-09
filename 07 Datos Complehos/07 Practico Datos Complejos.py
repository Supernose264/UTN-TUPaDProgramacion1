import os
import platform
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)

print("actividad 1,2,3:Diccionario precios_frutas")
print("actividad 4:Agenda telefonica")
print("actividad 5:Frase unica y contador de palabras")
print("actividad 6:notas de alumnos")
decision=int(input("Que actividad deseas ver: "))
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
elif decision==5:
    #5) Solicita al usuario una frase e imprime:
    #• Las palabras únicas (usando un set).
    #• Un diccionario con la cantidad de veces que aparece cada palabra
    frase=input("Ingrese una frase: ")
    # Divide la frase en palabras usando el espacio como separador
    palabras=frase.split()
    # Imprime las palabras únicas usando un set
    print("Palabras unicas: ", set(palabras))
    contador_palabras={}
    # Recorre la lista de palabras y cuenta las apariciones
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementa su contador
        if palabra in contador_palabras:
            contador_palabras[palabra]+=1
        # Si la palabra no está en el diccionario, la agrega con contador 1
        else:
            contador_palabras[palabra]=1
    print("Recuento: ", contador_palabras)
elif decision==6:   
    #Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
    #Luego, mostrá el promedio de cada alumno.
    alumnos={}
    for i in range(3):
        nombre=input("Ingrese el nombre del alumno: ")
        while nombre in alumnos:
            print("El alumno ya existem ingrese otro")
            nombre=input("Ingrese el nombre del alumno: ")
        notas=[]
        #Ingresa las 3 notas del alumno
        for j in range(3):
            nota=float(input(f"ingrese la nota {j+1} del alumno {nombre}: "))
            #Verifica que la nota este entre 0 y 10
            while nota<0 or nota>10:
                print("La nota debe estar entre 0 y 10")
                #solicita nuevamente la nota
                nota=float(input(f"ingrese la nota {j+1} del alumno {nombre}: "))
            #se agrega la nota a la lista de notas
            notas.append(nota)
        #se agrega el alumno al diccionario con su tupla de notas
        alumnos[nombre]=tuple(notas)
        os.system(CLEAR)
        #agregar un salto de linea para que se vea mejor
    print("Alumnos y sus notas: ", alumnos,"\n")
    for alumno, notas in alumnos.items():
        promedio=sum(notas)/len(notas)
        print(f"El promedio de {alumno} es: {promedio}")
elif decision==7:
    # Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
    #y Parcial 2:
    #• Mostrá los que aprobaron ambos parciales.
    #• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
    #• Mostrá los que aprobaron solo uno de los dos.
