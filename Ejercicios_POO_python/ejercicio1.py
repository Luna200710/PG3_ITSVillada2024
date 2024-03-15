class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrarnombre(self):
        print("Nombre:", self.nombre)

persona1 = Persona("Juan")
persona2 = Persona("María")

persona1.mostrarnombre()
persona2.mostrarnombre()