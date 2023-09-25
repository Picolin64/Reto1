import dataframe
import menu
import limpieza.logica as logica
import pandas as pd
from sodapy import Socrata

def main():
    print("Bienvenido al paquete de procesamiento de conjuntos de datos.")
    interaccionUsuario()
    return

def interaccionUsuario():
    opcion = input("Elija un metodo para cargar el conjunto de datos: \n1) Usar archivo csv local o URL. \n2) Cliente de socrata. \n3) Salir. \n")

    if opcion == "1":
        lecturaCsv()
    elif opcion == "2":
        clienteSocrata()
    elif opcion == "3":
        print("\nPrograma finalizado.")
    else:
        print("Elija una opcion correcta.")
        interaccionUsuario()

    return

def lecturaCsv():
    url = input("\nEscriba la ruta del archivo csv o una URL: ")
    try:
        dataframe.df = pd.read_csv(url)
    except:
        print("\nERROR: Escriba una ruta local o URL valida.")
        lecturaCsv()
        return
    
    logica.ensuciarDf()
    print("\nDataframe creado con exito.")
    if menu.interaccionUsuario() == "Atras":
        interaccionUsuario()

    return

def clienteSocrata():
    print("Ingrese los siguientes datos. Deje en blanco para omitir.")

    dominio = input("Dominio: ")
    token = input("Token: ")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if(not dominio.strip()):
        dominio = None
    if(not token.strip()):
        token = None
    if(not usuario.strip()):
        usuario = None
    if(not contraseña.strip()):
        contraseña = None

    try:
        cliente = Socrata(
            dominio,
            token,
            usuario,
            contraseña
        )
        print()
    except:
        print("Error: No se pudo crear el cliente. Verifique que los datos ingresados sean correctos.")
        clienteSocrata()
        return

    print("Cliente creado con exito.")
    conexionSocrata(cliente)
    return

def conexionSocrata(cliente):
    endpoint = input("Ingrese el URL endpoint: ")
    try:
        resultados = cliente.get(endpoint, limit=1000)
    except:
        print("\nError: No se pudo realizar la conexion. Verifique que los datos ingresados sean correctos.")
        conexionSocrata(cliente)
        return

    dataframe.df = pd.DataFrame.from_records(resultados)
    logica.ensuciarDf()
    print("\nDataframe creado con exito.")
    if menu.interaccionUsuario() == "Atras":
        interaccionUsuario()
        
    return

main()

"""
Registro_Nacional_de_Turismo_-_Vaup_s.csv
https://www.datos.gov.co/resource/mknp-pice.csv
www.datos.gov.co
mknp-pice
"""