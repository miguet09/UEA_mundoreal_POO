# src/main.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # Lista para almacenar eventos
        self.eventos = []

        # Configuración de la interfaz
        self.setup_ui()

    def setup_ui(self):
        # Marco para la visualización de eventos
        frame_visualizar = ttk.Frame(self.root, padding="10")
        frame_visualizar.pack(fill=tk.BOTH, expand=True)

        # Configuración del TreeView
        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_visualizar, columns=columnas, show="headings", selectmode="browse")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Marco para la entrada de datos
        frame_entrada = ttk.Frame(self.root, padding="10")
        frame_entrada.pack(fill=tk.X)

        # Etiqueta y DatePicker para la fecha
        lbl_fecha = ttk.Label(frame_entrada, text="Fecha:")
        lbl_fecha.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.fecha_entry = DateEntry(frame_entrada, width=12, background='darkblue',
                                     foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Etiqueta y Entry para la hora
        lbl_hora = ttk.Label(frame_entrada, text="Hora (HH:MM):")
        lbl_hora.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.hora_entry = ttk.Entry(frame_entrada, width=15)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        # Etiqueta y Entry para la descripción
        lbl_descripcion = ttk.Label(frame_entrada, text="Descripción:")
        lbl_descripcion.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.descripcion_entry = ttk.Entry(frame_entrada, width=50)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W)

        # Marco para los botones de acción
        frame_botones = ttk.Frame(self.root, padding="10")
        frame_botones.pack(fill=tk.X)

        # Botón para agregar evento
        btn_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para eliminar evento seleccionado
        btn_eliminar = ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para salir de la aplicación
        btn_salir = ttk.Button(frame_botones, text="Salir", command=self.root.quit)
        btn_salir.pack(side=tk.RIGHT, padx=5, pady=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validación de los campos
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        # Validar el formato de la hora
        try:
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Formato de hora incorrecto", "La hora debe tener el formato HH:MM.")
            return

        # Agregar el evento a la lista
        evento = (fecha, hora, descripcion)
        self.eventos.append(evento)

        # Insertar el evento en el TreeView
        self.tree.insert("", tk.END, values=evento)

        # Limpiar los campos de entrada
        self.fecha_entry.set_date(datetime.date.today())
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        # Obtener el ítem seleccionado
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Sin selección", "Por favor, selecciona un evento para eliminar.")
            return

        # Confirmar la eliminación
        confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
        if confirm:
            # Obtener los valores del ítem seleccionado
            item = self.tree.item(selected_item)
            valores = item['values']

            # Eliminar de la lista de eventos
            self.eventos = [evento for evento in self.eventos if evento != tuple(valores)]

            # Eliminar del TreeView
            self.tree.delete(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
