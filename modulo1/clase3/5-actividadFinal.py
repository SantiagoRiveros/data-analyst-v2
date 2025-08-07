#Crear un programa que almacene información sobre productos en un inventario y permita consultar detalles por su código.

inventario = {
    "A101": {"nombre": "Laptop", "precio": 1000, "stock": 5},
    "B202": {"nombre": "Mouse", "precio": 50, "stock": 35},
    "C303": {"nombre": "Teclado", "precio": 110, "stock": 9}
}

codigo = input("Ingrese el codigo del producto: ")

if codigo in inventario:
    producto = inventario[codigo]
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: {producto['precio']}")
    print(f"Stock: {producto['stock']}")
else:
    print("Producto no encontrado")
    
def consultarProducto(codigoProducto, inventarioProductos):
    if codigoProducto in inventarioProductos:
        productoSeleccionado = inventarioProductos[codigoProducto]
        print(f"Nombre: {productoSeleccionado['nombre']}")
        print(f"Precio: {productoSeleccionado['precio']}")
        print(f"Stock: {productoSeleccionado['stock']}")
    else:
        print("Producto no encontrado")
        
consultarProducto(codigo, inventario)