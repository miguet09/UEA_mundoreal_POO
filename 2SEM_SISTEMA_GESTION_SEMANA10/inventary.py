# inventory.py
from product import Producto
import os

class Inventario:
    def __init__(self):
        self.productos = []
        self.archivo = 'inventario.txt'
        # Intentar cargar productos al iniciar
        self.cargar_productos()

    def añadir_producto(self, producto):
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_productos()
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                self.productos.remove(producto)
                self.guardar_productos()
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_productos()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_productos(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f'{producto.get_id_producto()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n')
        except (IOError, PermissionError) as e:
            print(f"Error al guardar los productos: {e}")

    def cargar_productos(self):
        if not os.path.exists(self.archivo):
            # Crear el archivo si no existe
            open(self.archivo, 'w').close()

        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
        except (IOError, PermissionError) as e:
            print(f"Error al cargar los productos: {e}")
        except ValueError as e:
            print(f"Error en el formato de los datos: {e}")