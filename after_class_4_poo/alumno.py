from persona import Persona

class Alumno(Persona):

    def __init__(self, nombre, apellido, edad, dni, sexo, num_estudiante, comision):
        super().__init__(nombre, apellido, edad, dni, sexo)
        self.num_estudiante = num_estudiante
        self.comision = comision
        self.dni = dni

    def get_alumno(self, num_estudiante):
        with open('recursos/dataalumno.txt', 'r') as alumnos:
            for alumno in alumnos:
                detalles = alumno.split('|')
                if num_estudiante == detalles[0]:
                    persona = Persona()
                    data_alumno = persona.get_persona(detalles[1])
                    return detalles + data_alumno
                else:
                    return None

    def set_alumno(self):
        with open('recursos/dataalumno.txt', 'a') as alumno:
            alumno.write(f'{self.num_estudiante}|{self.dni}|{self.comision}|\n')
