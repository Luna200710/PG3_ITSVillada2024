class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer número entero: "))
        self.num2 = int(input("Ingrese el segundo número entero: "))
        self.realizar_operaciones()

    def realizar_operaciones(self):
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        resultado = self.num1 + self.num2
        print("Suma:", resultado)

    def resta(self):
        resultado = self.num1 - self.num2
        print("Resta:", resultado)

    def multiplicacion(self):
        resultado = self.num1 * self.num2
        print("Multiplicación:", resultado)

    def division(self):
        if self.num2 != 0:
            resultado = self.num1 / self.num2
            print("División:", resultado)
        else:
            print("No se puede dividir por cero.")


operaciones = Operaciones()