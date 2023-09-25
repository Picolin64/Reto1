import imprimir
import informacion
import limpieza.interaccionUsuario


def interaccionUsuario():
    opcion = input("\nElija la accion a realizar con el conjunto de datos: \n1)Imprimir el conjunto de datos. \n2)Graficar el conjunto de datos. \n3)Limpiar el conjunto de datos. \n4)Cargar un nuevo conjunto de datos. \n")
    if opcion == "1":
        respuesta = imprimir.interaccionUsuario()
    elif opcion == "2":
        respuesta = informacion.interaccionUsuario()
    elif opcion == "3":
        respuesta = limpieza.interaccionUsuario.interaccionUsuario()
    elif opcion == "4":
        return "Atras"
    else:
        print("Elija una opcion correcta.")
        return interaccionUsuario()

    if respuesta == "Atras":
        return interaccionUsuario()

    return