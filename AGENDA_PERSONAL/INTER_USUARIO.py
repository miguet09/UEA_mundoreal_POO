import tkinter as tk
from tkinter import messagebox

# Función para agregar una nueva tarea
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

# Función para marcar una tarea como completada
def completar_tarea():
    try:
        indice_tarea = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice_tarea)
        lista_tareas.delete(indice_tarea)
        lista_tareas.insert(tk.END, tarea + " (Completada)")
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        indice_tarea = lista_tareas.curselection()[0]
        lista_tareas.delete(indice_tarea)
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Entrada para las tareas
entrada_tarea = tk.Entry(ventana, width=35)
entrada_tarea.pack(pady=10)

# Botón para agregar tarea
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.pack(pady=10)

# Botón para completar tarea
boton_completar = tk.Button(ventana, text="Completar Tarea", command=completar_tarea)
boton_completar.pack(pady=5)

# Botón para eliminar tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Ejecutar el bucle de la ventana
ventana.mainloop()
