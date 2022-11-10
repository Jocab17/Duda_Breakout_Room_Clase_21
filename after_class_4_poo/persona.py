class Persona:

    def __init__(self, dni, nombre, apellido, edad, sexo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def get_persona(self, dni):
        with open('.\\recursos\\datapersona.txt', 'r') as personas:
            for persona in personas:
                detalles = persona.split('|')
                if dni == detalles[0]:
                    return detalles
                else:
                    return 'No se encuentra la persona'

    def set_persona(self):
        with open('.\\recursos\\datapersona.txt', 'a') as persona:
            persona.write(f'{self.dni}|{self.nombre}|{self.apellido}|{self.edad}|{self.sexo}|\n')