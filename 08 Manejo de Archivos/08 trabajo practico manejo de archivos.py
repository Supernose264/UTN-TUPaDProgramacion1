import os
import platform
# Esto determina el comando de limpieza según el sistema operativo
CLEAR = "cls" if platform.system() == "Windows" else "clear"
# Esto limpia la terminal para que solo quede el programa a la vista

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

# funcion para buscar productos.
def buscar_producto():
#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.
    nombre_por_nombre = input("Ingrese el nombre del producto a buscar: ")
    productos = diccionarios_de_productos()
    if nombre_por_nombre in productos:
        datos = productos[nombre_por_nombre]
        print(f"Producto encontrado: {nombre_por_nombre} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")
    else:
        print("Producto no encontrado.")


#funcion para guardar productos.
def guardar_productos(productos):
#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.
    with open("productos.txt", "w") as archivo:
        for producto, datos in productos.items():
            archivo.write(f"{producto},{datos['precio']},{datos['cantidad']}\n")
        print("Productos guardados exitosamente.")
#no entendi muy bien este ultimo punto, porque si agrego un producto lo agrega directamente al archivo,
#y si busco no se modifica nada, entonces no hay nada que guardar, pero lo hice igual.

# funcion menu
def menu():
    while True:
        os.system(CLEAR)
        print("== Gestor de Productos ==")
        print("1. Mostrar productos")
        print("2. agregar producto")
        print("3. Buscar producto")
        print("4. Mostrar diccionario de productos")
        print("5. Guardar productos")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ").strip()
        match opcion:
            case "1":
                mostrar_productos()
                input("\nPresione Enter para continuar...")
            case "2":
                agregar_producto()
                input("\nPresione Enter para continuar...")
            case "3":
                buscar_producto()
                input("\nPresione Enter para continuar...")
            case "4":
                print(diccionarios_de_productos())
                input("\nPresione Enter para continuar...")
            case "5":
                guardar_productos(diccionarios_de_productos())
                input("\nPresione Enter para continuar...")
            case "6":
                print("Saliendo.")
                break

# programa principal
menu()