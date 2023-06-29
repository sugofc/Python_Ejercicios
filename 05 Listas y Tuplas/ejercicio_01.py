"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
lista_materia = list()
n = 0

while True:
    materia = input("Ingrese Materia: ")
    lista_materia.append(materia)
    
    print(lista_materia)
