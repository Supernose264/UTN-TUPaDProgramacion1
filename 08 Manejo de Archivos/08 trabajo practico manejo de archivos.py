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

# funcion para cargar productos en diccionarios.
def diccionarios_de_productos():
#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

    productos = {}
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            producto, precio, cantidad = linea.strip().split(",")
            productos[producto] = {"precio": float(precio), "cantidad": int(cantidad)}
    return productos


#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.
def buscar_producto():
    nombre_por_nombre = input("Ingrese el nombre del producto a buscar: ")
    productos = diccionarios_de_productos()
    if nombre_por_nombre in productos:
        datos = productos[nombre_por_nombre]
        print(f"Producto encontrado: {nombre_por_nombre} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")
    else:
        print("Producto no encontrado.")

# Ejecucion de las funciones
agregar_producto()
mostrar_productos()
print(diccionarios_de_productos())
buscar_producto()