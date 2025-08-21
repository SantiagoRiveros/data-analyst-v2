import pandas as pd

dataframe = pd.read_csv("dataframe-v2.csv")

# Reemplazamos los nombres de columnas
dataframe.rename(columns={
    'Nombre': 'nombre',
    'Edad': 'edad',
    'Ciudad': 'ciudad'
}, inplace=True)

print(dataframe)