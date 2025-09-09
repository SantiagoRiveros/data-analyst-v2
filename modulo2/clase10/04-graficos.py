import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("Titanic-Corregido.csv")

# Histograma de edades

dataframe['Age'].hist(bins=20)
plt.title("Distribucion de edades")
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.savefig("grafico.png") 
plt.show()