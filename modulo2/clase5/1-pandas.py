# Dataframe
# Es una estructura tabular, conformada por filas y columnas, similar a una tabla de base de datos o una hoja de excel.

# Creando un dataframe a partir de un diccionario
import pandas as pd

# Datos como diccionario
datos = {
    "Nombre": ["Ana", "Juan", "Pablo", "Lucia", "Carlos", "Hernan", "Romina", "Jeronimo", "Ismael", "Leticia"],
    "Edad": [25, 18, 40, 31, 52, 21, 29, 40, 52, 19],
    "Ciudad": ["Berazategui", "Quilmes", "Avellaneda", "Florencio Varela", "Lanus", "Lomas de Zamora", "Ardigo", "La Plata", "Chascomus", "Mar del plata"],
    "Salario": [3000, 4000, 5000, 6000, 7000, 8000, 4000, 2000, 4000, 3400]
}

print(datos)
# Crear dataframe
dataframe = pd.DataFrame(datos)

print(dataframe)

# Explorar el dataframe

#Muestra las primeras 5 filas
print(dataframe.head())

# Mostrar las ultimas 5 filas
print(dataframe.tail())

# Mostrar la cantidad de filas y columnas:
print(dataframe.shape)

#Mostrar la informacion sobre el dataframe
print(dataframe.info())


# Acceder a filas y columnas

# Acceder a una columna
print(dataframe["Ciudad"])

# Acceder a una fila
print(dataframe.iloc[6])


# Describir Datos estadisticos

#Estadisticas generales de columnas numericas
print(dataframe.describe())

# ESTA PARTE QUE SIGUE, NO HACE FALTA QUE LA ENTIENDAN
""" 
            Edad      Salario
count  10.000000    10.000000 <- Count es la cantidad
mean   32.700000  4640.000000 <- Promedio
std    12.771931  1863.807334 <- Desviacion estandar
min    18.000000  2000.000000 <- Valor minimo
25%    22.000000  3550.000000 <- Primer Cuartil (Q1)
50%    30.000000  4000.000000 <- Segundo Cuartil (Q2) (o Mediana)
75%    40.000000  5750.000000 <- Tercer Cuartil (Q3)
max    52.000000  8000.000000 <- Valor Maximo

STD= Mide cuanto varian los datos respecto a la media (mean)
un STD alto -> Los valores estan muy dispersos
STD Bajo -> Los valores estan mas concentrados cerca de la media

Cuartiles:
Q1 -> El 25% de los datos son menores o iguales a este valor, y el 75% son mayores
Q2 (O mediana) -> El valor que está justo en el medio de la distribución: la mitad de los datos está por debajo y la otra mitad por encima.
Q3 -> El 75% de los datos son menores o iguales a este valor, y el 25% son mayores

Tomando la columna edad:
Q1 (25%) = 22 → 1 de cada 4 personas tiene 22 años o menos.

Mediana (50%) = 30 → la mitad tiene 30 años o menos.

Q3 (75%) = 40 → 3 de cada 4 personas tiene 40 años o menos.

"""

# Promedio de salarios
print(dataframe["Salario"].mean())

# Edad maxima
print(dataframe["Edad"].max())

print ("----------------------------------------")

#Modificar Datos

# Agregar una nueva columna:
dataframe["Experiencia"] = [2, 5, 1, 4, 8, 2, 5, 1, 4, 8 ]

print(dataframe)

# Supnogamos, que vamos a hacer un aumento del 10% a todos los empleados

dataframe["Salario"] = dataframe["Salario"] * 1.1

print(dataframe)

# Filtrar Datos:

#Filtrar personas mayores a 30
mayores_30 = dataframe[dataframe["Edad"] > 30]
print(mayores_30)

# Filtrar por ciudad
# Dejamos fuera al de varela
print("-----------------------------------------------------")
sin_varelenses = dataframe[dataframe["Ciudad"] != "Florencio Varela"]
print(sin_varelenses)


# Pero... ¿COMO GUARDO ESTO?

dataframe.to_csv("datos.csv", index=False)