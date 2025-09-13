import os
import platform
import random
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)
print("actividad 1: listas de promedios")
print("actividad 2: Lista de productos")
print("actividad 3: Lista de numeros al azar")
print("actividad 4: Numeros repetidos")
print("actividad 5: Estudiantes en clase")
print("actividad 6: Rotar numeros de una lista")
print("actividad 7: Lista de temperaturas minimas y maximas")
print("actividad 8:100 numeros:pares,impares,negativos, positivos y ceros")
print("actividad 9:100 numeros:media de valores")
print("actividad 10: invertir numeros")
decision=int(input("Que actividad deseas ver: "))
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
if decision == 1:
    #Crear una lista con las notas de 10 estudiantes.
    #• Mostrar la lista completa.
    #• Calcular y mostrar el promedio.
    #• Indicar la nota más alta y la más baja.
    lista_promedio= [7.5, 8.0, 6.3, 9.2, 5.8, 7.0, 8.5, 6.9, 9.8, 4.7]
    #suma los numeros y los divide por la cantidad de valores que hay en la lista
    promedio = sum(lista_promedio) / len(lista_promedio)
    #se imprime el promedio
    print(f"El promedio total de las notas es {promedio} ")
    #se imprime el menor numero de la lista
    print((f"La nota mas baja es {min(lista_promedio)}"))
    # se imprime el mayor numero de la lista
    print((f"La nota mas alta es {max(lista_promedio)}"))     
elif decision == 2:
    #Pedir al usuario que cargue 5 productos en una lista.
    #• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
    #• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
    #Lista de los productos
    productos = []
    #el usuario ingresa 5 producto (el loop ocurre 5 veces)
    for i in range(5):
        #el usuario ingresa un producto
        producto = input(f"Ingrese el nombre del producto {i+1}: ")
        #el producto del usuario se agrega a la lista
        productos.append(producto)
    #La lista "productos" se ordena alfabeticamente
    productos_ordenados = sorted(productos)
    #Se imprime el mensaje de los productos ordenados, en filas
    print("\nLista de productos ordenada alfabéticamente:")
    for p in productos_ordenados:
        print(f"- {p}")
    #se le pregunta al usuario que producto desea eliminar
    decision =str(input("\n¿Desea eliminar un producto?SI/NO: "))
    Mayuscula = decision.upper()
    if Mayuscula == "SI":
        #El usuario ingresa el producto que quiere eliminar
        eliminar = input("\n ¿Qué producto desea eliminar?: ")
        #Se Verifica si el producto está en la lista y eliminarlo
        if eliminar in productos:
            productos.remove(eliminar)
            print(f"\nProducto '{eliminar}' eliminado correctamente.")
        else:
            print(f"\nEl producto '{eliminar}' no se encuentra en la lista.")
        #se actualiza la lista con el producto eliminado
        productos_actualizados = sorted(productos)
        print("\nLista actualizada de productos:")
        for p in productos_actualizados:
            print(f"- {p}")
    else:
        print("\n¡Hasta la proxima!")
elif decision == 3:
    #Generar una lista con 15 números enteros al azar entre 1 y 100.
    #• Crear una lista con los pares y otra con los impares.
    #• Mostrar cuántos números tiene cada lista.    
    pares = []
    impares = []
    # Se genera una lista con 15 numeros aleatorios
    numeros = [random.randint(1, 100) for _ in range(15)]
    #se imprime la lista original con todos los numeros
    print (f"\nLista de numeros \n{numeros}")
    # se buscan los numeros pares e impares de la lista
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    #se imprimen las listas pares e impares
    print(f"\nLista de numeros pares\n{pares}")
    print(f"\nLista de numeros impares\n{impares}")
elif decision == 4:
    #Dada una lista con valores repetidos:
    #datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
    #• Crear una nueva lista sin elementos repetidos.
    #• Mostrar el resultado
    datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
    #se eliminan los valores repetidos
    lista_sin_repeticiones=list(set(datos))
    #se imprime la lista original
    print(f"\nLista original \n{datos}")
    #se imprime la lista sin repeticiones
    print(f"\nLista sin datos repetidos \n{lista_sin_repeticiones}")
