import pandas as pd

dataframe = pd.read_csv("dataframe-v1.csv")

# El metodo replace
# replace('viejo', 'nuevo') → Reemplaza valores.

dataframe['Ciudad'] = dataframe['Ciudad'].replace('Bs As', 'Buenos Aires')

print(dataframe)

# Reemplazar Bs As por Buenos Aires

# Pasar todos los nombres a minusculas
dataframe['Nombre'] = dataframe['Nombre'].str.lower()

print(dataframe)

# podemos hacer lo mismo con las ciudades
dataframe['Ciudad'] = dataframe['Ciudad'].str.lower()

# Cambiamos los datos a tipo int

dataframe['Edad'] = dataframe['Edad'].astype(int)

print(dataframe)

dataframe.to_csv("dataframe-v2.csv", index=False)