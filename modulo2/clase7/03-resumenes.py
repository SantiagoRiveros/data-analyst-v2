import pandas as pd

dataframe = pd.DataFrame({
    'nombre': ['Ana', 'Juan', 'Luis', 'Ana'],
    'edad': [23, 45, 31, 28],
    'salario': [4000, 6500, 5200, 4100]
})

# Resumen estadistico
print(dataframe.describe())

# Resumen personalizado.
print(dataframe.agg({
    'edad': ['min', 'max', 'mean'],
    'salario': ['sum', 'mean']
}))

# frecuencia de nombres
print(dataframe['nombre'].value_counts())