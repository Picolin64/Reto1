import dataframe
import pandas as pd

def imprimirDataframeFiltro(condicion, columna, valor):
    if condicion == 1:
        print(dataframe.df[dataframe.df[columna] == valor])
    elif condicion == 2:
        print(dataframe.df[dataframe.df[columna] != valor])
    elif condicion == 3:
        print(dataframe.df[dataframe.df[columna] > valor])
    elif condicion == 4:
        print(dataframe.df[dataframe.df[columna] >= valor])
    elif condicion == 5:
        print(dataframe.df[dataframe.df[columna] < valor])
    elif condicion == 6:
        print(dataframe.df[dataframe.df[columna] <= valor])

def valorPersonalizado(columna, valor):
    dataframe.df[columna].fillna(valor, inplace=True)

def obtenerMedia(columna):
    media = dataframe.df[columna].mean()
    dataframe.df[columna].fillna(media, inplace=True)
    return

def obtenerMediana(columna):
    mediana = dataframe.df[columna].median()
    dataframe.df[columna].fillna(mediana, inplace=True)
    return

def obtenerModa(columna):
    moda = dataframe.df[columna].mode()[0]
    dataframe.df[columna].fillna(moda, inplace=True)
    return

def limpiarCeldasVaciasColumna(columna):
    dataframe.df[columna].dropna(inplace=True)
    return

def reemplazarTodo(columna, condicion ,valor):
    if condicion == 1:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] == valor:
                dataframe.df.loc[i, columna] = valor
    elif condicion == 2:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] != valor:
                dataframe.df.loc[i, columna] = valor
    elif condicion == 3:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] > valor:
                dataframe.df.loc[i, columna] = valor
    elif condicion == 4:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] >= valor:
                dataframe.df.loc[i, columna] = valor
    elif condicion == 5:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] < valor:
                dataframe.df.loc[i, columna] = valor
    elif condicion == 6:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] <= valor:
                dataframe.df.loc[i, columna] = valor
    
    return

def reemplazarFila(fila, columna, valor):
    dataframe.df.loc[fila, columna] = valor
    return

def removerTodo(columna, condicion, valor):
    if condicion == 1:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] == valor:
                dataframe.df.drop(i, inplace=True) 
    elif condicion == 2:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] != valor:
                dataframe.df.drop(i, inplace=True) 
    elif condicion == 3:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] > valor:
                dataframe.df.drop(i, inplace=True) 
    elif condicion == 4:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] >= valor:
                dataframe.df.drop(i, inplace=True) 
    elif condicion == 5:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] < valor:
                dataframe.df.drop(i, inplace=True) 
    elif condicion == 6:
        for i in dataframe.df.index:
            if dataframe.df.loc[i, columna] <= valor:
                dataframe.df.drop(i, inplace=True) 