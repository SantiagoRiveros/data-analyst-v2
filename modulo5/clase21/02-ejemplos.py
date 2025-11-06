# Histograma
# Muestra como se distribuyen los valores de una variable numerica.

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("titanic.csv")

sns.histplot(data=dataframe, x="Age", bins=100, kde=True)
plt.savefig("histograma.jpg")

# Boxplot
# Muestra la mediana, Cuartiles, y los outliers

""" 
Los cuartiles, son una forma de dividir un conjunto de datos ordenados en cuatro partes iguales,
cada una (o casi) con la misma cantidad de datos
Sirven para describir la distribucion de datos y detectar tendencias o valores atipicos.

Cuando ordenas los datos de mayor a menor:

Cuartil -> Que indica -> Percentil equivalente -> Significado
Q1 -> Valor por debajo al 25% de los datos -> P25 -> El 25% de los valores son menos o iguales que Q1
Q2 (Mediana) -> Valor por debajo al 50% de los datos -> P50 -> Divide los datos a la mitad
Q3 -> Valor por debajo al 75% de los datos -> P75 -> El 75% de los valores son menores o iguales a Q3

Ej:

lista de edades
[10, 12, 13, 15, 18, 20, 22, 24, 27, 30]

Q1 (25%) -> Entre 12 y 13 -> 13.5 (mas o menos)
Q2 (mediana) -> entre 18 y 20 -> 19
Q3 (75%) -> Entre 24 y 27 -> 23.5

Esto significa que:
- El 25% tiene menos de 12.5 años
- el 50% menos de 19
- el 75% menos de 25.5

Como calcularlo:
import pandas as pd

edades = pd.Series([10, 12, 13, 15, 18, 20, 22, 24, 27, 30])
edades.quantile([0.25, 0.5, 0.75])

Rango Intercuartilico (IQR)

IQR = Q3 - Q1

Sirve para medir la dispersion de datos y detectas outliers:
Un valor es atipico si esta por debajo de Q1 - 1.5 * IQR
O por encima de Q3 + 1.5 * IQR


"""

plt.clf()
import pandas as pd

edades = pd.Series([10, 12, 13, 15, 18, 20, 22, 24, 27, 30])
print(edades.quantile([0.25, 0.5, 0.75]))

# Boxplot

sns.boxplot(data=dataframe, x="Pclass", y="Age")
plt.savefig("boxplot.jpg")


# Scatter Plot
# Edad VS Tarifa
plt.clf()

sns.scatterplot(data=dataframe, x="Age", y="Fare")
plt.savefig("scatterplot.jpg")

# Heatmap de correlacion
corr = dataframe.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.savefig("heatmap.jpg")