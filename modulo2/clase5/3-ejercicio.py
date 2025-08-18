import pandas as pd

diccionario = {
    "Nombre": ["Ana", "Juan", "Pedro", "Lucía", "Martín", "Carla"],
    "Edad": [25, 32, 45, 29, 41, 38],
    "Ciudad": ["Buenos Aires", "Córdoba", "Mendoza", "Rosario", "Tucumán", "Córdoba"],
    "Salario": [3500, 4200, 6000, 3800, 5200, 4800],
    "Puesto": ["Analista", "Desarrollador", "Gerente", "Analista", "Desarrollador", "Diseñadora"]
}

dataframe_empleados = pd.DataFrame(diccionario)

""" 
Paso 2 – Exploración básica (5 min)

Muestra las primeras 3 filas.

Muestra cuántas filas y columnas tiene.

Muestra un resumen estadístico (.describe()).

Paso 3 – Análisis estadístico (7 min)

Calcula el salario promedio.

Obtén la edad mínima y máxima.

¿Cuál es el salario más alto?

Paso 4 – Modificación de datos (8 min)

Agrega una columna "Años de Experiencia" con valores ficticios.

Aumenta todos los salarios un 7%.

Cambia el puesto de “Lucía” a "Jefa de Proyecto".

Paso 5 – Filtrado de datos (10 min)

Filtra los empleados que ganen más de $5000.

Muestra solo los empleados de Córdoba.

Filtra a los empleados cuyo puesto sea "Analista".

Paso 6 – Guardar resultados (5 min)

Guarda el DataFrame final en un archivo empleados_actualizado.csv.

Carga el CSV en un nuevo DataFrame y verifica que los datos sean los mismos.
"""

print("Dataframe creado")
print(dataframe_empleados)
print("--------------------------------------------")

# Paso 2 - Exploracion basica
print("Primeras 3 filas:")
print(dataframe_empleados.head(3))

print("--------------------------------------------")

print("Forma (filas, columnas)")
print(dataframe_empleados.shape)

print("--------------------------------------------")

print("Resumen estadistico:")
print(dataframe_empleados.describe())

print("--------------------------------------------")

# Paso 3 - Analisis Estadistico:
salario_promedio = dataframe_empleados["Salario"].mean()
edad_minima = dataframe_empleados["Edad"].min()
edad_maxima = dataframe_empleados["Edad"].max()
salario_maximo = dataframe_empleados["Salario"].max()

print("Salario promedio:")
print(salario_promedio)
print("Edad minima:")
print(edad_minima)
print("Edad maxima:")
print(edad_maxima)
print("Salario mas alto:")
print(salario_maximo)

print("--------------------------------------------")

# Paso 4 - Modificacion de datos:
# 1) Agregar columna Años de Experiencia (valores ficticios, misma longitud que el DF)
dataframe_empleados["Años de experiencia"] = [2, 6, 20, 5, 15, 9]

# 2) Aumentar salarios un 7%
dataframe_empleados["Salario"] = dataframe_empleados["Salario"] * 1.07

# 3) Cambiar el puesto de Lucia a "Jefa de proyecto"
dataframe_empleados.loc[dataframe_empleados["Nombre"] == "Lucía", "Puesto"] = "Jefa de proyecto"

print(dataframe_empleados)

print("--------------------------------------------")

# Paso 5 - Filtrado de datos
# 1) Empleados con salario > 5000
salario_mayor_5000 = dataframe_empleados[dataframe_empleados["Salario"] > 5000]

# 2) Empleados de Córdoba
empleados_cordoba = dataframe_empleados[dataframe_empleados["Ciudad"] == "Córdoba"]

# 3) Empleados cuyo puesto sea 'Analista'
empleados_analistas = dataframe_empleados[dataframe_empleados["Puesto"] == "Analista"]

print("Empleados con salario mayor a 5000:")
print(salario_mayor_5000)

print("Empleados de Cordoba:")
print(empleados_cordoba)

print("Empleados con puesto de Analista:")
print(empleados_analistas)

# Paso 6 - Guardar los datos
dataframe_empleados.to_csv("nuevo_dataframe.csv", index=False)