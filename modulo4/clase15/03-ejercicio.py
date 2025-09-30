# Ejercicio 1: Supervivencia por clase
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("titanic.csv")

sobrevivientes = dataframe[dataframe['Survived'] == 1]['Pclass'].value_counts().sort_index()
plt.bar(sobrevivientes.index, sobrevivientes.values)
plt.title('Supervivencia por clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
plt.savefig('titanic-ejercicio1')
plt.show()

""" 
df['Survived'] == 1 → Filtra solo las filas donde la columna Survived vale 1 (es decir, personas que sobrevivieron).

df[ ... ] → Se queda con esas filas filtradas.

['Pclass'] → Selecciona la columna de clase del pasajero (Pclass = 1, 2 o 3).

.value_counts() → Cuenta cuántos sobrevivientes hubo en cada clase.

.sort_index() → Ordena los resultados por el número de clase (1, 2, 3 en lugar de ordenados por frecuencia).
"""


# Ejercicio 2: Distribución de edad de los que sobrevivieron

plt.hist(dataframe[dataframe['Survived'] == 1]['Age'].dropna(), bins=20)
plt.title("Supervivencia por edad")
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.savefig('titanic-ejercicio2')
plt.show()

# Ejercicio 3: Supervivencia por sexo (gráfico de torta)

sexo = dataframe[dataframe['Survived'] == 1]['Sex'].value_counts()
plt.pie(sexo, labels=sexo.index, autopct='%1.1f%%')
plt.title('Supervivencia por sexo')
plt.savefig('titanic-ejercicio3')
plt.show()

# Ejercicio 4: Scatter entre tarifa y edad (color según supervivencia)

plt.scatter(dataframe['Age'], dataframe['Fare'], c=dataframe['Survived'], cmap='viridis')
plt.xlabel('Edad')
plt.ylabel('Tarifa')
plt.title('Edad vs Tarifa (color según supervivencia)')
plt.colorbar(label='0 = No sobrevivió, 1 = Sobrevivió')
plt.savefig('titanic-ejercicio4')
plt.show()