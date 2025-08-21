import pandas as pd

data = {
    'Nombre': [' Juan ', 'ANA', 'Pedro', 'ANA', None],
    'Edad': [25, None, 35, 25, 40],
    'Ciudad': ['Bs As', 'CÓRDOBA', 'Mendoza', 'Bs As', 'La Plata']
}

""" 
Detectar nulos y reemplazarlos con la media de la columna.

Eliminar duplicados.

Reemplazar “Bs As” por “Buenos Aires”.

Normalizar nombres (lower() + strip()).

Convertir la columna Edad a int.

Renombrar todas las columnas.
"""

# PAsamos el diccionario a dataframe
dataframe = pd.DataFrame(data)

# Reemplazando nombre nulo por Anonimo
dataframe['Nombre'].fillna("Anonimo", inplace=True)

print("Dataframe sin nombres nulos")
print(dataframe)
print("----------------------------------")
# Reemplazar edad nula con promedio de la columna
dataframe['Edad'].fillna(dataframe['Edad'].mean(), inplace=True)

print("Dataframe sin edad nula")
print(dataframe)
print("-----------------------------")

# Detectar duplicados
print(dataframe.duplicated())

print("-----------------------------------")

# Como no hay duplicados no hacemos nada

# Reemplazamos "Bs As" por "Buenos Aires"
dataframe['Ciudad'] = dataframe['Ciudad'].replace('Bs As', 'Buenos Aires')

print("Cambiamos Bs As por Buenos Aires")
print(dataframe)
print("--------------------")


# Normalizamos nombres
dataframe['Nombre'] = dataframe['Nombre'].str.lower().str.strip()

print("Nombres normalizados")
print(dataframe)
print("---------------------")

# Normalizar ciudades
dataframe['Ciudad'] = dataframe['Ciudad'].str.lower().str.strip()

print("Normalizamos ciudades")
print(dataframe)
print("--------------------------------")

# Convertir la columna edad a int
dataframe['Edad'] = dataframe['Edad'].astype(int)

print("Pasamos las edades a entero")
print(dataframe)
print("----------------------")

# renombrar todas las columnas
dataframe.rename(columns={
    'Nombre': 'nombre',
    'Edad': 'edad',
    'Ciudad': 'ciudad'
}, inplace=True)

print("Normalizamos las columnas")
print(dataframe)

# Guardamos el dataframe

dataframe.to_csv('ejercicio-final.csv')

dataframe = dataframe[sorted(dataframe.columns)]

print(dataframe)