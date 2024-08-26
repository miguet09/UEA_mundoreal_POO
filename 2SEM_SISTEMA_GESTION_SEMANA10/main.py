# main.py
from inventory import Inventario
from product import Producto


def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                id_producto = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == '2':
                id_producto = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == '3':
                id_producto = input("ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (deje en blanco si no desea cambiar): ")
                precio = input("Nuevo precio (deje en blanco si no desea cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == '4':
                nombre = input("Nombre del producto a buscar: ")
                inventario.buscar_producto(nombre)

            elif opcion == '5':
                inventario.mostrar_productos()

            elif opcion == '6':
                print("Saliendo del sistema.")
                break

            else:
                print("Opción no válida, intente de nuevo.")

        except ValueError:
            print("Error: Entrada no válida. Asegúrese de ingresar datos en el formato correcto.")


if __name__ == "__main__":
    menu()