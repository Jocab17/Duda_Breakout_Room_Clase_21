class Clase:

    def __init__(self, comision, nombre, tipo, horario, dias,):
        self.comision = comision
        self.nombre = nombre
        self.tipo = tipo
        self.horario = horario
        self.dias = dias

    def get_clase(self, comision):
        with open('recursos/dataclase.txt', 'r') as clases:
            for clase in clases:
                detalles = clase.split('|')
                if comision == detalles[0]:
                    return detalles
                else:
                    return None

    def set_clase(self):
        with open('recursos/dataclase.txt', 'a') as clase:
            clase.write(f'{self.comision}|{self.nombre}|{self.tipo}|{self.horario}|{self.dias}|\n')