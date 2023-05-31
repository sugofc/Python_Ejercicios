"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

#? Otra forma
horas = int(input("Horas trabajadas?: "))
coste = int(input("Coste por hora?: "))
pago = horas*coste

print(f"Horas trabajadas {horas}, el coste por hora es de ${coste}, tu total es ${pago}")