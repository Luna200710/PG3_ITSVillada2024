
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

try:
    num_mes = int(input("Ingrese el número de mes (1-12): "))
    nombre_mes = meses[num_mes - 1]
    print("El mes correspondiente al número ingresado es:", nombre_mes)
except IndexError:
    print("Error: El número de mes ingresado está fuera de rango.")