import limpieza.logica as logica
import filtrado
import utilidades

def interaccionUsuarioVacios():
    opcion = input("\nElija el metodo para limpiar los valores vacios: \n1)Eliminar filas con celdas vacias. \n2)Reemplazar valores vacios. \n3)Regresar al menu anterior. \n")
    if opcion == "1":
        return interaccionUsuarioVaciosEliminar()
    elif opcion == "2":
        return interaccionUsuarioVaciosReemplazar()
    elif opcion == "3":
        return "Atras"
    else:
        print("Elija una opcion correcta.")
        return interaccionUsuarioVacios()

    return

def interaccionUsuarioVaciosEliminar():
    opcion = input("\nElija en donde quiere eliminar los valores vacios: \n1)Todo el conjunto de datos. \n2)Columna especificada. \n3)Regresar al menu anterior. \n")
    if opcion == "1":
        logica.limpiarCeldasVaciasTodo()
    elif opcion == "2":
        columna = utilidades.hallarColumna()
        if columna is None:
            interaccionUsuarioVaciosEliminar()

        filtrado.limpiarCeldasVaciasColumna(columna)
    elif opcion == "3":
        interaccionUsuarioVacios()
    else:
        print("Elija una opcion correcta.")
        interaccionUsuarioVaciosEliminar()
        return
    
    print("\nOperacion completada.")
    interaccionUsuarioVaciosEliminar()
    return

def interaccionUsuarioVaciosReemplazar():
    opcion = input("\nElija en donde quiere reemplazar los valores vacios: \n1)Todo el conjunto de datos. \n2)Columna especificada. \n3)Regresar al menu anterior. \n")
    if opcion == "1":
        interaccionUsuarioVaciosReemplazarTodo()
    elif opcion == "2":
        interaccionUsuarioVaciosReemplazarColumna()
    elif opcion == "3":
        interaccionUsuarioVacios()
    else:
        print("Elija una opcion correcta.")
        interaccionUsuarioVaciosReemplazar()

    return

def interaccionUsuarioVaciosReemplazarTodo():
    opcion = input("\nElija con que valor desea reemplazar los valores vacios: \n1)Valor personalizado. \n2)Valor siguiente mas cercano no nulo. \n3)Valor anterior no cercano mas nulo. \n4)Regresar al menu anterior. \n")
    if opcion == "1":
        valor = input("\nEscriba el valor de reemplazo: ")
        logica.valorPersonalizado(None, valor)
    elif opcion == "2":
        logica.valorSiguiente()
    elif opcion == "3":
        logica.valorAnterior()
    elif opcion == "4":
        interaccionUsuarioVaciosReemplazar()
    else:
        print("Elija una opcion correcta.")
        interaccionUsuarioVaciosReemplazarTodo()
        return
    
    print("\nOperacion completada.")
    interaccionUsuarioVaciosReemplazarTodo()
    return

def interaccionUsuarioVaciosReemplazarColumna():
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuarioVaciosReemplazar()

    opcion = input("\nElija con que valor desea reemplazar los valores vacios: \n1)Valor personalizado. \n2)Media. \n3)Mediana. \n4)Moda. \n5)Regresar al menu anterior. \n")
    if opcion == "1":
        valor = input("\nEscriba el valor de reemplazo. Procure que el valor a ingresar sea del mismo tipo de dato de la columna: ")
        logica.valorPersonalizado(columna, valor)
    elif opcion == "2":
        try:
            filtrado.obtenerMedia(columna)
        except:
            print("\nERROR: El formato de la columna no es numerico. Imposible ejecutar la operacion.")
            interaccionUsuarioVaciosReemplazarColumna(columna)
            return
    elif opcion == "3":
        try:
            filtrado.obtenerMediana(columna)
        except:
            print("\nERROR: El formato de la columna no es numerico. Imposible ejecutar la operacion.")
            interaccionUsuarioVaciosReemplazarColumna(columna)
            return
    elif opcion == "4":
        try:
            filtrado.obtenerModa(columna)
        except:
            print("\nERROR: El formato de la columna no es numerico. Imposible ejecutar la operacion.")
            interaccionUsuarioVaciosReemplazarColumna(columna)
            return
    elif opcion == "5":
        interaccionUsuarioVaciosReemplazar()
    else:
        print("Elija una opcion correcta.")
        interaccionUsuarioVaciosReemplazarColumna(columna)
        return
    
    print("\nOperacion completada.")
    interaccionUsuarioVaciosReemplazarColumna()
    return