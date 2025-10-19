#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            producto, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")



#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

def agregar_producto():
    nombre = input("ingrese el nombre del producto: ")
    precio = input("ingrese el precio del producto: ")
    cantidad = input("ingrese la cantidad del producto: ")
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},${precio},{cantidad}\n")
    print("Producto agregado exitosamente.")

agregar_producto()
mostrar_productos()