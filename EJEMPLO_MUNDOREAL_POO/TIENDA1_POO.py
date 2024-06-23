# tienda.py

class Producto:
    def __init__(self, nombre, precio, cantidad):
        # Inicializa los atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        # Muestra la información del producto
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

    def actualizar_cantidad(self, cantidad):
        # Actualiza la cantidad del producto
        self.cantidad += cantidad


class Tienda:
    def __init__(self, nombre):
        # Inicializa los atributos de la tienda
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega un producto a la lista de productos de la tienda
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la tienda {self.nombre}.")

    def vender_producto(self, nombre_producto, cantidad):
        # Vende una cantidad específica de un producto
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad >= cantidad:
                    producto.actualizar_cantidad(-cantidad)
                    print(f"Vendido {cantidad} de {producto.nombre}.")
                else:
                    print(f"No hay suficiente {producto.nombre} en inventario.")
                return
        print(f"Producto {nombre_producto} no encontrado.")

    def mostrar_inventario(self):
        # Muestra el inventario completo de la tienda
        print(f"Inventario de la tienda {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_informacion()


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda("Mi Tienda")

    p1 = Producto("Manzanas", 0.50, 100)
    p2 = Producto("Naranjas", 0.75, 80)

    tienda.agregar_producto(p1)
    tienda.agregar_producto(p2)

    tienda.mostrar_inventario()

    tienda.vender_producto("Manzanas", 20)
    tienda.vender_producto("Naranjas", 90)

    tienda.mostrar_inventario()
