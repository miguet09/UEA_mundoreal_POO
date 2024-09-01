class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

    # Métodos para obtener y establecer atributos
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio
import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def cargar_inventario(self, archivo='inventario.json'):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.productos = {id_producto: Producto(**info) for id_producto, info in datos.items()}
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. Asegúrese de que el formato sea correcto.")
            self.productos = {}

    def guardar_inventario(self, archivo='inventario.json'):
        try:
            with open(archivo, 'w') as f:
                datos = {id_producto: producto.__dict__ for id_producto, producto in self.productos.items()}
                json.dump(datos, f, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto {id_producto} eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print(f"Producto {id_producto} actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)
def menu():
    inventario = Inventario()
    inventario.cargar_inventario()

    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
            except ValueError:
                print("Cantidad o precio inválidos. Intente nuevamente.")
                continue
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            inventario.guardar_inventario()
        elif opcion == '2':
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            inventario.guardar_inventario()
        elif opcion == '3':
            id_producto = input("ID del Producto a actualizar: ")
            cantidad = input("Nueva Cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo Precio (dejar en blanco si no cambia): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
            except ValueError:
                print("Cantidad o precio inválidos. Intente nuevamente.")
                continue
            inventario.actualizar_producto(id_producto, cantidad, precio)
            inventario.guardar_inventario()
        elif opcion == '4':
            nombre = input("Nombre del Producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        elif opcion == '6':
            inventario.guardar_inventario()
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
