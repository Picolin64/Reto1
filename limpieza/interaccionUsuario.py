import limpieza.interaccionUsuarioVacios as interaccionUsuarioVacios
import limpieza.interaccionUsuarioIncorrectos as interaccionUsuarioIncorrectos
import limpieza.interaccionUsuarioDuplicados as interaccionUsuarioDuplicados
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def interaccionUsuario():
    opcion = input("\nElija que datos quiere limpiar en el conjunto de datos: \n1)Valores vacios. \n2)Datos incorrectos. \n3)Datos duplicados. \n4)Regresar al menu anterior.")
    if opcion == "1":
        respuesta = interaccionUsuarioVacios.interaccionUsuarioVacios()
    elif opcion == "2":
        respuesta = interaccionUsuarioIncorrectos.interaccionUsuarioIncorrectos()
    elif opcion == "3":
        respuesta = interaccionUsuarioDuplicados.interaccionUsuarioDuplicados()
    elif opcion == "4":
        return "Atras"
    else:
        print("Elija una opcion correcta.")
        return interaccionUsuario()

    if respuesta == "Atras":
        return interaccionUsuario()

    return