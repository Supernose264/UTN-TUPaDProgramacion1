import os
import platform
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
    Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
    dígitos que contiene.
 
    
else:
    print("ingrese solo los numeros del 1 al 10")
