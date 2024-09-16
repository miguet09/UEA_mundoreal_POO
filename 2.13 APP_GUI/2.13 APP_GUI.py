import tkinter as tk
from tkinter import ttk


class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI Básica")

        # Crear el marco principal
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        # Etiqueta
        self.label = tk.Label(self.frame, text="Ingrese información:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        # Campo de texto
        self.entry = tk.Entry(self.frame, width=30)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        # Botón "Agregar"
        self.boton_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar_info)
        self.boton_agregar.grid(row=1, column=0, padx=5, pady=5)

        # Botón "Limpiar"
        self.boton_limpiar = tk.Button(self.frame, text="Limpiar", command=self.limpiar_info)
        self.boton_limpiar.grid(row=1, column=1, padx=5, pady=5)

        # Lista para mostrar datos
        self.lista = tk.Listbox(self.frame, width=50, height=10)
        self.lista.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def agregar_info(self):
        """ Agrega la información del campo de texto a la lista """
        info = self.entry.get()
        if info:
            self.lista.insert(tk.END, info)
            self.entry.delete(0, tk.END)

    def limpiar_info(self):
        """ Limpia el campo de texto y la lista """
        self.entry.delete(0, tk.END)
        self.lista.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()