
try:
    with open("strings.txt", "w") as archivo:
        archivo.write("Hola\n")
        archivo.write("Mundo\n")
        archivo.write(123)  # Se intenta escribir un entero
except TypeError:
    print("Error: No se puede escribir un entero en el archivo de texto.")
