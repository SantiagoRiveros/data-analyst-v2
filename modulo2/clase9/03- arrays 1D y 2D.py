import numpy as np

# Array 1D (o unidimensional)
arr = np.array([1, 2, 3, 4, 5])
print("Array 1D:")
print(arr)

# Creacion de un array bidimensional 2D (o Matriz):
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:")
print(matriz)

# Acceder a elementos y slicing
print("Primer elemento:", arr[0])
print("Elementos del indice 1 a 3:", arr[1:4])
print("Elemento en la fila 2, columna 3 de la matriz:", matriz[1, 2])   

