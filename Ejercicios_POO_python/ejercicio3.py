class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lados = [lado1, lado2, lado3]

    def imprimirladomayor(self):
        print("El lado mayor es:", max(self.lados))

    def esequilatero(self):
        if len(set(self.lados)) == 1:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")

triangulo = Triangulo(6, 5, 2)
triangulo.imprimirladomayor()
triangulo.esequilatero()