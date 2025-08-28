""" 
Crea un array con 1 millón de números aleatorios entre 0 y 100.

Calcula la media, el máximo, el mínimo y la desviación estándar.

Luego, filtra (sin bucles explícitos) todos los valores mayores a la media y cuenta cuántos son.
"""

import numpy as np

datos = np.random.uniform(0, 100, 1000000)

# calcular estadisticas
media = np.mean(datos)
maximo = np.max(datos)
minimo = np.min(datos)
desviacion_estandar = np.std(datos)

print("Media:", media)
print("Maximo:", maximo)
print("Minimo:", minimo)
print("Desviacion estandar:", desviacion_estandar)

valores_mayores = datos[datos > media]
print("Valores mayores a la media:", valores_mayores)
print("Cantidad de valores mayores a la media:", len(valores_mayores))

""" print(np.mean([1, 5, 1000000000000000000000000000000000000000]))
print(np.std([1, 5, 1000000000000000000000000000000000000000]))

print(np.mean([1,2,3]))
print(np.std([1,2,3]))

print(np.mean([1,1,1]))
print(np.std([1,1,1])) """