import dataframe
import filtrado
import utilidades

def interaccionUsuario():
    opcion = input("\nElija como desea imprimir el conjunto de datos: \n1)Sin filtros. \n2)Con filtros. \n3)Regresar al menu anterior. \n")
    if opcion == "1":
        print(dataframe.df)
        return interaccionUsuario()
    elif opcion == "2":
        return imprimirConFiltros()
    elif opcion == "3":
        return "Atras"
    else:
        print("Elija una opcion correcta.")
        return interaccionUsuario()

    return

def imprimirConFiltros():
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuario()
        return

    condicion = utilidades.obtenerCondicion()
    if condicion is None:
        interaccionUsuario()
        return

    valor = input("Escriba el valor para filtrar. Procure que el valor a ser ingresado coincida con el tipo de dato de la columna: ")

    try:
        if condicion is None:
            interaccionUsuario()
        else:
            filtrado.imprimirDataframeFiltro(condicion, columna, valor)
    except:
        print("ERROR: Imposible realizar la operacion especificada con valores de tipo no numericos.")
        imprimirConFiltros()
        return

    interaccionUsuario()
    return