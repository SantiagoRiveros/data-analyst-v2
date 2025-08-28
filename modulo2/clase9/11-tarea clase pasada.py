import pandas as pd

# Creamos dataframes
alumnos = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Maria'],
    'Edad': [20, 22, 21]
})

notas = pd.DataFrame({
    'ID': [1, 2, 3, 1],
    'Materia': ['Matematicas', 'Historia', 'Ingles', 'Historia'],
    'Nota': [9, 7, 8, 10]
})

# Inner merge
consolidado = pd.merge(alumnos, notas, on="ID", how="inner")
print(consolidado)

# EJEMPLO ELIMINANDO ID
# print(consolidado.drop("ID", axis=1))

# Creando dataframes adicionales
alumnos_nuevos1 = pd.DataFrame({
    'ID': [4, 5],
    'Nombre': ['Pedro', 'Lucía'],
    'Edad': [23, 20]
})

alumnos_nuevos2 = pd.DataFrame({
    'ID': [6, 7],
    'Nombre': ['Jorge', 'Sofía'],
    'Edad': [24, 22]
})

# Concatenar todos los alumnos
alumnos_total = pd.concat([alumnos, alumnos_nuevos1, alumnos_nuevos2], ignore_index=True)

#Guardamos los CSV
consolidado.to_csv("consolidado.csv", index=False)
alumnos_total.to_csv("alumnos_total.csv", index=False)
