class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
    
    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))
    
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = 0
    
    def cargar_datos(self):
        super().cargar_datos()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))
    
    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado", self.nombre, "debe pagar impuestos.")
        else:
            print("El empleado", self.nombre, "no debe pagar impuestos.")


persona1 = Persona()
persona1.cargar_datos()
persona1.imprimir_datos()

empleado1 = Empleado()
empleado1.cargar_datos()
empleado1.imprimir_datos()
empleado1.pagar_impuestos()