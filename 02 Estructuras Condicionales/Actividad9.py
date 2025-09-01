#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles
# #● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Introduce la magnitud del terremoto según la escala de Richter: "))
if magnitud < 3.0:
    categoria = "Muy leve"
elif magnitud < 4.0:
    categoria = "Leve"
elif magnitud < 5.0:
    categoria = "Moderado"
elif magnitud < 6.0:
    categoria = "Fuerte"
elif magnitud < 7.0:
    categoria = "Muy Fuerte"
elif magnitud >= 7.0:
    categoria = "Extremo"
print(f"La magnitud {magnitud} se clasifica como: {categoria}")