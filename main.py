def buscarLibro():
    buscado = input("ID del elemento a buscar: ")
    indexBuscado = arreglo.buscar(buscado)
    if indexBuscado is not None:
        print("Elemento encontrado en posicion: {0}".format(indexBuscado))
    else:
        print("Este ID no se encuentra en el registro.")
