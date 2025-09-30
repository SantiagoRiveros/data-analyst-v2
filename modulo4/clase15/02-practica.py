import matplotlib.pyplot as plt

# 1 - Grafico de linea

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Dibuja un grafico, con los valores de x en el eje horizontal, y de y en el eje vertical
plt.plot(x, y)
# Aca definimos el titulo del grafic
plt.title("Crecimiento")
# Aca definimos el "titulo" de el eje x
plt.xlabel("Tiempo")
# Aca definimos el titulo del eje y
plt.ylabel("Valor")
# Aca guardamos el grafico, lo que esta entre parentesis es el nombre del archivo
plt.savefig("grafico-de-linea")
# Aca generamos un "popup" que nos muestra el grafico
plt.show()


# 2 - Grafico de Barras
etiquetas = ['A', 'B', 'C']
valores = [10, 25, 5]

# Esto, dibuja un grafico de barras
plt.bar(etiquetas, valores)
plt.title('Comparacion de valores')
plt.savefig("grafico-de-barras")
plt.show()



# 3 - Grafico de torta

plt.pie([60, 30, 10], labels=['Parte 1', 'Parte 2', 'Parte 3'], autopct='%1.1f%%')

""" autopct='%1.1f%%' → Muestra el porcentaje en cada porción con 1 decimal.

%1.1f → significa “un número flotante con 1 decimal”.

%% → es el símbolo de porcentaje.

Ejemplo: 60.0%, 30.0%, 10.0%. """

plt.title('Distribucion de Categorias')
plt.savefig("grafico-de-torta")
plt.show()


# 4 - Histograma

import numpy as np

datos = np.random.normal(loc=50, scale=10, size=100)

""" 
👉 Genera 100 datos aleatorios que siguen una distribución normal (campana de Gauss):

loc=50 → es la media (el centro de la distribución).

scale=10 → es la desviación estándar (qué tan dispersos están los datos).

size=100 → cantidad de datos.
"""

plt.hist(datos, bins= 10)
# Bins = muestra un intervalo, es decir, va a mostrar de 10 en 10

plt.title('Distribucion de datos')
plt.savefig('histograma')
plt.show()


# 5 - Dispersion

x = np.random.rand(50)
y = x + np.random.normal(0, 0.1, 50)

plt.scatter(x, y)
plt.title('Relacion entre variables')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.savefig('dispersion')
plt.show()