import pandas as pd

dataframe = pd.DataFrame({
    'nombre': ['Ana', 'Juan', 'Luis', 'Ana'],
    'edad': [23, 45, 31, 28],
    'salario': [4000, 6500, 5200, 4100]
})


# Agrupar por nombre y sacar promedio de salario
print(dataframe.groupby('nombre')['salario'].mean())

print("-------------------")
# Agrupar por nombre y contar cuantas veces aparece
print(dataframe.groupby('nombre').size())

print("---------------")

# Agrupar por nombre y aplicar múltiples funciones
print(dataframe.groupby('nombre')['salario'].agg(['mean', 'min', 'max']))

# llamar solo a las anas y hacer estas funciones agregadas
print(dataframe[dataframe['nombre'] == 'Ana'].agg({'salario':['mean','min','max']}))