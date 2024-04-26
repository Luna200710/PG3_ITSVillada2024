while True:
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        suma = num1 + num2
        print("La suma de los números es:", suma)
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")
    else:
        continuar = input("¿Quiere seguir sumando valores? (s/n): ")
        if continuar.lower() != 's':
            break