elif decision == 5:
#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.
#Lista de estudiantes
    estudiantes = ["Lucía", "Mateo", "Sofía", "Tomás", "Valentina", "Julián", "Camila", "Agustín"]
    #se imprime la lista de estudiantes
    print(f"\nLista de estudiantes\n{estudiantes}")
    #se imprimen en filas los nombres de cada estudiantes
    for nombre in estudiantes:
        print(f"- {nombre}")
    # Se le pregunta al usuario si quiere agregar o eliminar a algun alumno
    accion = input("\n¿Deseás agregar un nuevo estudiante o eliminar uno existente? (escribí 'agregar' o 'eliminar'): ").lower()
    # Agregar estudiante
    if accion == "agregar":
        # el usuario ingresa el nombre del estudiante que quiere agregar
        nuevo = input("Ingresá el nombre del nuevo estudiante: ")
        #el nombre se agrega a la lista
        estudiantes.append(nuevo)
        # se notifica al usuario que se agrego al estudiante
        print(f"\n'{nuevo}' fue agregado a la lista.")
    # Eliminar estudiante
    elif accion == "eliminar":
        # el usuario ingresa el nombre del estudiante que quiere eliminar
        eliminar = input("Ingresá el nombre del estudiante que querés eliminar: ")
        #se verifica si el estudiante esta en la lista
        if eliminar in estudiantes:
            #se elimina al estudiante
            estudiantes.remove(eliminar)
            # se notifica al usuario que se elimino al estudiante
            print(f"\n'{eliminar}' fue eliminado de la lista.")
        #si el estudiante no esta en la lista se le notifica al usuario
        else:
            print(f"\n'{eliminar}' no se encuentra en la lista.")
    # Opción inválida
    else:
        print("\nOpción no reconocida. Por favor escribí 'agregar' o 'eliminar'.")
    # Se imprime la lista actualizada mostrando por fila el nombre de cada alumno
    print("\nLista actualizada de estudiantes:")
    for nombre in estudiantes:
        print(f"- {nombre}")    
elif decision == 6:
    #Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
    #último pasa a ser el primero).
    lista= [1, 2, 3, 4, 5, 6, 7]
    #se extrae el ultimo valor de la lista para luego concatenarle con la misma lista sin el ultimo valor
    lista = [lista[-1]] + lista[:-1]
    #se imprime la lista
    print (lista)
elif decision == 7:
    #Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
    #semana.
    #• Calcular el promedio de las mínimas y el de las máximas.
    #• Mostrar en qué día se registró la mayor amplitud térmica.
    # Lista anidada con las temperaturas minimas y maximas que hubo por dia
    temperaturas_con_dias = [
        ("Lunes",    [12, 24]),
        ("Martes",   [13, 25]),
        ("Miércoles",[11, 22]),
        ("Jueves",   [14, 26]),
        ("Viernes",  [15, 27]),
        ("Sábado",   [10, 21]),
        ("Domingo",  [9, 20])
    ]
    # se crea dos listas separadas con los valores minimos por un lado y los valores maximos por el otro
    minimas = [dia[1][0] for dia in temperaturas_con_dias]
    maximas = [dia[1][1] for dia in temperaturas_con_dias]
    # se canculan los promedios de cada lista
    promedio_minimas = sum(minimas)  / len(minimas)
    promedio_maximas = sum(maximas) / len(maximas)
    # Se usa max() con el parámetro key para comparar por la temperatura máxima (x[1][1]), para obtener el dia en el que hubo la mayor tempertura y extraerlo de la lista con [0]
    dia_mayor_maxima = max(temperaturas_con_dias, key=lambda x: x[1][1])[0]
    # Se calculan las amplitudes termicar para encontrar el día con mayor amplitud
    amplitudes = [[dia[0], dia[1][1] - dia[1][0]] for dia in temperaturas_con_dias]
    #Se usa max() sobre la lista amplitudes para compara por el segundo valor de cada lista (x[1]), que es la amplitud.
    dia_mayor_amplitud = max(amplitudes, key=lambda x: x[1])
    # Se se imprimen los resultados
    print(f"\nEl promedio de temperaturas mínimas fue: {promedio_minimas:.2f}°C")
    print(f"\nEl promedio de temperaturas máximas fue: {promedio_maximas:.2f}°C")
    print(f"\nEl día con la mayor temperatura máxima fue: {dia_mayor_maxima}")
    print(f"\nEl día con mayor amplitud térmica fue: {dia_mayor_amplitud[0]} con una diferencia de {dia_mayor_amplitud[1]}°C")    
elif decision == 8:
    #Crear una matriz con las notas de 5 estudiantes en 3 materias.
    #• Mostrar el promedio de cada estudiante.
    #• Mostrar el promedio de cada materia.
    # Lista anidada de las notas: cada fila es un estudiante, cada columna una materia
    notas = [        
        [7, 8, 9],  # Estudiante 1
        [6, 7, 8],  # Estudiante 2
        [9, 9, 10], # Estudiante 3
        [5, 6, 7],  # Estudiante 4
        [8, 7, 9]   # Estudiante 5
    ]
    #loop para que las notas se promedien una por una
    for i, estudiante in enumerate(notas, start=1):
        #se calcula el promedio del estudiante
        promedio = sum(estudiante) / len(estudiante)
        #se imprime
        print(f"\nPromedio del Estudiante {i}: {promedio:.2f}")
    #espacio vacio
    print()
    #la cantidad de materias que hay
    num_materias = len(notas[0])
    #se calcula el promedio de los estudiantes
    for j in range(num_materias):
        suma_materia = sum(estudiante[j] for estudiante in notas)
        promedio_materia = suma_materia / len(notas)
        print(f"\nPromedio de la Materia {j + 1}: {promedio_materia:.2f}")

else:
    print("hola")
