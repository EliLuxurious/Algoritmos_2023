import pandas as pd
import tkinter as tk
from tkinter import ttk
from docente_negocio import DocenteNegocio

# Crear una instancia de la lógica de negocios para Docente
docente_negocio = DocenteNegocio()

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Docente")
root.geometry("400x400")

# Función para limpiar los campos de entrada
def limpiar_controles():
    codigo_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    ap_paterno_entry.delete(0, tk.END)
    ap_materno_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    facultad_entry.delete(0, tk.END)

# Función para registrar y guardar un nuevo docente
def guardar_docente():
    codigo = codigo_entry.get()
    nombre = nombre_entry.get()
    ap_paterno = ap_paterno_entry.get()
    ap_materno = ap_materno_entry.get()
    dni = dni_entry.get()
    facultad = facultad_entry.get()
    
    # Registrar el docente
    docente_negocio.registrar_docente(codigo, nombre, ap_paterno, ap_materno, dni, facultad)
    docente_negocio.guardar_docentes()
    
    # Limpiar los campos de entrada después de guardar
    limpiar_controles()

# Función para salir de la aplicación
def salir():
    root.quit()

# Etiquetas y campos de entrada para Docente
codigo_label = ttk.Label(root, text="Código del docente:")
codigo_label.pack()
codigo_entry = ttk.Entry(root)
codigo_entry.pack()

nombre_label = ttk.Label(root, text="Nombre del docente:")
nombre_label.pack()
nombre_entry = ttk.Entry(root)
nombre_entry.pack()

ap_paterno_label = ttk.Label(root, text="Apellido Paterno:")
ap_paterno_label.pack()
ap_paterno_entry = ttk.Entry(root)
ap_paterno_entry.pack()

ap_materno_label = ttk.Label(root, text="Apellido Materno:")
ap_materno_label.pack()
ap_materno_entry = ttk.Entry(root)
ap_materno_entry.pack()

dni_label = ttk.Label(root, text="DNI:")
dni_label.pack()
dni_entry = ttk.Entry(root)
dni_entry.pack()

facultad_label = ttk.Label(root, text="Facultad:")
facultad_label.pack()
facultad_entry = ttk.Entry(root)
facultad_entry.pack()

# Botón para guardar el docente
guardar_button = ttk.Button(root, text="Guardar Docente", command=guardar_docente)
guardar_button.pack()

# Botón para salir
salir_button = ttk.Button(root, text="Salir", command=salir)
salir_button.pack()

root.mainloop()