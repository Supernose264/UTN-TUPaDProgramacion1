import os
import platform
import random
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)
print("actividad 1: listas de promedios)
print("actividad 2: Lista de productos")
print("actividad 3: Lista de numeros al azar")
print("actividad 4: suma en secuencia")
print("actividad 5: adivina el numero")
print("actividad 6: numeros pares del 0 al 100")
print("actatoria entre 0 y un valor dado")
print("actividad 8:100 numeros:pares,impares,negativos, positivos y ceros")
print("actividad 9:100 numeros:media de valores")
print("actividad 10: invertir numeros")
decision=int(input("Que actividad deseas ver: "))
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
if decision = 1:
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
elif decision = 2:
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
elif decision = 3:
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
else:
