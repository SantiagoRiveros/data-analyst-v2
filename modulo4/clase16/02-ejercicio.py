import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Traer el dataset de titanic
dataframe = sns.load_dataset("titanic")

print(dataframe)

# Ejercicio 1: Conteo de pasajeros por clase

sns.countplot(x="pclass", data=dataframe)
plt.title("Conteo de pasajeros por clase")
plt.savefig("img 1 - Conteo de pasajeros por clase")
# plt.show()

# Mostrar todos los dataset precargados
# print(sns.get_dataset_names())

# LIMPIAR EL GRAFICO
plt.figure()

# Ejercicio 2: Supervivencia por sexo
sns.barplot(x="sex", y="survived", data=dataframe)
plt.title("Tasa de supervivencia por sexo")
plt.ylabel("Proporción que sobrevivió")
plt.savefig("img 2 - Supervivencia por sexo")

# Ejercicio 3: Edad por clase (boxplot)

plt.figure()
sns.boxplot(x="pclass", y="age", data=dataframe)
plt.title("Distribucion de edad por clase")
plt.savefig("img 3 - Distribucion de edad por clase")

# Ejercicio 4: Relacion entre edad y tarifa
plt.figure()
sns.scatterplot(x="age", y="fare", hue="sex", data=dataframe)
plt.title("Relacion entre edad y tarifa")
plt.savefig("img 4 - Rleacion entre edad y tarifa")

# Ejercicio 5 - Mapa de correlaciones de calor
plt.figure()
corr = dataframe.select_dtypes(include=["number"]).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Mapa de correlaciones")
plt.savefig("img 5 - Mapa de correlaciones")

# Ejercicio 6 - Pairplot para varias variables
plt.figure()
sns.pairplot(dataframe[["age", "fare", "survived", "pclass"]], hue="survived")
plt.title("Pairplot para varias variables")
plt.savefig("img 6 - Pairplot para varias variables")

# Ejercicio 7 - Violinplot por sexo
plt.figure()
sns.violinplot(x="sex", y="age", data=dataframe)
plt.title("Violinplot por sexo")
plt.savefig("img 7 - Violinplot por sexo")

# Ejercicio 8 - Histograma de edad
plt.figure()
sns.histplot(dataframe['age'].dropna(), bins=20, kde=True)
plt.title("Histograma por edad")
plt.savefig("img 8 - Histograma por edad")