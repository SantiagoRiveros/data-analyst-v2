"""  
Python es un lenguaje de programacion facil de aprender, legible y versatil, utilizado en desarrollo web,
analisis de datos, inteligencia artificial y mas
"""

# Python no requiere declarar el tipo de dato, lo asigna automaticamente
# ¿Que es una variable? Es una asignacion que hacemos en python, para guardar un dato o valor.

# Sintaxis de una variable:
# nombreDeLaVariable = valorDeLaVariable

nombre = "Juan"  # String (cadena de caracteres)
edad = 25  # Entero (Int)
altura = 1.64  # Decimal (Float)
# Booleano (bool) es un dato, que solo admite dos valores: True o False
es_estudiante = True

# Ejercicio: Crea tres variables (nombre, edad y altura) y muestra su contenido con print().

# print es un metodo o funcion, que muestra en consola, lo que le asignes, dentro de los parentesis

print(nombre)
print(edad)
print(altura)

# Otro ejercicio, ingresa un nombre por consola, y mostralo en pantalla
# input, es un metodo, por el cual, te pide ingresar algun tipo de dato, por terminal
nombreUsuario = input("¿Como te llamas?: ")
print("Hola", nombreUsuario)

# Operadores matematicos:

a = 10
b = 3
print(a + b)  # 13 suma
print(a - b)  # 7 resta
print(a * b)  # 30 multiplicacion
print(a / b)  # 3.333333333 division
print(a // b)  # 3 division entera, en la division se ignoran los decimales
print(a % b)  # 1 modulo, es el resto, de la division entera
# 10 dividido 3, es 3, ahora 3 x 3 = 9, 10 - 9 = 1, es la resta de la division

# 10 / 3 = 3                      resultado * dividendo = 9              10 - 9 = 1

print(a ** b)  # 1000 Potencia

# Condicionales:
edadUsuario = 12
if edadUsuario >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Bucles (for y while)


# Bucles for (recorriendo una lista)
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:  # Le asigna un valor temporal a cada uno de los elementos de frutas, y ejecuta el bloque de codigo de abajo, una vez por cada una
    # 1er vuelta -> fruta = "manzana"
    # 2da vuelta -> fruta = "banana"
    # 3er vuelta -> fruta = "cereza"
    print(fruta)

# Bucle while (repite hasta que se cumpla una condicion)
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # contador = contador + 1

# Funciones
# Las funciones son bloques de codigo que se pueden aislar, y ejecutar en repetidas ocasiones

# Tiene dos fases: declaracion, y ejecucion

# Declaracion


def saludar(nombreFuncion):
    print("Hola", nombreFuncion)


# Ejecucion
saludar("Juan")
saludar("Maria")
