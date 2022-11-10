from alumno import Alumno
from profesor import Profesor
from clase import Clase

class Comision(Alumno, Profesor, Clase):

    def __init__(self, num_comision, num_estudiante=None, dni=None):
        self.num_comision = num_comision
        self.num_estudiante = num_estudiante
        self.dni = dni

    def get_alumno_comision(self):
        with open('recursos/datacomision.txt', 'r') as comisiones:
            lista_alumnos = []
            for comision in comisiones:
                detalles = comision.split('|')
                if self.num_comision == detalles[0]:
                    lista_alumnos.append(detalles[1])
        return lista_alumnos

    def get_profesor_comision(self):
        with open('recursos/datacomision.txt', 'r') as comisiones:
            lista_profesor = []
            for comision in comisiones:
                detalles = comision.split('|')
                if self.num_comision == detalles[0]:
                    lista_profesor.append(detalles[2])
        return lista_profesor


    def set_comision(self):
        with open('recursos/datacomision.txt', 'a') as comision:
            comision.write(f'{self.num_comision}|{self.num_estudiante}|{self.dni}|\n')