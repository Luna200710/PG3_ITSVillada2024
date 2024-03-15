def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    cantidad_vocales = 0
    for letra in frase:
        if letra in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

frase = input("Ingrese una frase: ")
print("Cantidad de vocales:", contar_vocales(frase))

