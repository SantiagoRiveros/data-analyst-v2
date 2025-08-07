# Sintaxis basica del if-else

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
    
# Elif

nota = int(input("Ingrese su nota: "))

if nota >= 90:
    print("Excelente")
elif nota == 75:
    print("Bien")
elif nota >= 70:
    print("Aprobado")
else:
    print("Desaprobado")
    
#Ejercicio:
# olicitar al usuario un número y verificar si es positivo, negativo o cero.

numero = print("Seleccione un numero")

if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("EL numero es cero")