import dataframe
import utilidades
import pandas as pd
import seaborn as sns

def interaccionUsuario():
    opcion = input("\nElija el metodo para visualizar la informacion del conjunto de datos: \n1)Cantidad de valores. \n2)Cantidad de valores unicos por columna. \n3)Mapa de calor de valores nulos. \n4)Grafico de barras. \n5)Histograma. \n6)Regresar al menu anterior. \n")

    if opcion == "1":
        interaccionUsuarioCantidad()
    elif opcion == "2":
        interaccionUsuarioValoresUnicos()
    elif opcion == "3":
        mapaCalor()
    elif opcion == "4":
        graficoBarras()
    elif opcion == "5":
        histograma()
    elif opcion == "6":
        return "Atras"
    else:
        print("\nElija una opcion correcta.")
        interaccionUsuario()

    return "Atras"

def interaccionUsuarioCantidad():
    opcion = input("\nElija el tipo de valores que desea visualizar: \n1)Nulos. \n2)No nulos. \n3)Regresar al menu anterior. \n")

    if opcion == "1":
        interaccionUsuarioCantidadNulos()
    elif opcion == "2":
        interaccionUsuarioCantidadNoNulos()
    elif opcion == "3":
        return interaccionUsuario()
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

def interaccionUsuarioValoresUnicos():
    opcion = input("\nElija si desea incluir valores nulos en la busqueda: \n1)Incluir valores nulos. \n2)No incluir valores nulos. \n3)Regresar al menu anterior. \n")

    if opcion == "1":
        print(f"\nValores unicos por columna: \n{valoresUnicosColumna(True)}")
        interaccionUsuarioValoresUnicos()
    elif opcion == "2":
        print(f"\nValores unicos por columna: \n{valoresUnicosColumna(False)}")
        interaccionUsuarioValoresUnicos()
    elif opcion == "3":
        interaccionUsuario()
    else:
        print("\nElija una opcion correcta.")
        interaccionUsuarioValoresUnicos()

    return

def valoresUnicosColumna(nulos):
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuario()
        return

    if nulos:
        return dataframe.df[columna].value_counts(dropna=False)
    else:
        return dataframe.df[columna].value_counts()
    
def mapaCalor():
    sns.heatmap(dataframe.df.isnull(), cbar=False)
    return

def graficoBarras():
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuario()
        return
    
    dataframe.df[columna].value_counts().sort_index(ascending=True).plot(kind = 'bar')
    return

def histograma():
    columna = utilidades.hallarColumna()
    if columna is None:
        interaccionUsuario()
        return
    
    dataframe.df[columna].hist(bins=10)
    return
    