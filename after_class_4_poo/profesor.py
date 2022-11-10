from persona import Persona

class Profesor(Persona):

    def __init__(self, nombre, apellido, edad, dni, sexo, profesion, cuenta_bancaria, comision):
        super().__init__(nombre, apellido, edad, dni, sexo)
        self.profesion = profesion
        self.cuenta_bancaria = cuenta_bancaria
        self.comision = comision
        self.dni = dni

    def get_profesor(self, id):
        with open('recursos/dataprofesor.txt', 'r') as profesors:
            for profesor in profesors:
                detalles = profesor.split('|')
                if id == detalles[0]:
                    persona = Persona()
                    data_profesor = persona.get_persona(detalles[0])
                    return detalles + data_profesor
                else:
                    return None

    def set_profesor(self):
        with open('recursos/dataprofesor.txt', 'a') as profesor:
            profesor.write(f'{self.dni}|{self.profesion}|{self.cuenta_bancaria}|{self.comision}|\n')
