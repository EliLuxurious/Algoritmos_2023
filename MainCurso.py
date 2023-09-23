import pandas as pd
from openpyxl import Workbook
from curso_negocio import CursoNegocio
from Curso import Curso  # Importar la clase Curso desde curso.py

curso_negocio = CursoNegocio()

def registrar_cursos():
    codigo = input('Ingrese código del curso: ')
    nombre = input('Ingrese nombre del curso: ')
    curso_negocio.registrar_curso(codigo, nombre)
    curso_negocio.guardar_cursos()
    print(f'Registro correctamente el curso')

def obtener_cursos():
    listado_cursos = curso_negocio.obtener_cursos()
    for curso in listado_cursos:
        print(f'Código del curso: {curso.codigo}, Nombre del curso: {curso.nombre}')
        if curso.mostrar_docente():
            print(f'Docente asignado: {curso.mostrar_docente().nombre}')
        else:
            print('Docente no asignado')

def editar_curso():
    # Puedes implementar la edición de cursos si lo deseas
    pass

opciones = {
    "1": registrar_cursos,
    "2": obtener_cursos,
    "3": editar_curso,
    "4": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar cursos")
    print("2. Listar cursos")
    print("3. Editar curso")
    print("4. Salir")
    print("##########################")

    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
