""" 
Crea dos DataFrames:

Ventas: con columnas ID, Producto, Cantidad

Precios: con columnas ID y Precio

Realiza un inner merge sobre ID para obtener un DataFrame combinado que incluya Producto, Cantidad y Precio.

"""

import pandas as pd

dataframe_ventas = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Producto': ['A', 'B', 'C', 'D'],
    'Cantidad': [10, 15, 20, 5]
})

dataframe_precios = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Precio': [100, 200, 150, 250]
})

dataframe_consolidado = pd.merge(dataframe_ventas, dataframe_precios, on="ID", how="inner")
dataframe_consolidado.to_csv("dataframe_consolidado.csv", index=False)
print(dataframe_consolidado)