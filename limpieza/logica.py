import dataframe
import filtrado
import pandas as pd
import numpy as np

def ensuciarDf():
    for i in range(10):
        dataframe.df.iloc[[np.random.randint(0,50)],[1]] = np.nan
        dataframe.df.iloc[[np.random.randint(0,50)],[3]] = np.nan
        dataframe.df.iloc[[np.random.randint(0,50)],[4]] = np.nan
        dataframe.df.iloc[[np.random.randint(0,50)],[5]] = np.nan
        dataframe.df.iloc[[np.random.randint(0,50)],[6]] = np.nan
        dataframe.df.iloc[[np.random.randint(0,50)],[7]] = np.nan
        dataframe.df.iloc[[np.random.randint(0,50)],[8]] = np.nan
        dataframe.df.iloc[[np.random.randint(0,50)],[9]] = np.nan
        dataframe.df.iloc[[np.random.randint(0,50)],[10]] = np.nan
    return

def limpiarCeldasVaciasTodo():
    dataframe.df.dropna(inplace=True)

def valorPersonalizado(columna, valor):
    if columna is None:
        dataframe.df.fillna(valor, inplace=True)
    else:
        filtrado.valorPersonalizado(columna, valor)

    return

def valorSiguiente():
    dataframe.df.fillna(method="bfill", inplace=True)
    return

def valorAnterior():
    dataframe.df.fillna(method="ffill", inplace=True)
    return

def removerFila(fila):
    dataframe.df.drop(fila, inplace=True)
    return

def removerDuplicados():
    dataframe.df.drop_duplicates(inplace = True) 
    return