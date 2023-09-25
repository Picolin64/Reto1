"""
Información: Este paquete contendrá las funciones que permitan obtener la información pertinente para el preprocesamiento del dataset, tales como: 
cantidad de valores NaN o de cualquier otro valor (general y por columna), cantidad de valores NaN consecutivos por columna, mapa de calor de los valores NaN 
o de cualquier otro valor o rango,  mapas de calor que permitan identificar la distancia de los valores a la media de la columna, diagramas de cajas y bigotes 
por columna, cuartiles por columna, etc.
"""

"""
*Cantidad de valores
    *Nulos
        *General
        *Columna
    *No nulos
        *General
        *Columna
*Mapa de calor

"""
import dataframe
import utilidades
import pandas as pd

def interaccionUsuario():
    opcion = input("\nElija el metodo para visualizar la informacion del conjunto de datos: \n1)Cantidad de valores. \n2)Regresar al menu anterior. \n")

    if opcion == "1":
        return interaccionUsuarioCantidad()
    elif opcion == "2":
        return "Atras"
    else:
        print("\nElija una opcion correcta.")
        return interaccionUsuario()

    return

def interaccionUsuarioCantidad():
    opcion = input("\nElija el tipo de valores que desea visualizar: \n1)Nulos. \n2)No nulos. \n3)Regresar al menu anterior. \n")

    if opcion == "1":
        interaccionUsuarioCantidadNulos()
    elif opcion == "2":
        interaccionUsuarioCantidadNoNulos()
    elif opcion == "3":
        interaccionUsuario()
    else:
        print("\nElija una opcion correcta.")
        interaccionUsuarioCantidad()

    return

def interaccionUsuarioCantidadNulos():
    opcion = input("\nElija donde desea visualizar la cantidad de datos nulos: \n1)General. \n2)Columna. \n3)Regresar al menu anterior. \n")

    if opcion == "1":
        print(f"\nCantidad de valores nulos: \n{cantidadNulosGeneral()}")
        interaccionUsuarioCantidadNulos()
    elif opcion == "2":
        print(f"\nCantidad de valores nulos: \n{cantidadNulosColumna()}")
        interaccionUsuarioCantidadNulos()
    elif opcion == "3":
        interaccionUsuarioCantidad()
    else:
        print("\nElija una opcion correcta.")
        interaccionUsuarioCantidadNulos()

    return

def cantidadNulosGeneral():
    return dataframe.df.isna().sum()

def cantidadNulosColumna():
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuarioCantidadNulos()
        return
    
    return dataframe.df[columna].isna().sum()

def interaccionUsuarioCantidadNoNulos():
    opcion = input("\nElija donde desea visualizar la cantidad de datos no nulos: \n1)General. \n2)Columna. \n3)Regresar al menu anterior. \n")

    if opcion == "1":
        print(f"\nCantidad de valores no nulos: \n{cantidadNoNulosGeneral()}")
        interaccionUsuarioCantidadNoNulos()
    elif opcion == "2":
        print(f"\nCantidad de valores no nulos: \n{cantidadNoNulosColumna()}")
        interaccionUsuarioCantidadNoNulos()
    elif opcion == "3":
        interaccionUsuarioCantidad()
    else:
        print("\nElija una opcion correcta.")
        interaccionUsuarioCantidadNoNulos()

    return

def cantidadNoNulosGeneral():
     return dataframe.df.count()

def cantidadNoNulosColumna():
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuarioCantidadNulos()
        return
    
    return dataframe.df[columna].count()

