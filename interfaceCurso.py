import pandas as pd
import tkinter as tk
from tkinter import ttk
from curso_negocio import CursoNegocio

# Crear una instancia de la lógica de negocios para Curso
curso_negocio = CursoNegocio()

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Curso")
root.geometry("400x400")

# Función para limpiar los campos de entrada
def limpiar_controles():
    codigo_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)

# Función para registrar y guardar un nuevo curso
def guardar_curso():
    codigo = codigo_entry.get()
    nombre = nombre_entry.get()
    
    # Registrar el curso
    curso_negocio.registrar_curso(codigo, nombre)
    curso_negocio.guardar_cursos()
    
    # Limpiar los campos de entrada después de guardar
    limpiar_controles()

# Función para salir de la aplicación
def salir():
    root.quit()

# Etiquetas y campos de entrada para Curso
codigo_label = ttk.Label(root, text="Código del curso:")
codigo_label.pack()
codigo_entry = ttk.Entry(root)
codigo_entry.pack()

nombre_label = ttk.Label(root, text="Nombre del curso:")
nombre_label.pack()
nombre_entry = ttk.Entry(root)
nombre_entry.pack()

# Botón para guardar el curso
guardar_button = ttk.Button(root, text="Guardar Curso", command=guardar_curso)
guardar_button.pack()

# Botón para salir
salir_button = ttk.Button(root, text="Salir", command=salir)
salir_button.pack()

root.mainloop()

