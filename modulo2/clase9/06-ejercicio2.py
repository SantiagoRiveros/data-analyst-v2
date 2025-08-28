""" 
Crea un array con los números [4, 8, 15, 16, 23, 42] y calcula su suma, promedio y desviación estándar.

Eleva al cuadrado cada elemento del array y luego calcula la raíz cuadrada de cada uno.
"""

import numpy as np

arr = np.array([4, 8, 15, 16, 23, 42])

print("Suma:", np.sum(arr))
print("Promedio:", np.mean(arr))
print("Desviacion Estandar:", np.std(arr))

print("Elevado al cuadrado:", arr ** 2)
print("Raiz cuadrada:", np.sqrt(arr))

elevado = arr ** 2
raiz = np.sqrt(elevado)

print(raiz)

