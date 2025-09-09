import pandas as pd

dataframe = pd.read_csv("titanic.csv")

print(dataframe.head())

# exploracion inicial:

print(dataframe.info())
print(dataframe.describe())
print(dataframe.columns)

print(dataframe.isnull().sum())

# Limpieza inicial

dataframe = dataframe.drop(columns=['Cabin', 'Ticket', 'Name'])


print(dataframe.columns)

# Rellenar valores faltantes
dataframe['Age'] = dataframe['Age'].fillna(dataframe['Age'].mean())
dataframe['Embarked'] = dataframe['Embarked'].fillna('Unknown')

print(dataframe.isnull().sum())

# Analisis estadistico

# Tasa de supervivencia
print(dataframe['Survived'].value_counts(normalize=True))
# El parámetro normalize=True en value_counts() hace que pandas te devuelva las frecuencias relativas (porcentajes) en lugar de los conteos.
print(dataframe['Survived'].value_counts())


# Edad promedio

print(dataframe['Age'].mean())

# Edad promedio de fallecidos:
print(dataframe[dataframe['Survived'] == 0]['Age'].mean())

# Valor con coma
print(str(dataframe['Age'].mean()).replace('.',','))

# redondeando
print(round(dataframe['Age'].mean(), 3))


# -------------

# Supervivencia por sexo
print(dataframe.groupby('Sex')['Survived'].mean())


# Supervivencia por clase social
print(dataframe.groupby('Pclass')['Survived'].mean())

dataframe.to_csv("Titanic-Corregido.csv")