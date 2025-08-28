import numpy as np

arr = np.array([10, 20, 30, 40])
print("Array original:", arr)
print("Array sumado 5:", arr + 5)
print("Array multiplicado por 2:", arr * 2)

# Funciones estadisticas
print("Suma:", np.sum(arr)) # Suma todos los elementos de un array
print("Media:", np.mean(arr)) # Suma todos los elementos, y los divide por la cantidad
print("Desviacion estandar:", np.std(arr)) # Desviacion estandar, es decir, cual es la media de diferencia de los valores con la media
print("Minimo:", np.min(arr)) # devuelve el valor minimo
print("Maximo:", np.max(arr)) # Devuelve el valor maximo
