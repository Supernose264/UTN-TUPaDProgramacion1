#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
frase=input("escribe una palabra o una frase: ")
vocales="AEIOUaeiou"
if frase and frase[-1] in vocales:
    frase += "!"
print (frase)

