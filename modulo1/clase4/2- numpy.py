import numpy as np
# importe numpy y el "as np" es para darle "un nombre" para usarlo


# crear un array 1D
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Quiero multiplicar cada elemento del array por 2
arr2 = arr * 2
print(arr2)

""" 🧩 Ejercicio 1 - Operaciones con Arrays
Crea un array con los números del 1 al 10 y obtén:
✅ La suma total
✅ El promedio
✅ Los valores mayores a 5 """

arrayEjercicio = np.arange(1,11)
print(arrayEjercicio)

# Calcular la suma total
suma_total = np.sum(arrayEjercicio)

print("Suma Total: ", suma_total)

# Calcular el promedio
promedio = np.mean(arrayEjercicio)
print("Promedio: ", promedio)

# Mayores a 5
mayores_a_5 = arrayEjercicio[arrayEjercicio > 5]
print("Elementos mayores a 5: ", mayores_a_5)

""" 
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]

"""

array5por5 = np.arange(25).reshape(5, 5)
print(array5por5)