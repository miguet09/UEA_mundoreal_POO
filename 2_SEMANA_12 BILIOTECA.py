class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn} en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in [u.id_usuario for u in self.usuarios]:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")

    def dar_baja_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if libro and usuario:
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} ya tiene prestado el libro '{libro.titulo}'.")
        else:
            print("El libro o el usuario no existe.")

    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if libro and usuario:
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print(f"El libro '{libro.titulo}' no está prestado a {usuario.nombre}.")
        else:
            print("El libro o el usuario no existe.")

    def buscar_libro(self, criterio, valor):
        encontrados = [libro for libro in self.libros.values() if getattr(libro, criterio, None) == valor]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio} igual a '{valor}'.")

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", "1234567890")
libro2 = Libro("1984", "George Orwell", "Distopía", "0987654321")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana García", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("1234567890", "001")
biblioteca.devolver_libro("1234567890", "001")

# Buscar y listar libros prestados
biblioteca.buscar_libro("categoria", "Fantasía")
biblioteca.listar_libros_prestados("001")