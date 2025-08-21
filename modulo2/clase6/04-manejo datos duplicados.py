import pandas as pd

data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Juan Pablo', "Jorge", "Jorge", "Jorge"],
    'Edad': [25, 30, 29, 25, 40, 40, 40],
    'Ciudad': ['Bs As', 'Cordoba', 'Mendoza', 'Bs As', 'La Plata', 'La Plata', 'La Plata']
}

dataframe = pd.DataFrame(data)

# Usando el metodo duplicated
print(dataframe.duplicated())

dataframe_sin_duplicados = dataframe.drop_duplicates()

print(dataframe_sin_duplicados)

dataframe_sin_duplicados.to_csv("dataframe-v1.csv", index=False)