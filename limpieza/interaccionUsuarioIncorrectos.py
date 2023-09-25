import dataframe
import limpieza.logica as logica
import filtrado
import utilidades

def interaccionUsuarioIncorrectos():
    opcion = input("\nElija el metodo para limpiar los datos incorrectos: \n1)Reemplazar valores incorrectos. \n2)Remover filas con valores incorrectos. \n3)Regresar al menu anterior. \n")
    if opcion == "1":
        return interaccionUsuarioIncorrectosReemplazar()
    elif opcion == "2":
        return interaccionUsuarioIncorrectosRemover()
    elif opcion == "3":
        return "Atras"
    else:
        print("Elija una opcion correcta.")
        return interaccionUsuarioIncorrectos()

def interaccionUsuarioIncorrectosReemplazar():
    opcion = input("\nElija en donde quiere reemplazar valores incorrectos: \n1)Todo el conjunto de datos. \n2)Fila especificada. \n3)Regresar al menu anterior. \n")
    if opcion == "1":
        interaccionUsuarioIncorrectosReemplazarTodo()
    elif opcion == "2":
        interaccionUsuarioIncorrectosReemplazarFila()
    elif opcion == "3":
        interaccionUsuarioIncorrectos()
    else:
        print("Elija una opcion correcta.")
        interaccionUsuarioIncorrectosReemplazar()

    return

def interaccionUsuarioIncorrectosReemplazarTodo():
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuarioIncorrectosReemplazar()
        return

    condicion = utilidades.obtenerCondicion()
    if condicion is None:
        interaccionUsuarioIncorrectosReemplazar()
        return

    valor = input("Escriba el valor de reemplazo. Procure que el valor a ser ingresado coincida con el tipo de dato de la columna: ")
    try:
        filtrado.reemplazarTodo(columna, condicion, valor)
    except:
        print("ERROR: Imposible realizar la operacion especificada con valores de tipo no numericos.")
        interaccionUsuarioIncorrectosReemplazarTodo()
        return
    
    print("\nOperacion completada.")
    interaccionUsuarioIncorrectosReemplazar()
    return

def interaccionUsuarioIncorrectosReemplazarFila():
    try:
        fila = int(input("\nEscriba el indice de la fila a reemplazar: "))
    except:
        print("\nERROR: La fila ingresada debe corresponder a un valor numerico.")
        interaccionUsuarioIncorrectosReemplazarFila()
        return
    
    if fila in dataframe.df.index:
        columna = utilidades.hallarColumna()
        if columna is None:
            interaccionUsuarioIncorrectosReemplazar()
            return

        valor = input("Escriba el valor de reemplazo. Procure que el valor a ser ingresado coincida con el tipo de dato de la columna: ")
        filtrado.reemplazarFila(fila, columna, valor)
        print("\nOperacion completada.")
        interaccionUsuarioIncorrectosReemplazarFila()
    else:
        print("Indice no encontrado.")
        interaccionUsuarioIncorrectosReemplazarFila()

    return

def interaccionUsuarioIncorrectosRemover():
    opcion = input("\nElija en donde quiere remover filas con valores incorrectos: \n1)Todo el conjunto de datos. \n2)Fila especificada. \n3)Regresar al menu anterior. \n")
    if opcion == "1":
        interaccionUsuarioIncorrectosRemoverTodo()
    elif opcion == "2":
        interaccionUsuarioIncorrectosRemoverFila()
    elif opcion == "3":
        interaccionUsuarioIncorrectos()
    else:
        print("Elija una opcion correcta.")
        interaccionUsuarioIncorrectosReemplazar()

    return
    
def interaccionUsuarioIncorrectosRemoverTodo():
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuarioIncorrectosRemover()
        return

    condicion = utilidades.obtenerCondicion()
    if condicion is None:
        interaccionUsuarioIncorrectosRemover()
        return

    valor = input("Escriba el valor no deseado. Procure que el valor a ser ingresado coincida con el tipo de dato de la columna: ")
    try:
        filtrado.removerTodo(columna, condicion, valor)
    except:
        print("ERROR: Imposible realizar la operacion especificada con valores de tipo no numericos.")
        interaccionUsuarioIncorrectosRemoverTodo()
        return
    
    print("\nOperacion completada.")
    interaccionUsuarioIncorrectosRemover()
    return

def interaccionUsuarioIncorrectosRemoverFila():
    try:
        fila = input("\nEscriba el indice de la fila a reemplazar: ")
    except:
        print("\nERROR: La fila ingresada debe corresponder a un valor numerico.")
        interaccionUsuarioIncorrectosRemoverFila()()
        return

    if fila in logica.df.index:
        logica.removerFila(fila)
        print("\nOperacion completada.")
        interaccionUsuarioIncorrectosRemover()
    else:
        print("Indice no encontrado.")
        interaccionUsuarioIncorrectosRemoverFila()
    return