import pandas as pd

data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Juan', None],
    'Edad': [25, 30, None, 25, 40],
    'Ciudad': ['Bs As', 'Cordoba', 'Mendoza', 'Bs As', 'La Plata']
}

dataframe = pd.DataFrame(data)

print("PROBANDO EL DESCRIBE")
print(dataframe.describe())

# ver valores nulos
print(dataframe.isnull().sum())

# Borrar datos nulos
dataframe_sin_nulos = dataframe.dropna()

print(dataframe_sin_nulos)


# Reemplazamos la edad nula, con la edad promedio
dataframe['Edad'].fillna(dataframe['Edad'].mean(), inplace=True)

print("PROMEDIO DE EDAD")
print(dataframe['Edad'].mean())

print(dataframe)

# Reemplazamos el nombre por "Anonimo"
dataframe['Nombre'].fillna('Anonimo', inplace=True)

print(dataframe)

