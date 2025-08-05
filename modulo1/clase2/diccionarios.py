# Los diccionares, guardan pares de clave : valor

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", }
# No es una cadena, sino conjunto de datos

# Como es la sintaxis? todo envuelto en llaves {}, la clave SIEMPRE va entre comillas dobles "", el valor se lo asignas
# con 2 puntos : y separado uno del otro con una coma ,



# Como accedo al nombre de persona?
# Parecido a la lista, pero le pasas la clave que queres acceder, en vez de su posicion
print(persona["nombre"])

# En que tipo de dato, tendrian una lista de DNIs? en la lista o tupla
# En que tipo de datos, tendrias el valor de un DNI? en diccionarios

coordenadas = {"lat": "50° N", "long": "30° W"}


berazategui = {"poblacion": 500000, "provincia": "Buenos Aires", "añoDeFundacion": 1960} 

# Como eliminamos una clave?

del berazategui["provincia"]
print(berazategui)

persona2 = {"nombre": "Pepe", "edad": 25}

# Como le agrego una clave?

persona2["ciudad"] = "New York"
print(persona2)

# Como se lo modifico?
persona2["nombre"] = "Jose"
print(persona2)

# Metodos utiles:

# keys te devuelve las claves
print(persona2.keys())

# values te devuelve los valores
print(persona2.values())

#items te devuelve claves y valores
print(persona2.items())

#print(persona2["mascota"])

# Ejercicio: Crea un diccionario con información de un auto (marca, modelo, año) y actualiza el año.

auto = {"Marca": "Ford", "modelo": "Escort", "año": 1998 }

auto["año"] = 2000
print(auto)