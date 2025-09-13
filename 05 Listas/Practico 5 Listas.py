import os
import platform
import random
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
print("actividad 1: del 0 al 100")
print("actividad 2: cantidad de digitos en el numero")
print("actividad 3: suma de numeros entre dos valores")
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
if desicio