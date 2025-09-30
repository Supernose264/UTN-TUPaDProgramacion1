import os
import platform
import time
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)
print("actividad 1:Funcion Hola Mundo")
decision=int(input("Que actividad deseas ver: "))
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
match decision:
    case 1:
        #Crear una función llamada imprimir_hola_mundo que imprima por
        #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
        #programa principal
        def imprimir_hola_mundo():
            return print("Hola Mundo!")
        
        def imagen_del_mundo():
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

        imagen_del_mundo()
    case 2:
        import time
        #Crear una función llamada saludar_usuario(nombre) que reciba
        #como parámetro un nombre y devuelva un saludo personalizado.
        #Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
        #principal solicitando el nombre al usuario.
        def saludar_usuario(nombre):
            return print(f"Hola {nombre}!")
        def reconociendo(nombre_usuario):
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
            print("bueno, encantado de conocerte, adios")

        nombre=input("¡HELLO! ¿What is your name? ")
        reconociendo(nombre)