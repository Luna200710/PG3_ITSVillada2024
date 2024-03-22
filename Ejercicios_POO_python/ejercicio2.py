class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def estaregular(self):
        if self.nota >= 6:
            print("El alumno", self.nombre, "está regular.")
        else:
            print("El alumno", self.nombre, "no está regular.")


alumno1 = Alumno("Juan", 8)
alumno2 = Alumno("María", 5)

alumno1.imprimir()
alumno1.estaregular()

alumno2.imprimir()
alumno2.estaregular()
