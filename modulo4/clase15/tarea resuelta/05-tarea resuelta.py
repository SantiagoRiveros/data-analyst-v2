import pandas as pd

titanic = pd.read_csv("titanic.csv")

#1-¿Qué clase tenía más mujeres?

# Filtrar mujeres y contar por clase
mujeres_por_clase = titanic[titanic["Sex"] == "female"]["Pclass"].value_counts()

print(f"La clase con mas pasajeras mujeres es {mujeres_por_clase.idxmax()}")

#2- ¿Cuál es la distribución de tarifas para los pasajeros de 3ra clase?
import matplotlib.pyplot as plt

tarifas_3ra = titanic[titanic["Pclass"] == 3]["Fare"]

# Mostrar estadisticas basicas
print(tarifas_3ra.describe())


# Mostrar histograma
plt.hist(tarifas_3ra, bins=30, edgecolor="black")
plt.title("Distribucion de tarifas - 3ra Clase")
plt.xlabel("Tarifa")
plt.ylabel("Cantidad de pasajeros")
plt.savefig("Distribucion de tarifas - 3ra Clase")

#3- ¿Cuál es la edad promedio de los pasajeros que embarcaron en cada puerto?
#Agrupar por puerto de embarque y calcular edad promedio
edad_promedio_por_puerto = titanic.groupby("Embarked")["Age"].mean()

print(edad_promedio_por_puerto)

#4-Mostrá la cantidad de personas que sobrevivieron y no sobrevivieron por sexo.

supervivencia_por_sexo = titanic.groupby(["Sex", "Survived"]).size().unstack()
print(supervivencia_por_sexo)

# Grafico
supervivencia_por_sexo.plot(kind="bar", stacked=True)
plt.title("Supervivientes y no supervivientes por sexo")
plt.xlabel("Sexo")
plt.ylabel("Cantidad de personas")
plt.legend(["No Sobrevivio", "Sobrevivio"])
plt.savefig("Supervivientes y no supervivientes por sexo")

# Unstack convierte la segunda fila del indice en columnas

print(titanic.groupby(["Sex", "Survived"]).size())
print(titanic.groupby(["Sex", "Survived"]).size().unstack())