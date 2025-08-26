import pandas as pd

# Esto es el dataframe 1 -> Empleados
df_empleados = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Lucía'],
    'Departamento': ['Ventas', 'IT', 'Marketing', 'IT']
})

# Dataframe 2 -> Salarios

df_salarios = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Salario': [3000, 4000, 3500, 4500]
})

# Merge Inner
# Se fusionan SOLO los empleados con un salario asociado
df_inner = pd.merge(df_empleados, df_salarios, on="ID", how="inner")
print("INNER JOIN")
print(df_inner)
print("----------------------")
 #Explicación: Sólo se incluirán los empleados cuyo ID esté presente en ambos DataFrames, es decir, ID 1, 2 y 3.


# Left Join
df_left = pd.merge(df_empleados, df_salarios, on="ID", how="left")
print("LEFT JOIN")
print(df_left)
print("----------------------")

# Right Join
df_right = pd.merge(df_empleados, df_salarios, on="ID", how="right")
print("RIGHT JOIN")
print(df_right)
print("----------------------")

# Outer Join
df_outer = pd.merge(df_empleados, df_salarios, on="ID", how="outer").drop_duplicates()
print("OUTER JOIN")
print(df_outer)