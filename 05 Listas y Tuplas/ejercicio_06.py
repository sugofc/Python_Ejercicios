"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

#! Forma 1
# asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
# repetir = list()

# for a in asignaturas:
#     n = int(input(f'Nota de la asignatura {a}: '))
#     if n < 4:
#         repetir.append(a)
# else:
#     print(f"Asignaturas por repetir: {repetir}")

#! Forma 2
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for a in range(len(asignaturas)-1, -1, -1):
    score = float(input(f"Nota de la asignatura {asignaturas[a]}: "))
    if score >= 5:
        asignaturas.pop(a)
print(f"Tienes que repetir {asignaturas}")