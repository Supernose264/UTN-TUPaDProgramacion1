import os
import platform
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista
os.system(CLEAR)

# funcion para mostrar los productos.
def mostrar_productos():
    
#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            producto, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")


# funcion para agregar productos.
def agregar_producto():
#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente
    producto = input("ingrese el nombre del producto: ")
    precio = input("ingrese el precio del producto: ")
    cantidad = input("ingrese la cantidad del producto: ")
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{producto},{precio},{cantidad}\n")
    print("Producto agregado exitosamente.")

agregar_producto()
mostrar_productos()