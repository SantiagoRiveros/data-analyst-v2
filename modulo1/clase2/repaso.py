# Variables y tipos de datos:

entero = 3 # Es de tipo Integer (int), es decir un numero entero
flotante = 0.3 # Es tipo Float, es decir un numero decimal
string = "hola" # Es de tipo String, o cadena de caracteres, cabe recalcar que hace falta envolverlos en comillas
booleano = True # Es de tipo Bool, aceptar solo dos valores, True o False, es decir, verdadero o falso.

# Si escribo un string sin comillas, python lo va a interpretar como si fuera una variable

# Variable es un dato, donde guardamos "algo"

# La sintaxis de la variables es -> NOMBRE_DE_LA_VARIABLE = VALOR_DE_LA_VARIABLE

# ¿Que es Pytron?

""" 
Python es un lenguaje de programacion de alto nivel, interpretado, orientado a objetos, de codigo abierto y de proposito general.

Caracteristicas:

-Facil de aprender y usar:
    Python tiene una sintaxis simple y cercana al lenguaje natural, lo que facilita la lectura
    y escritura de codigo
    
-Codigo abierto:
    Es gratuito y permite su uso y distribucion, incluso con fines comerciales.
    
-Orientado a objetos:
    Permite la organizacion de codigo en objetos, facilitando la reutilizacion y el mantenimiento.
    
-Extensible:
    Python se integra facilmente con otros lenguajes como C y C++, permitiendo aprovechar
    el rendimiento de estos lenguajes de maneras criticas.
    
-Versatil:
    Se utiliza en amplia gama de aplicaciones, desde desarrollo web, hasta analisis de datos y machine learning.
    
-Amplia comunidad:
    Cuenta con una gran comunidad de usuarios y desarrolladores que contribuyen con bibliotecas
    frameworks y soporte
"""

#Ejercicio de repaso:

#Pedir al usuario su nombre y edad, y mostrar un mensaje indicando si es mayor de edad.


# Pedimos el nombre mediante consola, con el metodo input
nombre = input("Ingresa tu nombre: ")

# Lo que va dentro de los parentesis, es lo que va a mostrar en consola, para pedirle el dato al usuario

# Pedimos la edad mediante consola, con el metodo input
edad = input("Ingresa tu edad: ")

# Todo lo que ingresa por consola, se lo considera de tipo string, utilizamos el metodo int, para que lo transforme en entero
# ¿Porque hacemos esto? Porque luego si es de tipo integer, vamos a poder compararlo con numeros, Ej: edad > 3


# Condicionales if-else

if type(int(edad)) == int:
    if int(edad) >= 18:
        print(f"Hola {nombre}, eres mayor de edad")
        #la letra f, justo antes de que comienze el string, nos permite "insertar un dato" dentro del mismo
        #este dato, debe estar envuelto en llaves
    else:
        print(f"Hola {nombre}, eres menor de edad")
else:
    print("Dato de edad no es convertible a entero")
    
