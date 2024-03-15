def buscaradentro(lista, elemento):
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return "El elemento no se encuentra en la lista."
lista = [8, 12, 9, 45]
elemento_buscado = 12
resultado = buscaradentro(lista, elemento_buscado)
print("El elemento", elemento_buscado, "se encuentra en el índice", resultado)

