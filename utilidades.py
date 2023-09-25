import dataframe
import limpieza.logica

def hallarColumna():
    columna = input("\nEscriba el nombre de la columna. Deje en blanco para regresar al anterior menu: ")
    if columna in dataframe.df.columns:
        return columna
    elif columna.strip() == "":
        return None
    else:
        print("Columna no encontrada.")
        hallarColumna()

    return

def obtenerCondicion():
    condicion = input("\nElija la condicion a cumplir para reemplazar o remover filas: \n1)Igual \n2)Diferente \n3)Mayor \n4)Mayor o igual \n5)Menor \n6)Menor o igual \n7)Regresar al menu anterior. \n") 
    if condicion == "1":
        return 1
    elif condicion == "2":
        return 2
    elif condicion == "3":
        return 3
    elif condicion == "4":
        return 4
    elif condicion == "5":
        return 5
    elif condicion == "6":
        return 6
    elif condicion == "7":
        return None
    else:
        print("Elija una opcion correcta.")
        obtenerCondicion()

    return