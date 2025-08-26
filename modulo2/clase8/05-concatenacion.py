import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2],
    'Nombre': ['Ana', 'Juan']
})

df2 = pd.DataFrame({
    'ID': [3, 4],
    'Nombre': ['Pedro', 'Lucía']
})

dataframe_concatenado = pd.concat([df1, df2], axis=0, ignore_index=True)

# QUE ES AXIS?
# Define en que direccion se concatena
# axis= 0 -> concatena por filas (Uno debajo del otro)
# axis = 1 -> concatena por columnas

""" 
Por defecto, pandas mantiene los índices originales de cada dataframe al concatenar.

Si lo pones en True, pandas resetea los índices y asigna uno nuevo consecutivo desde 0.
"""


print(dataframe_concatenado)

# Ejemplo con axis 1
dataframe_salarios = pd.DataFrame({
    "Salarios": [200, 1000, 420, 125]
})

# concateno con el nuevo dataframe
dataframe_concatenado_v2 = pd.concat([dataframe_concatenado, dataframe_salarios], axis=1, ignore_index=False)

print(dataframe_concatenado_v2)

print("-------------")

dataframe_raro = pd.concat([df1, dataframe_salarios], axis=1, ignore_index=False)
print(dataframe_raro)