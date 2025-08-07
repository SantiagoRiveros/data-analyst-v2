#📌 Actividad Final:
# Crear un programa que almacene una lista de estudiantes en un diccionario y permita consultar datos.

# ----------------------------
estudiantes = {
    "001" : {"nombre": "Juan", "edad": 20, "curso": "Python"},
    "002" : {"nombre": "Ana", "edad": 22, "curso": "Data Science"}
}

codigo = input("Ingrese el codigo del estudiante: ")

# Declaracion de funcion

def consultarEstudiante(codigoEstudiante, listaEstudiantes):
    if codigoEstudiante in listaEstudiantes:
        print(listaEstudiantes[codigoEstudiante])
    else:
        print("Estudiante no encontrado")
        
        
# Ejecucion
consultarEstudiante(codigo, estudiantes)