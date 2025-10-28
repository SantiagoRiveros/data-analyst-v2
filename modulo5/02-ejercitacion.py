# 1 - Calcular la media de visitantes por pais
import pandas as pd
import numpy as np

dataframe = pd.read_csv("InternationalVisitorArrivalsbyCountryofNationality.csv")

media_por_pais = dataframe.groupby("con")["arv_count"].mean().sort_values(ascending=False)

print(media_por_pais)

# 2- Calcular mediana y moda
mediana_por_pais = dataframe.groupby("con")["arv_count"].median()
print("MEDIANA ------------------------")
print(mediana_por_pais)

print("MODA -----------------------")

moda_por_pais = dataframe.groupby("con")["arv_count"].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)


print(moda_por_pais)

# 3. Desviación estándar por país
desviacion_por_pais = dataframe.groupby("con")["arv_count"].std()

print("STD -------------------------")

print(desviacion_por_pais)


print("DISPERSION ----------------")

# DIspersion por region
dispersión_por_region = dataframe.groupby("region")["arv_count"].std().sort_values(ascending=False)

print(dispersión_por_region)

# Grafico
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
dispersión_por_region.plot(kind="bar")
plt.title("Desviación estándar de visitantes por región")
plt.ylabel("Desviación estándar")
plt.xlabel("Región")
plt.savefig("Dispersion por region.jpg")
plt.show()