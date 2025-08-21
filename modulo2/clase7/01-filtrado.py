import pandas as pd

dataframe = pd.DataFrame({
    'nombre': ['Ana', 'Juan', 'Luis', 'Ana'],
    'edad': [23, 45, 31, 28],
    'salario': [4000, 6500, 5200, 4100]
})

# Filtrar personas mayores a 30 años


print("Personas mayores a 30 años")
# print(dataframe.loc[dataframe['edad'] > 30])
print(dataframe[dataframe['edad'] > 30])
print("----------------------")

# Filtrar con multiples condiciones


print("Personas mayores a 30 años con sueldo superior a 6000")

print(dataframe[(dataframe['edad'] > 30) & (dataframe['salario'] > 6000)])
print("--------------------------------")

# usando loc

print("Usando .loc para filtrar las Anas")
print(dataframe.loc[dataframe['nombre'] == 'Ana'])

print("---------------------")

# Solo nombre y salario de mayores de 30
print(dataframe.loc[dataframe['edad'] > 30, ['nombre', 'salario']])
print("-----------------------")


# usando Query
print(dataframe.query("edad > 30 and salario > 6000"))
