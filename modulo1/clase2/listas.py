# Listas

# Las listas son estructuras ordenadas y mutables.
#Sintaxis:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Puede tener mas o menos longitud
# Es una cadena de datos, de longitud variable, los cuales se separan unos del otro con comas
# Ademas, la posicion de un dato, es importante, ya que para acceder a el, vamos a hacerlo con su posicion
# Ejemplo en lenguaje natural: Quiero acceder al dato en la posicion 4 de la variable X

frutas = ["manzana", "naranja", "pomelo", "kiwi"]

#posiciones   0         1         2         3

# Como es la sintaxis para imprimir algo en X posicion?
# NOMBRE_DE_LA_LISTA[POSICION_A_LA_QUE_SE_QUIERE_ACCEDER]
print(frutas[2])

# Cabe destacar que en las listas, se pueden mezclar tipos de datos

ejemploListaVariada = ["Pomelo", "Mandarina", True, False, 0, 6, 5, 1.87, 1.92, ["Hola", 5, 8]]
ejemploMasSimple = ["hola", "chau", [1, 2, 3]]
#                    0       1     2

print(ejemploMasSimple[2][2])

# Metodos utiles para listas:
verduras = ["lechuga", "tomate", "morron", "lechuga"]
#metodo append, sirve, para agregar un elemento
verduras.append("zanahoria")
print(verduras)

# metodo remove, sirve para eliminar un elemento
verduras.remove("lechuga")
print(verduras)

#Cuando tiene mas de un elemento, elimina el primero que encuentra

#metodo len, para saber la longitud de una lista
print(len(verduras))

# Subslicing
print(verduras[1:3])
# El primer numero lo incluye, el ultimo no

#Ejercicio: Crea una lista con 5 ciudades, agrega otra ciudad y elimina la segunda.

ciudades = ["Berazategui", "Florencio Varela", "Lomas de Zamora", "Quilmes", "La Plata"]

# Agregamos otra ciudad
ciudades.append("Lanus")
print(ciudades)

# vamos a eliminar la segunda
# ciudades.remove(1) <- Esto da error, porque no encuentra 1 en la lista

# Lo que esta en segunda posicion = ciudades[1]
print(ciudades[1] == "Florencio Varela")
ciudades.remove(ciudades[1])
print(ciudades)
