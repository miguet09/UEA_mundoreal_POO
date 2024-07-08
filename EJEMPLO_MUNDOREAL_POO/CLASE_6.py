# Definición de la clase base
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación del nombre

    def get_nombre(self):
        return self.__nombre

    def hacer_sonido(self):
        pass  # Método que será sobrescrito en las clases derivadas


# Clase derivada que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza  # Encapsulación de la raza

    def hacer_sonido(self):
        return "Guau!"  # Polimorfismo: sobrescritura del método hacer_sonido


# Clase derivada que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.__color = color  # Encapsulación del color

    def hacer_sonido(self):
        return "Miau!"  # Polimorfismo: sobrescritura del método hacer_sonido


# Función principal para probar el programa
def main():
    perro1 = Perro("Rex", "Labrador")
    gato1 = Gato("Pelusa", "Blanco")

    # Ejemplos de polimorfismo
    animales = [perro1, gato1]
    for animal in animales:
        print(f"{animal.get_nombre()} hace {animal.hacer_sonido()}")


if __name__ == "__main__":
    main()