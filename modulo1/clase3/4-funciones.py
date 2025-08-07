# Crear una función que reciba un nombre y una edad, y retorne un mensaje indicando si la persona es mayor de edad o no.

# Que es unaf uncion
# Es un bloque de codigo reutilizable que realiza una tarea especifica

# Sintaxis:

def mensajes(nombre, edad):
    if edad >= 18:
        print(f"{nombre} es mayor de edad")
    else:
        print(f"{nombre} es menor de edad")
        
mensajes("Roberto", 11)
mensajes("Cristian", 21)