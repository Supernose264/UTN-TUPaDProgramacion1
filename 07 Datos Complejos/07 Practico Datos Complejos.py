import os
import platform
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)

print("actividad 1,2,3:Diccionario precios_frutas")
print("actividad 4:Contactos telefonicos")
print("actividad 5:Frase unica y contador de palabras")
print("actividad 6:notas de alumnos")
print("actividad 7:Estudiantes que aprobaron parciales")
print("actividad 8:Stock de productos")
print("actividad 9:Agenda de eventos")
print("actividad 10:Diccionario de paises y capitales")
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
    parcial1={1,2,3,4,5,6,7,8,9,10}
    parcial2={5,6,7,8,9,10,11,12,13,14}
    print("Estudiantes que aprobaron ambos parciales: ", parcial1.intersection(parcial2))
    print("Lista total de estudiantes que aprobaron al menos un parcial (sin repetir): ", parcial1.union(parcial2))
    print("Estudiantes que aprobaron solo uno de los dos parciales: ", parcial1.symmetric_difference(parcial2))
elif decision==8:
    #Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
    #Permití al usuario:
    #• Consultar el stock de un producto ingresado.
    #• Agregar unidades al stock si el producto ya existe.
    #• Agregar un nuevo producto si no existe.
    Productos={"Arroz": 10, "Fideos": 15, "Pan": 20, "Leche": 25}
    #Menu de opciones
    while True:
        print("1. consultar stock")
        print("2. Agregar unidades al stock")
        print("3. Agregar un nuevo producto")
        print("4. Salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion==1:
            # ingresa el nombre del producto a consultar
            producto=input("Ingrese el nombre del producto: ")
            #si el producto existe, muestra el stock
            if producto in Productos:
                print(f"El stock de {producto} es: {Productos[producto]}")
            #si el producto no existe, muestra un mensaje
            else:
                print("El producto no existe")
        elif opcion==2:
            #ingresa el nombre del producto al que se le van a agregar unidades
            producto=input("Ingrese el nombre del producto: ")
            #si el producto existe, agrega las unidades al stock
            if producto in Productos:
                unidades=int(input("Ingrese la cantidad de unidades a agregar: "))
                #verifica que las unidades sean positivas
                while unidades<0:
                    print("La cantidad de unidades debe ser positiva")
                    unidades=int(input("Ingrese la cantidad de unidades a agregar: "))
                Productos[producto]+=unidades
                print(f"El nuevo stock de {producto} es: {Productos[producto]}")
            #si el producto no existe, muestra un mensaje
            else:
                print("El producto no existe")
        elif opcion==3:
            #ingresa el nombre del nuevo producto
            producto=input("Ingrese el nombre del nuevo producto: ")
            #si el producto no existe, lo agrega al diccionario
            if producto not in Productos:
                unidades=int(input("Ingrese la cantidad de unidades: "))
                #verifica que las unidades sean positivas
                while unidades<0:
                    print("La cantidad de unidades debe ser positiva")
                    unidades=int(input("Ingrese la cantidad de unidades: "))
                Productos[producto]=unidades
                print(f"El producto {producto} fue agregado con un stock de {unidades}")
            #si el producto ya existe, muestra un mensaje
            else:
                print("El producto ya existe")
        elif opcion==4:
            print("Saliendo...")
            break
elif decision==9:
    #Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
    #Permití consultar qué actividad hay en cierto día y hora
    agenda={}
    #Carga de eventos
    for i in range(3):
        dia=input("Ingrese el dia del evento (formato DD/MM): ")
        hora=input("Ingrese la hora del evento (formato HH:MM): ")
        evento=input("Ingrese el nombre del evento: ")
        #Verifica que el evento no exista
        while (dia, hora) in agenda:
            print("El evento ya existe, ingrese otro")
            dia=input("Ingrese el dia del evento (formato DD/MM): ")
            hora=input("Ingrese la hora del evento (formato HH:MM): ")
            evento=input("Ingrese el nombre del evento: ")
        #Agrega el evento a la agenda
        agenda[(dia, hora)]=evento
    print("Eventos cargados")
    print(agenda)
elif decision==10:
    #Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
    #diccionario donde:
    #• Las capitales sean las claves.
    #• Los países sean los valores
    original ={"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago", "Uruguay": "Montevideo"}
    invertido={}
    for pais, capital in original.items():
        invertido[capital]=pais
    print("Diccionario original: ", original)
    print("Diccionario invertido: ", invertido)
else:
    print("Opcion no valida")