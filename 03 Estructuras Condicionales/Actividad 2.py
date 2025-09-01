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
