import pandas as pd
from Curso import Curso  # Importar la clase Curso desde Curso.py

class CursoNegocio():
    listado_cursos = []
    registros_cursos = 'C:/Users/Elia/Desktop/PROGRAMACION/Python/CICLO 3/Herencia/listado_alumno/listado_curso.xlsx'

    def __init__(self):
        self.listado_cursos = []

    def obtener_cursos(self):
        df = pd.read_excel(self.registros_cursos)
        listado_cursos = []
        for index, row in df.iterrows():
            curso = Curso(row['Codigo'], row['Nombre'])
            curso.notas = row['Notas']
            listado_cursos.append(curso)
        return listado_cursos

    def registrar_curso(self, codigo, nombre):
        self.listado_cursos = self.obtener_cursos()
        curso = Curso(codigo, nombre)
        self.listado_cursos.append(curso)
        print(f'Se agregó un curso: {len(self.listado_cursos)}')

    def guardar_cursos(self):
        if len(self.listado_cursos) > 0:
            data = []
            for curso in self.listado_cursos:
                data.append([curso.codigo, curso.nombre, curso.notas])
            columnas = ['Codigo', 'Nombre', 'Notas']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_cursos, index=False, engine='openpyxl')
            return f'Se registraron correctamente los datos del curso'
        else:
            return f'Se generó un error al registrar el curso'

