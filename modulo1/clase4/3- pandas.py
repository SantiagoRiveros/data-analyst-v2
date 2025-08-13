# Pandas es una librería para manipular datos tabulares como si fueran hojas de cálculo.

import pandas as pd

datos = [10, 20, 30, 40, 50]
series = pd.Series(datos)
print(series)

# QUe es una serie? Basicamente, como una tabla pero unidimensional
# En Python, una serie (Series) es una estructura de datos unidimensional,

# Dataframes
# Es una tabla bidimensional, con filas y columna

dataframe = pd.DataFrame({
    "Nombre": ["Ana", "Pedro", "Jacinto", "Roman", "Felipe"],
    "Edad": [25, 18, 41, 29, 59],
    "Salario": [8000, 9000, 4000, 3000, 2000]
})
print(dataframe)


# QUiero acceder a los nombres
print(dataframe["Nombre"])

print("ACA SE DIVIDE -------------------")

# Como acceder a una fila
print(dataframe.iloc[2])

# acceder a filas especificas
print(dataframe.loc[[1, 3]])

#Obtener datos de una persona en especifico
print(dataframe[dataframe["Nombre"] == "Felipe"])

def encontrarPersona(nombre):
    fila = dataframe[dataframe["Nombre"] == nombre]
    return fila

nombrePersonaBuscar = input("Ingrese el nombre de la persona: ")
print(encontrarPersona(nombrePersonaBuscar))

# CUando no tenes identificador unico, y buscar a X persona con X cualidad
print(dataframe[(dataframe["Nombre"] == "Felipe") & (dataframe["Edad"] == 25)])

#Operador And &
# Operador OR |