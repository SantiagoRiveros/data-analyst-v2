""" 
Ejercicio:

Crea un array 1D con los números del 10 al 20.

Extrae los elementos del 3er al 7mo.

Crea un array 2D de 3x3 y accede al elemento central.
"""
import numpy as np

arr1D = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
elementos_extraidos = arr1D[2:7]
print(elementos_extraidos)

arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2D[1, 1])

print(np.std(arr2D[1]))